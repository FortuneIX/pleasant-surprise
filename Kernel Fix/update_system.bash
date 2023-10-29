# Update package information
sudo apt update
sudo apt upgrade

# Check if an NVIDIA GPU is present
if lspci | grep -i nvidia; then
    echo "NVIDIA GPU detected. Installing NVIDIA drivers..."
    ubuntu-drivers devices
    sudo ubuntu-drivers autoinstall
    echo "NVIDIA drivers installed."
else
    echo "No NVIDIA GPU detected. Skipping driver installation."
fi

# Check for Intel CPU
if lscpu | grep -i 'genuineintel'; then
    echo "Intel CPU detected. Checking for Intel microcode updates..."
    sudo apt install intel-microcode
    echo "Intel microcode updates installed."
else
    echo "No Intel CPU detected. Skipping Intel microcode update."
fi



sudo reboot