@echo off

set "OUTDIR=salida"
set "ZIPNAME=SegranchCompress.zip"

if not exist "%OUTDIR%" mkdir "%OUTDIR%"

echo Comprimiendo todo en %OUTDIR%\%ZIPNAME%...

for %%f in (*) do (
    if /I not "%%f"=="%OUTDIR%" (
        tar -a -c -f "%OUTDIR%\%ZIPNAME%" "%%f"
    )
)

pause