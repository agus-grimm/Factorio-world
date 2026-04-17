@echo off

set "INDIR=entrada"
set "OUTDIR=salida"
set "ZIPNAME=Segranch.zip"

if not exist "%OUTDIR%" (
    echo No existe la carpeta %OUTDIR%
    pause
    exit /b
)

if not exist "%INDIR%" (
    mkdir "%INDIR%"
)

echo Limpiando carpeta %INDIR%...
rmdir /s /q "%INDIR%"
mkdir "%INDIR%"

echo Comprimiendo contenido de %OUTDIR% en %INDIR%\%ZIPNAME%...
tar -a -c -f "%INDIR%\%ZIPNAME%" -C "%OUTDIR%" *

echo Listo.
pause