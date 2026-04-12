import os

ruta = "C:\\SOC_Lab"

print("Iniciando escaneo...\n")

for archivo in os.listdir(ruta):
    if archivo.endswith(".exe"):
        print(f"[ALERTA] Archivo ejecutable detectado: {archivo}")
    else:
        print(f"[OK] Archivo no ejecutable: {archivo}")

print("\nEscaneo finalizado.")