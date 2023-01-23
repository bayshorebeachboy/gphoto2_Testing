# clear captured gphoto image
import os
import subprocess
import os, os.path
import glob
import shutil
import logging
import sys
import gphoto2 as gp
import re
import datetime
from datetime import datetime
import ephem  
o=ephem.Observer()  
o.lat='45'  
o.long='-124'  
s=ephem.Sun()  
s.compute()  


path_to_images = '/Users/Neal/Documents/gphoto2_testing/captured_image'
path_for_movie = '/Users/Neal/Documents/gphoto2_testing/ForMovie'
####################
#fix base_file
####################
base_file = '/Users/Neal/Documents/gphoto2_testing/ForMovie/IMG_'

# used to alert lost camera etc.
#import smtplib

# Use sms gateway provided by mobile carrier:
# at&t:     number@mms.att.net
# t-mobile: number@tmomail.net
# verizon:  number@vtext.com
# sprint:   number@page.nextel.com

# Establish a secure session with gmail's outgoing SMTP server using your gmail account
#server = smtplib.SMTP( "smtp.gmail.com", 587 )

#server.starttls()

#server.login( 'nealm040@gmail.com', 'DuneGirl$4' )



camera_list = []
for name, addr in gp.check_result(gp.gp_camera_autodetect()):
    camera_list.append((name, addr))
if not camera_list:
    #print('No camera detected')delete_files()
    theMsg = 'No camera detected'
    #print('The message is :', theMsg)
    #server.sendmail( 'gphoto2', '5418706584@mms.att.net', 'A620 Camera is not connected')    
    
    
 
camera_list.sort(key=lambda x: x[0])
# ask user to choose one
#for index, (name, addr) in enumerate(camera_list):
    #print('{:d}:  {:s}  {:s}'.format(index, addr, name))
    #if name == 'Canon PowerShot A620 (PTP mode)':
        #print(addr)
        #set_camera(addr)  

camera = gp.Camera()
port_info_list = gp.PortInfoList()
port_info_list.load()
idx = port_info_list.lookup_path(addr)
#print('idx='+str(idx))
#idx = 2
camera.set_port_info(port_info_list[idx])
gp.check_result(gp.gp_camera_init(camera))

def delete_files(): # Delete Files from server
    os.chdir(path_to_images)
    #print(os.curdir)
    subprocess.call('rm -r ./*', shell=True)
    print('Existing image files deleted...')
    return 0 
    
def main():
    # defer delete till confirmed image will be created i.e. "It is Day..."
    # delete_files()
    #capture_image()    
    logging.basicConfig(format='%(levelname)s: %(name)s: %(message)s', level=logging.WARNING)
    gp.check_result(gp.use_python_logging())
    ############################################

    # make a list of all available cameras
    camera_list = []
    # end set camera
    ############################################
  
    sunrise = ephem.localtime(o.next_rising(s))
    sunset = ephem.localtime(o.next_setting(s))
    if sunset < sunrise: # Sunset is Less Than Sunrise
        print('Day')
        # delete_files() funtion cd's to gphoto2_testing
        # may refactor to use full path rather than cd to the dir.
        delete_files() #delete files from server
        print('Capturing image')
        file_path = gp.check_result(gp.gp_camera_capture(camera, gp.GP_CAPTURE_IMAGE))
        # print('Camera file path: {0}/{1}'.format(file_path.folder, file_path.name))
        target = os.path.join(path_to_images, file_path.name)
        print('Copying image to', target)
        camera_file = gp.check_result(gp.gp_camera_file_get(camera, file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL))
        gp.check_result(gp.gp_file_save(camera_file, target))
        #cl = gp.check_result(gp.gp_camera_folder_list_files(camera, "/store_00010001/DCIM/100CANON"))
        #e = 1
        #for name in cl:
            #print(name[e])
        # gp.check_result(gp.gp_camera_file_delete(camera, "/store_00010001/DCIM/100CANON", "IMG_0002.JPG"))
        # delete files from camera
        gp.check_result(gp.gp_camera_folder_delete_all(camera, "/store_00010001/DCIM/100CANON"))
        #cl = gp.check_result(gp.gp_camera_folder_list_files(camera, "/store_00010001/DCIM/100CANON"))
        #e = 1
        #for name in cl:
            #print(name[e])        
        gp.check_result(gp.gp_camera_exit(camera))
        # gp.check_result(gp.gp_camera_file_delete
        #end capture image 
        
        ##############################
        # format camera file name and re-name as webcam.jpg
        # currently assumes only one file in folder
        print(glob.glob("./*.*"))
        file_to_rename = glob.glob("./*.*")
        fix_me = str(file_to_rename)
        fix_me = re.sub('[[/\]\'\"]', '', fix_me)
        fix_me = re.sub('.', '', fix_me, 1)
        os.rename(fix_me, 'webcam.jpg')
        print("Re-name to webcam.jpg")
        
    else: print('Night')
if __name__ == "__main__":
    sys.exit(main())


