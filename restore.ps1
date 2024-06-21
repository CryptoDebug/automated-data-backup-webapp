$source = "C:\Backup\data.txt"
$dest = "C:\MyWebApp\data.txt"
$logFile = "C:\MyWebApp\restore.log"

# Copier le fichier de sauvegarde vers l'emplacement original
try {
    Copy-Item -Path $source -Destination $dest -Force
    $message = "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') - Restauration réussie"
} catch {
    $message = "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') - Erreur de restauration : $_"
}

# Écriture dans le fichier de log
Add-Content -Path $logFile -Value $message