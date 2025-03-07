#Name: Daniel Waitt
#StudentId: 011912918

#Step B1: Check for existance of AD OU Finance

$ouExists = Get-ADOrganizationalUnit -Filter {Name -eq 'Finance'} -ErrorAction SilentlyContinue

if ($ouExists) {
    Write-Host "The Finance OU already exists. Deleting"
    Remove-ADOrganizationalUnit -Identity $ouExists -Recursive -Confirm:$false
    Write-Host "The Finance OU has been deleted"
}

#Step B2: Create a new AD OU Finance

Write-Host "Creating the Finance OU"
New-ADOrganizationalUnit -Name Finance -ProtectedFromAccidentalDeletion $false
Write-Host "The Finance OU has been created"

#Step B3: Import the fiancePersonnel.csv into AD OU Finance

$csvPath = Join-Path $PSScriptRoot 'financePersonnel.csv'
$users = Import-csv -Path $csvPath
$Path = "OU=Finance,DC=consultingfirm,DC=com"

foreach ($ADUser in $users) {
    $firstname = $ADUser.First_Name
    $lastname = $ADUser.Last_Name
    $displayname = $firstname + " " + $lastname
    $postalcode = $ADUser.PostalCode
    $officephone = $ADUser.OfficePhone
    $mobilephone = $ADUser.MobilePhone

    if ($displayname.Length -gt 20) {
        $displayname = $displayname.Substring(0, 20)
    }
    $name = "$firstname $lastname"

    $userParams = @{
        SamAccountName = $samAcct
        GivenName = $firstname
        Surname = $lastname
        DisplayName = $displayname
        Postalcode = $postalcode
        OfficePhone = $officephone
        MobilePhone = $mobilephone
        AccountPassword = (ConvertTo-SecureString 'P@ssw0rd!23' -AsPlainText -Force)
        Enabled = $true
        Path = $Path
        Name = $name
    }
    try {
        Write-Host "Creating User '$displayname', $firstname', '$lastname', '$postalcode', '$officephone', '$mobilephone'"
        New-ADUser @userParams -ErrorAction Stop
        Write-Host "User '$displayname' has been created."
    }
    catch {
        Write-Host "An error occured while creating user '$displayname' : $_"
    }
}
#Step B4: Generate the output file for submission

$adResultsPath = Join-Path $PSScriptRoot '.\AdResults.txt'

try {
    $users = Get-ADUser -Filter * -SearchBase 'ou=Finance,dc=consultingfirm,dc=com' -Properties DisplayName, PostalCode, OfficePhone, MobilePhone > .\AdResults.txt
    $adResultsPath = Join-Path $PSScriptRoot 'AdResults.txt'
   
    $users | ForEach-Object {
        $user = $_
        $output = "Display Name: $($user.DisplayName)"
        $output += "`nPostal Code: $($user.PostalCode)"
        $output += "`nOffice Phone: $($user.OfficePhone)"
        $output += "`nMobile Phone: $($user.MobilePhone)"
        $output += "`n"
       
        $output | Out-File -FilePath $adResultsPath -Append -Encoding UTF8
    }

    Write-Host "The AdResults.txt file has been generated"
}
catch {
    Write-Host "An error occurred while generating the AdResults.txt file: $_"
}
