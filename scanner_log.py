import os
from datetime import datetime

ruta = "C:\\SOC_Lab"
contador_alertas = 0

# Generar nombre de log con fecha
fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file = f"C:\\SOC_Lab\\log_{fecha}.txt"

print("=== INICIO DE ESCANEO SOC ===\n")

with open(log_file, "w") as log:
    log.write("=== LOG DE ESCANEO SOC ===\n\n")

    for archivo in os.listdir(ruta):

        if archivo.endswith(".exe"):
            mensaje = f"[ALERTA] Ejecutable detectado: {archivo}"
            print(mensaje)
            log.write(mensaje + "\n")
            contador_alertas += 1

            if "." in archivo[:-4]:
                critico = f"[CRITICO] Doble extensión detectada: {archivo}"
                print(critico)
                log.write(critico + "\n")

        else:
            mensaje = f"[OK] Archivo seguro: {archivo}"
            print(mensaje)
            log.write(mensaje + "\n")

    resumen = f"\nTotal de archivos sospechosos: {contador_alertas}"
    print(resumen)
    log.write(resumen)

print(f"\nLog generado en: {log_file}")