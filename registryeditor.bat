@echo off
setlocal EnableDelayedExpansion

REM Change the path to your Python executable and script
set "PYTHON_EXECUTABLE=C:\Users\%USERNAME%\AppData\Local\Microsoft\WindowsApps\python.exe"
set "PYTHON_SCRIPT=path_to_your_script"

powershell -WindowStyle Hidden -Command "Start-Process '%PYTHON_EXECUTABLE%' -ArgumentList '\"%PYTHON_SCRIPT%\"' -Verb RunAs"
