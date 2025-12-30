#!/bin/bash

set -e

# Install dependencies

sudo apt update
sudo apt install -y ansible make git wget python3-venv
sudo wget https://github.com/bcicen/ctop/releases/download/v0.7.7/ctop-0.7.7-linux-amd64 -O /usr/local/bin/ctop
sudo chmod +x /usr/local/bin/ctop

# Install Containernet
CWD=$(pwd)

if [ -z "$INSTALL_DIR" ]; then
    INSTALL_DIR="$HOME/.containernet"
fi

git clone https://github.com/containernet/containernet.git $INSTALL_DIR/containernet
cd $INSTALL_DIR
sudo ansible-playbook -i "localhost," -c local containernet/ansible/install.yml
cd containernet
python3 -m venv venv
source venv/bin/activate
pip install .
cd $CWD

# Build Docker images

sudo make build

# Done

echo -e "\n \033[1;32m✔\033[0m Setup successful!"
echo -e "\n Run the following commands to start your network:"
echo -e " ──────────────────────────────────────────────────"
echo -e "\tsource ${INSTALL_DIR}/containernet/venv/bin/activate"
echo -e "\tsudo -E env PATH=\$PATH ./topo.py"
echo -e " ──────────────────────────────────────────────────\n"
