from subprocess import PIPE, Popen
import os


def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]
os.chdir('/Users/Neal/go/src/github.com/porjo/youtubeuploader')
#print cmdline("cat /etc/services")
#print cmdline('ls')
#print cmdline('rpm -qa | grep "php"')
#print cmdline('nslookup google.com')
id = cmdline('./youtubeuploader -filename /Users/Neal/Documents/gphoto2_testing/TestMovies/test.mp4')
#print(id)