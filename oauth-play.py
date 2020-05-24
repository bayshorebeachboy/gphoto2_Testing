import requests
import json
import httplib2

import googleapiclient
import flask
from googleapiclient.discovery import build
#from googleapiclient.errors import HttpError
#from googleapiclient.http import MediaFileUpload
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow
import google.oauth2.credentials
import google_auth_oauthlib.flow
#import googleapiclient.discovery

YOUTUBE_DELETE_SCOPE = "https://www.googleapis.com/auth/youtube"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

flow = flow_from_clientsecrets('/Users/Neal/Documents/gphoto2_testing/client_secrets.json', scope = 'https://www.googleapis.com/auth/youtube', redirect_uri='http://example.com/auth_return')
storage = Storage('/Users/Neal/Documents/gphoto2_testing/delete_video.py-oauth2.json')
credentials = storage.get()
if credentials is None:
    print('None')
elif credentials.invalid:
        print('Invalid')
else:
    print('Ok')
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,http=credentials.authorize(httplib2.Http()))
channels_response = youtube.channels().list(mine=True, part="contentDetails").execute()
for channel in channels_response["items"]:
    # From the API response, extract the playlist ID that identifies the list
    # of videos uploaded to the authenticated user's channel.
    uploads_list_id = channel["contentDetails"]["relatedPlaylists"]["uploads"]

    print "Videos on channel %s" % uploads_list_id

    # Retrieve the list of videos uploaded to the authenticated user's channel.
    playlistitems_list_request = youtube.playlistItems().list(
      playlistId=uploads_list_id,
    part="snippet",
    maxResults=50
  )

    while playlistitems_list_request:
        playlistitems_list_response = playlistitems_list_request.execute()

        # Print information about each video.
        for playlist_item in playlistitems_list_response["items"]:
            title = playlist_item["snippet"]["title"]
            video_id = playlist_item["snippet"]["resourceId"]["videoId"]
            #if title == 'Bayshore Weather Timelapse':
                #vid = video_id
                #print(video_id)
                #return(vid)
            print "%s (%s)" % (title, video_id)

        playlistitems_list_request = youtube.playlistItems().list_next(
        playlistitems_list_request, playlistitems_list_response)