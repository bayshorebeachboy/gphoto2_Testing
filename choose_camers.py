
from __future__ import print_function

import logging
import six
import sys
import os
import gphoto2 as gp

path_to_images = '/Users/Neal/Documents/gphoto2_testing/captured_image'
path_for_movie = '/Users/Neal/Documents/gphoto2_testing/ForMovie'


def set_camera(addr):
    camera = gp.Camera()
    port_info_list = gp.PortInfoList()
    port_info_list.load()
    idx = port_info_list.lookup_path(addr)
    print('idx='+str(idx))
    #idx = 2
    camera.set_port_info(port_info_list[idx])


#def main(addr):
# make a list of all available cameras
camera_list = []
for name, addr in gp.check_result(gp.gp_camera_autodetect()):
    camera_list.append((name, addr))
if not camera_list:
    print('No camera detected')
 
camera_list.sort(key=lambda x: x[0])
# ask user to choose one
for index, (name, addr) in enumerate(camera_list):
    print('{:d}:  {:s}  {:s}'.format(index, addr, name))
    if name == 'Canon PowerShot A620 (PTP mode)':
        print(addr)
        set_camera(addr)
