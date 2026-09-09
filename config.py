"""
Shared configuration for Crazyflie test scripts.
"""

from cflib.utils import uri_helper

# Crazyflie connection URI
# Format: radio://<radio_interface>/<radio_channel>/<radio_bandwidth>/<crazyflie_address>
#
# Parameters:
#   - radio_interface: 0 (typically the first Crazyradio dongle)
#   - radio_channel:   80 (radio channel)
#   - radio_bandwidth: 2M (datarate: 250K, 1M, or 2M)
#   - crazyflie_addr:  E7E7E7E7E7 (Crazyflie address)
#
# If the CRAZYFLIE_URI environment variable is set, it will be used instead.
URI = uri_helper.uri_from_env(default="radio://0/80/2M/E7E7E7E7E7")
