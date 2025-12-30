#!/usr/bin/env python3

from mininet.net import Containernet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel

setLogLevel("info")

net = Containernet(controller=Controller, link=TCLink)
net.addController("c0")

attacker = net.addDocker(
    "attacker",
    ip="10.0.0.2",
    dimage="infra/attacker:latest",
    docker_args={
        "extra_hosts": ["modern.art:20.0.0.2"]
    }
)

frontend = net.addDocker(
    "frontend",
    ip="20.0.0.2",
    dimage="infra/frontend:latest",
    docker_args={
        "extra_hosts": ["api.modern.art:20.0.0.3"]
    }
)

backend = net.addDocker(
    "backend",
    ip="20.0.0.3",
    dimage="infra/backend:latest"
)

r0 = net.addHost("r0")

sw0 = net.addSwitch("sw0")
sw1 = net.addSwitch("sw1")

net.addLink(attacker, sw0)
net.addLink(sw0, r0, intfName2="r0-eth0", params2={"ip": "10.0.0.1/30"})

net.addLink(r0, sw1, intfName1="r0-eth1", params1={"ip": "20.0.0.1/29"})
net.addLink(frontend, sw1)
net.addLink(backend, sw1)

net.start()

r0.cmd("sysctl -w net.ipv4.ip_forward=1")
attacker.cmd("ip route add default via 10.0.0.1")
frontend.cmd("ip route add default via 20.0.0.1")
backend.cmd("ip route add default via 20.0.0.1")

frontend.cmd("nginx -g 'daemon off;'")
backend.cmd("uvicorn main:app --host 0.0.0.0 --port 5000")


CLI(net)
net.stop()