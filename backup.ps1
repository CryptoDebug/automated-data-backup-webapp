$source = "C:\MyWebApp\data.txt"
$dest = "C:\Backup"
$logFile = "C:\MyWebApp\backup.log"

if (-not (Test-Path -Path $dest)) {
    New-Item -ItemType Directory -Path $dest
}

try {
    Copy-Item -Path $source -Destination $dest -Force
    $message = "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') - Sauvegarde réussie"
} catch {
    $message = "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') - Erreur de sauvegarde : $_"
}

Add-Content -Path $logFile -Value $message