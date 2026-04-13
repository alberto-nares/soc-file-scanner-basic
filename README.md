# SOC File Scanner (Basic)

## Description
This project simulates a basic Security Operations Center (SOC) task by detecting executable files in a user directory.

## Objective
Identify potentially suspicious executable files (.exe) located outside standard installation directories.

## Environment
- OS: Windows 10 (Virtual Machine)
- Language: Python
- Path analyzed: C:\SOC_Lab

## How it works
The script scans a directory and classifies files:
- [OK] Non-executable files
- [ALERT] Executable files (.exe)

## Example Output
[OK] archivo1.txt  
[OK] foto.jpg  
[ALERT] virus.exe  

## Skills demonstrated
- Basic scripting (Python)
- File analysis
- Security mindset (threat detection)
- SOC environment simulation

---

## Improvements

This version includes enhanced detection capabilities:

- Detection of double extension files (e.g. file.jpg.exe)
- Basic threat counting
- Improved alert classification:
  - [ALERTA] Executable detected
  - [CRITICO] Evasion technique detected

## Example (Improved Output)

[ALERTA] Ejecutable detectado: virus.exe  
[ALERTA] Ejecutable detectado: foto.jpg.exe  
[CRITICO] Posible evasión por doble extensión: foto.jpg.exe  

Total de archivos sospechosos: 2

---

## Logging Feature

This version includes log generation for audit and incident response purposes.

- Logs are automatically generated with timestamp
- Each scan creates a new log file
- Logs store all scan results including alerts and critical detections

## Example Log Output

=== LOG DE ESCANEO SOC ===

[OK] archivo1.txt  
[ALERTA] virus.exe  
[CRITICO] foto.jpg.exe  

Total de archivos sospechosos: 2
