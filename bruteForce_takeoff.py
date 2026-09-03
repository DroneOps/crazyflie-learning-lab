import time
import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie

URI = 'radio://0/120/2M/E7E7E7E7E7'

cflib.crtp.init_drivers()

with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:
    commander = scf.cf.commander
    print('__Empezando...') 
    # 0 deg roll, 0 deg pitch, 0 deg/s yaw rate
    # thrust: valor entero típicamente entre 10000 y 60000
    thrust_hover = 20001 
    
    # Enviar setpoints de forma continua 
    for _ in range(30):
        print(f'paso{_}')
        commander.send_setpoint(0.0, 0.0, 0.0, thrust_hover)
        time.sleep(0.1)

    # land
    commander.send_setpoint(0.0, 0.0, 0.0, 0)
