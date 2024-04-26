# Desactivar la impresión de los comandos
$VerbosePreference = "SilentlyContinue"

git submodule update --init --recursive

# Instalar virtualenv
Write-Host "Installing virtualenv..."
pip install virtualenv

# Crear el entorno virtual
Write-Host "Creating virtual environment..."
python -m venv src\env

# Activar el entorno virtual
Write-Host "Activating virtual environment..."
. .\src\env\Scripts\Activate

# Instalar los requisitos del proyecto
Write-Host "Installing project requirements..."
pip install -r src\requirements.txt

# Instalar los requisitos de PyGraphics
Write-Host "Installing AI requirements..."
pip install -r src\ai\requirements.txt

Write-Host "Installation completed."
pause