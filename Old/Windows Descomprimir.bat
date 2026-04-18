@echo off

set "INDIR=entrada"
set "OUTDIR=salida"

if not exist "%INDIR%" (
    echo No existe la carpeta %INDIR%
    pause
    exit /b
)

if not exist "%OUTDIR%" (
    mkdir "%OUTDIR%"
)

echo Limpiando carpeta %OUTDIR%...
rmdir /s /q "%OUTDIR%"
mkdir "%OUTDIR%"

for %%f in ("%INDIR%\*.zip") do (
    echo Descomprimiendo %%~nxf en %OUTDIR%...
    tar -xf "%%f" -C "%OUTDIR%"
)

pause