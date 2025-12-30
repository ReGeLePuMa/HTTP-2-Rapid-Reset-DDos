#!/usr/bin/env python3

from mininet.net import Containernet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel, info

setLogLevel("info")

config_map = {
    "attacker_config": {
        "name": "attacker",
        "image": "infra/attacker:latest",
        "ip": "10.0.0.3"
    },
    "frontend_config": {
        "name": "frontend",
        "image": "infra/frontend:latest",
        "ip": "20.0.0.3",
        "hostname": "modern.art"
    },
    "backend_config": {
        "name": "backend",
        "image": "infra/backend:latest",
        "ip": "20.0.0.4",
        "hostname": "api.modern.art"
    }
}

net = Containernet(controller=Controller, link=TCLink)
net.addController("c0")

backend = net.addDocker(
    config_map["backend_config"]["name"],
    ip=config_map["backend_config"]["ip"],
    dimage=config_map["backend_config"]["image"]
)

frontend = net.addDocker(
    config_map["frontend_config"]["name"],
    ip=config_map["frontend_config"]["ip"],
    dimage=config_map["frontend_config"]["image"]
)

attacker = net.addDocker(
    config_map["attacker_config"]["name"],
    ip=config_map["attacker_config"]["ip"],
    dimage=config_map["attacker_config"]["image"]
)

r0 = net.addHost("r0", ip="10.0.0.2")

sw0 = net.addSwitch("sw0")
sw1 = net.addSwitch("sw1")

net.addLink(attacker, sw0)
net.addLink(sw0, r0, intfName2="r0-eth0")

net.addLink(r0, sw1, intfName1="r0-eth1", params1={"ip": "20.0.0.2/29"})
net.addLink(frontend, sw1)
net.addLink(backend, sw1)

net.start()

info("Configuring routing...\n")
r0.cmd("sysctl -w net.ipv4.ip_forward=1")
attacker.cmd("ip route add 20.0.0.0/29 via 10.0.0.2")
frontend.cmd("ip route add 10.0.0.0/29 via 20.0.0.2")
backend.cmd("ip route add 10.0.0.0/29 via 20.0.0.2")

info("Adding DNS entries...\n")
frontend_ip = config_map["frontend_config"]["ip"]
frontend_host = config_map["frontend_config"]["hostname"]

backend_ip = config_map["backend_config"]["ip"]
backend_host = config_map["backend_config"]["hostname"]

attacker.cmd(f'echo "{frontend_ip} {frontend_host}" >> /etc/hosts')
frontend.cmd(f'echo "{backend_ip} {backend_host}" >> /etc/hosts')

info("Starting services...\n")
backend.cmd("gunicorn main:app -k uvicorn.workers.UvicornWorker -b 0.0.0.0:5000 -D")
frontend.cmd("nginx -g 'daemon on;'")

info("Running CLI...\n")
CLI(net)

info("Stopping network...\n")
net.stop()
