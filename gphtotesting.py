import gphoto2 as gp
import os
import subprocess
import sys
#gp.check_result(gp.use_python_logging())
camera = gp.check_result(gp.gp_camera_new())
gp.check_result(gp.gp_camera_init(camera))
print('Capturing image')
file_path = gp.check_result(gp.gp_camera_capture(camera, gp.GP_CAPTURE_IMAGE))
#file_path = '/Users/Neal/Documents/gphoto2_testing'
#print file_path
#print('Camera file path: {0}/{1}'.format(file_path.folder, file_path.name))
target = os.path.join('/tmp', file_path.name)
#target = '/Users/Neal/Documents/gphoto2_testing/test.jpg'
print('Copying image to', target)
#camera_file = gp.check_result(gp.gp_camera_file_get(camera, file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL))
camera_file = gp.check_result(gp.gp_camera_file_get(camera, file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL))
gp.check_result(gp.gp_file_save(camera_file, target))
subprocess.call(['xdg-open', target])
gp.check_result(gp.gp_camera_exit(camera))