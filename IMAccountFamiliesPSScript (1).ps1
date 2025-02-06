# Define the parameters for the API request
$accessKey = "insert"

# Define the API endpoint
$apiUrl = "https://api.cloudcheckr.com/api/billing.json/get_account_family_v2"

# Define the path to the CSV file containing cc_account_ids
$csvPath = ""C:\Users\dwaitt\Downloads\accounts_export_2024-12-17 23_02_38.xlsx"" 

# Read the cc_account_ids from the CSV file
$ccAccountIds = Import-Csv -Path $csvPath | Select-Object -ExpandProperty cc_account_id

# Set headers for the request
$headers = @{
    "Content-Type" = "application/json"
}

# Initialize an array to store results
$resultData = @()

# Loop through each cc_account_id and send the API request
foreach ($ccAccountId in $ccAccountIds) {
    # Prepare the request body
    $body = @{
        use_cc_account_id = $ccAccountId
        access_key = $accessKey
    } | ConvertTo-Json -Depth 10

    try {
        Write-Host "Sending request to CloudCheckr API for cc_account_id: $ccAccountId..."
        $response = Invoke-RestMethod -Uri $apiUrl -Method POST -Body $body -Headers $headers

        # Check if the response contains data
        if ($response -and $response.account_families) {
            Write-Host "Data received for cc_account_id: $ccAccountId."
            $resultData += $response.account_families
        } else {
            Write-Host "No account family data found for cc_account_id: $ccAccountId."
        }
    } catch {
        Write-Error "An error occurred for cc_account_id $ccAccountId: $_"
    }
}

# Export all collected data to CSV
if ($resultData.Count -gt 0) {
    Write-Host "Exporting all data to IMAccountFamilies.csv..."
    $resultData | Export-Csv -Path "IMAccountFamilies.csv" -NoTypeInformation -Force
    Write-Host "Data successfully exported to IMAccountFamilies.csv"
} else {
    Write-Host "No data to export."
}