import threading

from PyP100 import PyL530
from controls import Controls
import config

ip = "192.168.0.166"
email = config.email
password = config.password


bulb = PyL530.L530(ip, email, password)
control_unit = Controls(bulb)


bulb.handshake()
bulb.login()

threading.Timer(.1, control_unit.listen).start()
control_unit.listen()
