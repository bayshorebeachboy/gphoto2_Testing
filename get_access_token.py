# get_access_token

import requests
#import googleapiclient.discovery
#from oauth2client.client import GoogleCredentials
##import gdata.youtube
##import gdata.youtube.service
#from gdata import youtube
#from oauth2client.client import flow_from_clientsecrets




#url = 'https://accounts.google.com/o/oauth2/token?'
url = 'https://www.googleapis.com/oauth2/v4/token'



# args = 'client_id=' + client_id + '&client_secret=' + client_secret + '&redirect_uri=http://www.google.com&' + '&refresh_token=' + refresh_token + 'scope=https://www.googleapis.com/auth/youtube.force-ssl&' + '&grant_type=refresh_token'

args = {'client_id': '810529243230-7kgba59s05qi9b8fsqq6fcn1veo002oh.apps.googleusercontent.com', 'client_secret': 'rkUt1KbZFnenAnhqJED3XPPx', 'refresh_token': '1/JYFYamTRdniLjniRCiiqBkz3w_JGz5H60QQVXu3vKW79ueBBFgJ6Z68EepqpwKqt', 'grant_type': 'refresh_token'}
print(args)


get_token = requests.post(url, data = args)

result = get_token.json() #['access_token'] 

print(result)



# this may be a way to use an access token
# GET access_token=ya29.GlxBBS89....part=snippet&mine=true
# doesen't seem to work - <responce [400]> (bad request)
#url = 'https://www.googleapis.com/youtube/v3/channels'
#args = 'access_token: ' + result + ', part: snippet, mine: true'
#get_token = requests.get(url, data = args)



#credentials =  get_token.json() #['access_token']
#print(credentials)

# this also dosen't work 
#credentials = GoogleCredentials.get_application_default()


#flow = flow_from_clientsecrets('/Users/Neal/Documents/gphoto2_testing/client_secrets.json',
                               #scope='https://www.googleapis.com/auth/calendar',
                               #redirect_uri='http://example.com/auth_return')

#YOUTUBE_DELETE_SCOPE = "https://www.googleapis.com/auth/youtube"
#YOUTUBE_API_SERVICE_NAME = "youtube"
#YOUTUBE_API_VERSION = "v3"

## youtube.videos is not part of this api
## resp = youtube.videos().delete('LVlqBR4otdU', onBehalfOfContentOwner=None).execute()
## this may be a way to use an access token
## GET access_token=ya29.GlxBBS89x1SQ89cxesu124YvJsmCGWjtZU0dwxahWm-rciGFoipsfAOTJjEoUrEBX3cPqEMpbX5z5_Vvh55s-kaK8g_-GlE3-wiBBGSSNtHs8zC4y2F5LGKUExUjZA&part=snippet&mine=true
## from youtube DataAPI Samples
#client = googleapiclient.discovery.build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, credentials=None)
