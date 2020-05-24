# make_movie.py
import ffmpy
import os
import shutil
from subprocess import call


#from ffmpy import FFmpeg

#base_file = '/Users/Neal/Documents/gphoto2_testing/ForMovie'
#the_file = base_file + str(i) + '.jpg'
#the_file = '/Users/Neal/Documents/gphoto2_testing/ForMovie/movie.mp4'
the_file = 'movie.mp4'
if os.path.isfile(the_file):
    print('Deleting File')
    os.remove(the_file)
os.system('ffmpeg -f image2 -r 1 -s 3072x2304 -i /Users/Neal/Documents/gphoto2_testing/ForMovie/IMG_%03d.jpg -vcodec libx264 -crf 10 -pix_fmt yuv420p -y /Users/Neal/Documents/gphoto2_testing/TestMovies/test.mp4')

#ff = FFmpeg(
    #inputs={'/Users/Neal/Documents/gphoto2_testing/ForMovie/IMG_%03d.jpg ': None},
    #outputs={'-vcodec libx264 -crf 10 -pix_fmt yuv420p -y /Users/Neal/Documents/gphoto2_testing/TestMovies/test.mp4'}
#)
    
    
#ff = FFmpeg(
    #inputs={'/Users/Neal/Documents/gphoto2_testing/ForMovie/IMG_%04d.jpg': None},
    #outputs={'-vcodec mpeg4 -y /Users/Neal/Documents/gphoto2_testing/ForMovie/test.mp4'}
    ##outputs={'movie.mp4': None}
#)

#ff.cmd
#ff.run()

#delete files and otherwise cleanup

   