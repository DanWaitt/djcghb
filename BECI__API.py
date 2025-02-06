import requests
import json
import time
import pandas as pd

api_token = '**********************************'
start_date = "2024-12-01T00:00:00Z"
end_date = "2024-12-31T23:59:59.999Z"

def get_cost_query(token, post_payload):
# Define the URL and header for the POST request
    post_url = "https://api.spotinst.io/cloudBilling/v1/cost/query"
    
    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
    }

    # Make the POST request
    post_response = requests.request("POST", post_url, headers=headers, data=post_payload)

    # Print the response from the POST request
    print("POST response:", post_response.status_code)

    # Extract the response ID from the POST response
    response_data = post_response.json()
    response_id = response_data['response']['items'][0]['id']

    # Define the URL for the GET request using the response ID
    get_url = f"https://api.spotinst.io/cloudBilling/v1/cost/query/{response_id}"

    # Poll the status of the query until it is completed
    status = None
    while status != "Completed":
        get_response = requests.request("GET", get_url, headers=headers)
        status_data = get_response.json()
        status = status_data['response']['items'][0]['state']
        print("Current status:", status)
        if status != "Completed":
            time.sleep(5)  # Wait for 5 seconds before checking again

    # Once the status is completed, download the data
    download_url = f"https://api.spotinst.io/cloudBilling/v1/cost/query/{response_id}/downloadLink"
    download_response = requests.request("GET", download_url, headers=headers).json()
    download_link = download_response['response']['items'][0]['downloadLink']
    data_downloaded = requests.get(download_link)

    # Check if the request was successful
    if data_downloaded.status_code == 200:
        # Load the content into a DataFrame
        from io import StringIO
        data = StringIO(data_downloaded.text)
        df = pd.read_csv(data)
        print("Data downloaded successfully.")
        #print(df.head())  # Display the first few rows of the DataFrame
    else:
        print(f"Failed to download data. Status code: {download_response.status_code}")

    return df 


def get_cost_not_tagged(data1, data2):
    # Convert the lists to DataFrames
    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)

    # Step 1: Sum the EFFECTIVECOST in df1
    df1_sum = df1.groupby(['SUBACCOUNTID', 'SERVICENAME'])['EFFECTIVECOST'].sum().reset_index()

    # Step 2: Merge this sum with df2
    df_merged = pd.merge(df2, df1_sum, on=['SUBACCOUNTID', 'SERVICENAME'], suffixes=('', '_df1'), how='outer')

    # Step 3: Subtract the summed EFFECTIVECOST from df2's EFFECTIVECOST and store the result in a new column
    df_merged['EFFECTIVECOST_DIFF'] = df_merged['EFFECTIVECOST'] - df_merged['EFFECTIVECOST_df1']

    # Step 4: Update the EFFECTIVECOST column with the values from EFFECTIVECOST_DIFF where applicable
    df_merged.loc[df_merged['EFFECTIVECOST_DIFF'].notnull(), 'EFFECTIVECOST'] = df_merged['EFFECTIVECOST_DIFF']
    
    # Step 5: Add a new column called "Tag Value" to df_merged
    df_merged['Tag Value'] = None

    # Step 6: Append all rows from df1 to df_merged
    df_merged = pd.concat([df_merged, df1], ignore_index=True)

    # Display the resulting dataframe
    #print(df_merged)

    return df_merged    

def main():
    #call get_cost_query() for Cost Center Tags
    payload1 = json.dumps({
    "costQuery": {
        "includeZeroCosts": True,
        "includeQuantity": False,
        "startDate": start_date,
        "endDate": end_date,
        "groupBy": [
        "tagValue",
        "serviceName",
        "subAccountId"
        ],
        "filter": "tags['Cost Center'] eq *",
        "useFinOpsApiFilterSpec": True
    }
    })

    payload2 = json.dumps({
    "costQuery": {
        "includeZeroCosts": True,
        "includeQuantity": False,
        "startDate": start_date,
        "endDate": end_date,
        "groupBy": [
        "serviceName",
        "subAccountId"
        ],
        "useFinOpsApiFilterSpec": True
    }
    })
    
    #Get Costs by Cost Center, filtered by cost center and get all costs
    cost_center_costs = get_cost_query(api_token, payload1)
    #print(cost_center_costs.head())

    all_costs = get_cost_query(api_token, payload2)
    #cost_center_costs.to_csv('allcosts.csv', index=False)
    #send both responses to get_cost_not_tagged() and then still need to do the subtraction piece (EFFECTIVECOST - SUM_EFFECTIVECOST)
    invoice = get_cost_not_tagged(cost_center_costs,all_costs)

    # Save the downloaded data to a file
    invoice.to_csv('output.csv', index=False)
    
    #print(invoice.head())

if __name__ == '__main__':
    main()
