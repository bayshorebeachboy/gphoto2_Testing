import subprocess
import sys
sys.path.insert(0, '/Users/Neal/Documents/gphoto2_testing/id-delete-upload')
from id-delete-upload import *
sys.path.






subprocess.call(['python', '/Users/Neal/Documents/gphoto2_testing/delete-video.py'])
subprocess.call(['python', '/Users/Neal/Documents/gphoto2_testing/upload-video.py', '--file', '/Users/Neal/Dropbox/WeatherMovie/test.mp4', '--title', 'Bayshore Weather Timelapse'])