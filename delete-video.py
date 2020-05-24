#!/usr/bin/python

import httplib
import httplib2
import os
import random
import sys
import time

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow


# Explicitly tell the underlying HTTP transport library not to retry, since
# we are handling retry logic ourselves.
httplib2.RETRIES = 1

# Maximum number of times to retry before giving up.
MAX_RETRIES = 10

# Always retry when these exceptions are raised.
RETRIABLE_EXCEPTIONS = (httplib2.HttpLib2Error, IOError, httplib.NotConnected,
                        httplib.IncompleteRead, httplib.ImproperConnectionState,
  httplib.CannotSendRequest, httplib.CannotSendHeader,
  httplib.ResponseNotReady, httplib.BadStatusLine)

# Always retry when an apiclient.errors.HttpError with one of these status
# codes is raised.
RETRIABLE_STATUS_CODES = [500, 502, 503, 504]

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret. You can acquire an OAuth 2.0 client ID and client secret from
# the Google Developers Console at
# https://console.developers.google.com/.
# Please ensure that you have enabled the YouTube Data API for your project.
# For more information about using OAuth2 to access the YouTube Data API, see:
#   https://developers.google.com/youtube/v3/guides/authentication
# For more information about the client_secrets.json file format, see:
#   https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
CLIENT_SECRETS_FILE = "/Users/Neal/Documents/gphoto2_testing/client_secrets.json"

# This OAuth 2.0 access scope allows an application to upload files to the
# authenticated user's YouTube channel, but doesn't allow other types of access.
YOUTUBE_DELETE_SCOPE = "https://www.googleapis.com/auth/youtube"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# This variable defines a message to display if the CLIENT_SECRETS_FILE is
# missing.
MISSING_CLIENT_SECRETS_MESSAGE = """
WARNING: Please configure OAuth 2.0

To make this sample run you will need to populate the client_secrets.json file
found at:

   %s

with information from the Developers Console
https://console.developers.google.com/

For more information about the client_secrets.json file format, please visit:
https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
""" % os.path.abspath(os.path.join(os.path.dirname(__file__),
                                   CLIENT_SECRETS_FILE))

VALID_PRIVACY_STATUSES = ("public", "private", "unlisted")


def get_authenticated_service(args):
    flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
                                 scope=YOUTUBE_DELETE_SCOPE,
    message=MISSING_CLIENT_SECRETS_MESSAGE)

    storage = Storage("%s-oauth2.json" % sys.argv[0])
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        credentials = run_flow(flow, storage, args)

    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
               http=credentials.authorize(httplib2.Http()))
########################################################
def get_video_id():
    YOUTUBE_READONLY_SCOPE = "https://www.googleapis.com/auth/youtube"
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    
    flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
                                   message=MISSING_CLIENT_SECRETS_MESSAGE,
                                   scope=YOUTUBE_READONLY_SCOPE)
    
    storage = Storage("%s-oauth2.json" % sys.argv[0])
    credentials = storage.get()
    
    if credentials is None or credentials.invalid:
        flags = argparser.parse_args()
        credentials = run_flow(flow, storage, flags)
    
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    http=credentials.authorize(httplib2.Http()))
    
    # Retrieve the contentDetails part of the channel resource for the
    # authenticated user's channel.    
    channels_response = youtube.channels().list(
        mine=True,
      part="contentDetails"
    ).execute()
    
    for channel in channels_response["items"]:
        # From the API response, extract the playlist ID that identifies the list
        # of videos uploaded to the authenticated user's channel.
        uploads_list_id = channel["contentDetails"]["relatedPlaylists"]["uploads"]
    
        #print "Videos in list %s" % uploads_list_id
    
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
                if title == 'Bayshore Weather Timelapse':
                    vid = video_id
                    print(video_id)
                    return(vid)
                #print "%s (%s)" % (title, video_id)
    
            playlistitems_list_request = youtube.playlistItems().list_next(
            playlistitems_list_request, playlistitems_list_response)
        #######################################################


if __name__ == '__main__':
    #argparser.add_argument("--id", required=True, help="Video youtube ID")  
    #args = argparser.parse_args()

    #if not args.id:
        #exit("Please specify a youtube ID using the --id= parameter.")
    ############################################################
    #get_video_id()
    args = get_video_id()
    ############################################################
    if args is not None: 
    ############################################################
        youtube = get_authenticated_service(args)
        
        try:
            #resp = youtube.videos().delete(id=args.id, onBehalfOfContentOwner=None).execute()
            resp = youtube.videos().delete(id=args, onBehalfOfContentOwner=None).execute()
    
        except HttpError, e:
            print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)