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
