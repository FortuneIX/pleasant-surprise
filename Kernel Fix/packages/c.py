# Optional USE ONLY IF BASH IS NOT WORKING!

import subprocess

# Check for NVIDIA GPU
nvidia_check = subprocess.run(['lspci | grep -i nvidia'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
if nvidia_check.returncode == 0:
    print("NVIDIA GPU detected. Installing NVIDIA drivers...")
    subprocess.run(['ubuntu-drivers devices'], shell=True)
    subprocess.run(['sudo ubuntu-drivers autoinstall'], shell=True)
    print("NVIDIA drivers installed.")
else:
    print("No NVIDIA GPU detected. Skipping NVIDIA driver installation.")

# Check for Intel CPU
intel_check = subprocess.run(['lscpu | grep -i "genuineintel"'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
if intel_check.returncode == 0:
    print("Intel CPU detected. Checking for Intel microcode updates...")
    subprocess.run(['sudo apt install intel-microcode'], shell=True)
    print("Intel microcode updates installed.")
else:
    print("No Intel CPU detected. Skipping Intel microcode update.")

# Update and upgrade packages
subprocess.run(['sudo apt update'], shell=True)
subprocess.run(['sudo apt upgrade -y'], shell=True)

# Install Python
subprocess.run(['sudo apt install python3 -y'], shell=True)

# Check for GPU driver updates
nvidia_check = subprocess.run(['lspci | grep -i nvidia'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
if nvidia_check.returncode == 0:
    print("Checking for GPU driver updates...")
    subprocess.run(['ubuntu-drivers devices'], shell=True)
    print("GPU driver check completed.")

# Reboot your computer to apply changes
subprocess.run(['sudo reboot'], shell=True)
