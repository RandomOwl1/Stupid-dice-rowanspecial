#!/bin/bash

# Function to install Python3 (Windows or Linux / macOS)
install_python3() {
    # Detect OS
    OS=$(uname)

    if [[ "$OS" == "Linux" ]]; then
        echo "Detected Linux. Installing Python3..."
        # Update package list and install Python3 (for Debian-based systems)
        sudo apt-get update
        sudo apt-get install python3 python3-pip -y
    elif [[ "$OS" == "Darwin" ]]; then
        echo "Detected macOS. Installing Python3..."
        # Install Python3 using Homebrew
        if ! command -v brew &>/dev/null; then
            echo "Homebrew is not installed. Installing Homebrew first..."
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        fi
        brew install python3
    elif [[ "$OS" == "CYGWIN"* || "$OS" == "MINGW"* ]]; then
        echo "Detected Windows. Please manually install Python3 from https://www.python.org/downloads/."
        exit 1
    else
        echo "Unsupported operating system. Please install Python3 manually."
        exit 1
    fi
}

# Check if Python3 and pip are installed
if ! command -v python3 &>/dev/null; then
    echo "Python3 is not installed. Installing Python3..."
    install_python3
fi

if ! command -v pip3 &>/dev/null; then
    echo "pip3 is not installed. Installing pip3..."
    python3 -m ensurepip --upgrade
fi

# Install required Python packages
echo "Installing required Python packages..."
pip3 install random time sys os platform

# Check if the installation was successful
if [ $? -eq 0 ]; then
    echo "Python packages installed successfully!"
else
    echo "Failed to install Python packages. Please check for errors."
    exit 1
fi

# Run another .sh script in the current working directory
if [ -f "./another_script.sh" ]; then
    echo "Running another_script.sh..."
    ./another_script.sh
else
    echo "another_script.sh not found in the current directory."
    exit 1
fi
