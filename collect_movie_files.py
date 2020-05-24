#collect_movie_files

import os
import subprocess
import os, os.path
import glob
import shutil
import logging
import sys

#from pathlib import Path 
#import gphoto2 as gp
#import re

path_to_movie = '/Users/Neal/Documents/gphoto2_testing/ForMovie'

base_file = '/Users/Neal/Documents/gphoto2_testing/ForMovie/IMG_00'
file_found = True
i = 1
while file_found:    
    the_file = base_file + str(i) + '.jpg'
    #used to create a bunch of files
    #open(the_file, 'a')
    if os.path.isfile(the_file):
        print('Found :', the_file)
        i += 1
    else:
        print('Creating 1 File')
        file_found = False
        #break loop and...
#create one from current image
scr = '/Users/Neal/Documents/gphoto2_testing/captured_image/webcam.jpg'
dst = '/Users/Neal/Documents/gphoto2_testing/ForMovie/IMG_00' + str(i) + '.jpg' 
shutil.copy(scr, dst)
        
        
