#name: Daniel Waitt
#studentId: 011912918

#Task 1: Scripting In PowerShell 

#options displayed until the 5 is selected

do { 
    Write-Host "Option Selection"
    Write-Host "1. List .log files in the Requirements1 folder (to DailyLog.txt)"
    Write-Host "2. List files in Requirements1 in tabular format (Alphabetically to C916contents.txt)"
    Write-Host "3. List Current CPU and Memory Usage"
    Write-Host "4. List running processes sorted by virtual size"
    Write-Host "5. Exit script"

#User Input message 

    $choice = Read-Host "Enter a number (1-5)"

    
    switch ($choice) {

         #Step B1: List .log files in Requirements1 folder with current date and redirect to DailyLog.txt

        1 {
        try {
            $logFiles = Get-ChildItem -Path $PSScriptRoot -Filter "*.log" | Select-Object -ExpandProperty Name
            $logFilesWithDate = "$(Get-Date) - $($logFiles -join ', ')"
            Add-Content -Path "$PSScriptRoot\DailyLog.txt" -Value $logFilesWithDate
            Write-Host "Saved to DailyLog.txt"
        }
        catch [System.OutOfMemoryException] {
            Write-Host "Error: System.OutOfMemoryException error occured"
        }
        }

        #Step B2: List files in Requirements1 folder in alphabetical order and output to C916contents.txt

        2 {
        try {
            $files = Get-ChildItem "Requirements1" | Select-Object Name
            $files | Sort-Object Name | Format-Table -Property Name, Mode, LastWriteTime, Length | Out-File -FilePath "$PSScriptRoot\C916contents.txt"
            Write-Host "Saved to C916contents.txt"
        }
        catch [System.OutOfMemoryException] {
            Write-Host "Error123: System.OutOfMemoryException error occured"
        }
        }

        #Step B3: Show current CPU and memory usage

        3 {
        try {
            $cpuUsage = Get-CimInstance -Class Win32_Processor | Select-Object -ExpandProperty LoadPercentage
            $memoryUsage = Get-CimInstance -Class Win32_OperatingSystem | Select-Object -Property FreePhysicalMemory, TotalVisibleMemorySize

            Write-Host "Current CPU Usage: $cpuUsage%"
            Write-Host "Free Physical Memory: $($memoryUsage.FreePhysicalMemory) KB"
            Write-Host "Total Visible Memory: $($memoryUsage.TotalVisibleMemorySize) KB"
        }
        catch [System.OutOfMemoryException] {
            Write-Host "Error123: System.OutOfMemoryException error occured"
        }
        }

        #Step B4: List running processes sorted by virtual size in grid format

        4 {
        try {
            Get-Process | Sort-Object -Property VM | Select-Object -Property Id, ProcessName, 
            @{Name="VM (MB)";Expression={[math]::round($_.VM / 1MB, 2)}} | Out-GridView
        }
        catch [System.OutOfMemoryException] {
            Write-Host "Error123: System.OutOfMemoryException error occured"
        }
        }

        #Step B5: Exit the script

        5 {
            Exit-PSHostProcess
            Write-Host "GoodBye"
        }

        #Invalid Choice

        default {
            Write-Host "Invalid selection. Please enter 1-5"
        }
    }
} 

while ($choice -ne "5")

#Step D: Apply exception handling using try-catch for System.OutOfMemoryException for each option.
#try {#Code#}
#catch [System.OutOfMemoryException] {Write-Host "Error123: System.OutOfMemoryException error occured"}




