## Topology

![topology](https://i.imgur.com/hompm31.png)

## Installation

To install the necessary packages, run the following commands:

```bash
./install.sh
```

To change the default installation directory, you can modify the `INSTALL_DIR` variable like so:

```bash
INSTALL_DIR=/custom/path ./install.sh
```

## Usage

To start the infrastructure, run the following commands:

```bash
source ~/.containernet/containernet/venv/bin/activate
sudo -E env PATH=$PATH ./topo.py
```

To start the attack, execute the following command in the attacker container:

```bash
./attacker -url='https://modern.art:443/api' -requests=500000
```

After a few moments, when you try to access the website using `curl`, it becomes unresponsive.

```
root@attacker:/attacker# curl -k https://modern.art/
curl: (28) SSL connection timeout
```

To stop the infrastructure, simply enter `exit` in the terminal where `topo.py` is running.
