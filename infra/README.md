## Topology

![topology](https://i.imgur.com/hompm31.png)

## Installation

To install the necessary packages, run the following commands:

```bash
ubuntu@server:~/HTTP-2-Rapid-Reset-DDos/infra$ ./install.sh
```

To change the default installation directory, you can modify the `INSTALL_DIR` variable like so:

```bash
ubuntu@server:~/HTTP-2-Rapid-Reset-DDos/infra$ INSTALL_DIR=/custom/path ./install.sh
```

## Usage

To start the infrastructure, run the following commands:

```bash
ubuntu@server:~/HTTP-2-Rapid-Reset-DDos/infra$ source ~/.containernet/containernet/venv/bin/activate
(venv) ubuntu@server:~/HTTP-2-Rapid-Reset-DDos/infra$ sudo -E env PATH=$PATH ./topo.py
```

In another terminal, you can see the docker containers running and various statistics using:

```bash
ubuntu@server:~$ sudo ctop
```

To start the attack, execute the following command in the attacker container:

```bash
root@attacker:/# ./attacker -requests=10000  -url  https://modern.art/api  -wait=100  -delay=10 -concurrency=5
```

To stop the infrastructure, simply enter `exit` in the terminal where `topo.py` is running.
