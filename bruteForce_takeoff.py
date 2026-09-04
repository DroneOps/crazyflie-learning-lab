"""
A test for a takeoff without position estimation, which the crazyflie requieres in order to fly
"""

import time

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie

URI = "radio://0/120/2M/E7E7E7E7E7"

cflib.crtp.init_drivers()

# Spoiler: this doesnt work, it may crash, the crazy needs a position estimator
with SyncCrazyflie(URI, cf=Crazyflie(rw_cache="./cache")) as scf:
    commander = scf.cf.commander
    print("Starting...")
    # 0 deg roll, 0 deg pitch, 0 deg/s yaw rate
    # thrust: between 10000 and 60000
    thrust_hover = 20001

    # The crazyflie continuosly requieres setpoints to fly
    for _ in range(30):
        commander.send_setpoint(0.0, 0.0, 0.0, thrust_hover)
        time.sleep(0.1)

    # land
    commander.send_setpoint(0.0, 0.0, 0.0, 0)
