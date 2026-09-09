"""
Simple script for connecting to the Crazyflie, verifying connection,
and briefly spinning the motors to provide physical feedback.
"""

import time

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from config import URI


def simple_connect(scf):
    """
    Test connection to the Crazyflie and briefly spin motors at low thrust.
    """
    print("Connected to Crazyflie successfully.")
    print("Spinning motors briefly for physical feedback...")

    commander = scf.cf.commander

    # Spin motors at a low thrust value (well below liftoff threshold)
    # to physically verify motor response
    low_thrust = 15000
    for _ in range(5):
        commander.send_setpoint(0.0, 0.0, 0.0, low_thrust)
        time.sleep(0.1)

    # Stop motors
    commander.send_setpoint(0.0, 0.0, 0.0, 0)
    time.sleep(1)
    print("Disconnecting from Crazyflie.")


if __name__ == "__main__":
    # Initialize the low-level drivers
    cflib.crtp.init_drivers()

    print(f"Connecting to {URI}...")
    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache="./cache")) as scf:
        simple_connect(scf)
