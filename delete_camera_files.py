#delete_camera_file.py

import os
import sys
import gphoto2 as gp

path_to_camera_files = '/store_00010001/DCIM/137CANON'
def delete_file(camera, path_to_camera_files):
    folder, name = os.path.split(path_to_camera_files)
    gp.check_result(gp.gp_camera_file_delete(camera, folder, name))


def main():
    delete_files()
    capture_image()
    print(glob.glob("./*.*"))
    file_to_rename = glob.glob("./*.*")
    fix_me = str(file_to_rename)
    fix_me = re.sub('[[/\]\'\"]', '', fix_me)
    fix_me = re.sub('.', '', fix_me, 1)
    #pass_me = '["mv" ' + ', "' + path_to_images + '/' + fix_me + '" , "' + path_to_images + '/' + 'webcam.jpg"]'
    #print pass_me
    os.rename(fix_me, 'webcam.jpg')
    #subprocess.call(pass_me)
    
if __name__ == "__main__":
    sys.exit(main())