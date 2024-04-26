# Desactivar la impresión de los comandos
$VerbosePreference = "SilentlyContinue"

# Activar el entorno virtual
Write-Host "Activating virtual environment..."
. .\env\Scripts\Activate

Write-Host "Invoke..."
python main.py