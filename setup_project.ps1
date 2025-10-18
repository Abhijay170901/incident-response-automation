# PowerShell script to create Incident Response Automation project skeleton

# Base project directory
$baseDir = "C:\Users\abhij\incident-response-automation"

# Folder structure
$folders = @(
    "scanners",
    "alerts",
    "automation",
    "reports",
    "docs",
    "tests"
)

# Create base directory
if (-Not (Test-Path $baseDir)) {
    New-Item -Path $baseDir -ItemType Directory
    Write-Host "Created base directory: $baseDir"
} else {
    Write-Host "Base directory already exists: $baseDir"
}

# Create subfolders
foreach ($folder in $folders) {
    $fullPath = Join-Path $baseDir $folder
    if (-Not (Test-Path $fullPath)) {
        New-Item -Path $fullPath -ItemType Directory
        Write-Host "Created folder: $fullPath"
    } else {
        Write-Host "Folder already exists: $fullPath"
    }
}

# Create placeholder files
$files = @(
    @{Path="main.py"; Content="# main.py`nprint('Incident Response Automation Skeleton')"},
    @{Path="requirements.txt"; Content="requests`npandas"},
    @{Path="scanners\scanner_placeholder.py"; Content="def scan():`n    print('Scanning placeholder')"},
    @{Path="alerts\alert_parser_placeholder.py"; Content="def parse():`n    print('Parsing alerts placeholder')"},
    @{Path="automation\response_placeholder.py"; Content="def respond():`n    print('Automated response placeholder')"},
    @{Path="tests\test_placeholder.py"; Content="def test_placeholder():`n    assert True, 'Placeholder test passed'"},
    @{Path="docs\README.md"; Content="# Incident Response Automation Docs`nProject documentation and playbooks"}
)

foreach ($file in $files) {
    $filePath = Join-Path $baseDir $file.Path
    if (-Not (Test-Path $filePath)) {
        Set-Content -Path $filePath -Value $file.Content
        Write-Host "Created file: $filePath"
    } else {
        Write-Host "File already exists: $filePath"
    }
}

Write-Host "✅ Project skeleton created successfully!"
