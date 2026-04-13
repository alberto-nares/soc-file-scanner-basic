import os

ruta = "C:\\SOC_Lab"
contador_alertas = 0

print("=== INICIO DE ESCANEO SOC ===\n")

for archivo in os.listdir(ruta):
    
    if archivo.endswith(".exe"):
        print(f"[ALERTA] Ejecutable detectado: {archivo}")
        contador_alertas += 1

        # Detección de doble extensión
        if "." in archivo[:-4]:
            print(f"[CRITICO] Posible evasión por doble extensión: {archivo}")

    else:
        print(f"[OK] Archivo seguro: {archivo}")

print("\n=== RESUMEN ===")
print(f"Total de archivos sospechosos: {contador_alertas}")
print("\nEscaneo finalizado.")