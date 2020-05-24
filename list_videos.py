import urllib, json
author = 'nealm040@gmail.com'

#import urllib, json
#author = 'Youtube_Username'
inp = urllib.urlopen(r'http://gdata.youtube.com/feeds/api/videos?max-results=50&alt=json&orderby=published&author=' + author)
resp = json.load(inp)
inp.close()
first = resp['feed']['entry'][0]
print first['title'] # video title
print first['link'][0]['href'] #url
#foundAll = False
#ind = 1
#videos = []
#while not foundAll:
    #inp = urllib.urlopen(r'http://gdata.youtube.com/feeds/api/videos?start-index={0}&max-results=4&alt=json&orderby=published&author={1}'.format( ind, author ) )
    #try:
        #resp = json.load(inp)
        #inp.close()
        #returnedVideos = resp['feed']['entry']
        #for video in returnedVideos:
            #videos.append( video ) 

        #ind += 1
        #print len( videos )
        #if ( len( returnedVideos ) < 2 ):
            #foundAll = True
    #except:
        ##catch the case where the number of videos in the channel is a multiple of 50
        #print "error"
        #foundAll = True

#for video in videos:
    #print video['title'] # video title
    #print video['link'][0]['href'] #url