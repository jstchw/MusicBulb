import threading

from PyP100 import PyP100
from controls import Controls
import config

ip = "192.168.0.166"
email = config.email
password = config.password

p100 = PyP100.P100(ip, email, password)
control_unit = Controls(p100)


p100.handshake()
p100.login()

threading.Timer(.1, control_unit.listen).start()
control_unit.listen()
