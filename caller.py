import subprocess
print('Uploading...')
subprocess.call(['python', '/Users/Neal/Documents/gphoto2_testing/upload-video.py', '--file', '/Users/Neal/Dropbox/WeatherMovie/test.mp4', '--title', 'Bayshore Weather Timelapse'])
print('Done.')
#subprocess.call(['python', '/Users/Neal/Documents/gphoto2_testing/callee.py'])


title = 'Bayshore Weather Timelapse'