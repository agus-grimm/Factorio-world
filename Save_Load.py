#!/usr/bin/env python3
import os
import sys
import zipfile
import shutil
from pathlib import Path
from datetime import datetime

INDIR  = Path("entrada")
OUTDIR = Path("salida")
ZIPNAME = "Segranch.zip"

def comprimir():
    # Verificar que salida existe
    if not OUTDIR.exists():
        print(f"No existe la carpeta {OUTDIR}")
        return
    
    # Crear carpeta de backups si no existe
    backups_dir = Path("backups")
    if not backups_dir.exists():
        backups_dir.mkdir(parents=True)
    
    # Crear nueva carpeta entrada si no existe
    if not INDIR.exists():
        print(f"No existe la carpeta {INDIR}, creándola...")
        INDIR.mkdir(parents=True)

    # Comprimir salida
    zip_path = INDIR / ZIPNAME
    print(f"Comprimiendo {OUTDIR} en {zip_path}...")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for file in OUTDIR.rglob("*"):
            zf.write(file, file.relative_to(OUTDIR))

    # Carpeta destino en ../saves
    saves_dir = Path("..").resolve()
    target_zip = saves_dir / ZIPNAME
    
    # Hacer backup del archivo anterior en ../saves
    if target_zip.exists():
        print(f"Haciendo backup de {target_zip.name}...")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_zip = backups_dir / f"{ZIPNAME[:-4]}_backup_{timestamp}.zip"
        shutil.copy2(target_zip, backup_zip)
        print(f"  Backup guardado en {backup_zip}")
    
    # Copiar el nuevo .zip a ../saves
    print(f"Copiando {zip_path.name} a {saves_dir}...")
    shutil.copy2(zip_path, target_zip)
    
    print("Listo.")

def descomprimir():
    # Buscar archivos .zip en la carpeta padre (./.factorio/saves)
    saves_dir = Path("..").resolve()
    zip_files = list(saves_dir.glob("*.zip"))
    
    if not zip_files:
        print(f"No hay archivos .zip en {saves_dir}")
        return
    
    # Mostrar lista de archivos disponibles
    print("Archivos .zip disponibles:")
    for i, zip_file in enumerate(zip_files, 1):
        print(f"  {i}) {zip_file.name}")
    
    # Pedir selección al usuario
    while True:
        try:
            opcion = int(input("Selecciona un archivo [número]: ").strip()) - 1
            if 0 <= opcion < len(zip_files):
                selected_zip = zip_files[opcion]
                break
            else:
                print("Opción inválida.")
        except ValueError:
            print("Por favor ingresa un número válido.")
    
    # Crear carpeta de backups si no existe
    backups_dir = Path("backups")
    if not backups_dir.exists():
        backups_dir.mkdir(parents=True)
    
    # Hacer backup del salida anterior
    if OUTDIR.exists():
        print(f"Haciendo backup de {OUTDIR}...")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_folder = backups_dir / f"salida_backup_{timestamp}"
        shutil.copytree(OUTDIR, backup_folder)
        print(f"  Backup guardado en {backup_folder}")
        
        # Limpiar salida
        shutil.rmtree(OUTDIR)

    # Crear entrada si no existe
    if not INDIR.exists():
        print(f"No existe la carpeta {INDIR}, creándola...")
        INDIR.mkdir(parents=True)

    # Crear salida
    OUTDIR.mkdir()

    # Descomprimir el archivo seleccionado
    print(f"Descomprimiendo {selected_zip.name} en {OUTDIR}...")
    with zipfile.ZipFile(selected_zip, "r") as zf:
        zf.extractall(OUTDIR)

    print("Listo.")

if __name__ == "__main__":
    print("¿Qué querés hacer?")
    print("  1) Cargar/Comprimir   (salida → entrada/Segranch.zip)")
    print("  2) Salvar/Descomprimir (entrada/*.zip → salida)")
    opcion = input("Opción [1/2]: ").strip()

    if opcion == "1":
        comprimir()
    elif opcion == "2":
        descomprimir()
    else:
        print("Opción inválida.")
        sys.exit(1)