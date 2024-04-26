@echo off

git submodule update --init --recursive

echo Installing virtualenv...
pip install virtualenv

echo Creating virtual environment...
python -m venv src/env

echo Activating virtual environment...
call .\src\env\Scripts\activate

echo Installing project requirements...
pip install -r src/requirements.txt

echo Installing AI requirements...
pip install -r src/ai/requirements.txt

echo Installation completed.
pause


