# Sample Python code for user authorization

import os

import google.oauth2.credentials

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
import urllib3
urllib3.disable_warnings()

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
# CLIENT_SECRETS_FILE = "/Users/Neal/Desktop/gdata-python-client-master/samples/apps/client_secrets.json"
CLIENT_SECRETS_FILE = "/Users/Neal/go/src/github.com/porjo/youtubeuploader/client_secrets.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

def get_authenticated_service():
    #flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_console()
    return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

def channels_list_by_username(service, **kwargs):
    results = service.channels().list(
      **kwargs
    ).execute()

    print('This channel\'s ID is %s. Its title is %s, and it has %s views.' %
        (results['items'][0]['id'],
        results['items'][0]['snippet']['title'],
        results['items'][0]['statistics']['viewCount']))

if __name__ == '__main__':
    ## When running locally, disable OAuthlib's HTTPs verification. When
    ## running in production *do not* leave this option enabled.
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    # https://accounts.google.com/o/oauth2/v2/auth?scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fyoutube.readonly&response_type=code&state=security_token%3D138r5719ru3e1%26url%3Dhttps://oauth2.example.com/token&redirect_uri=http://127.0.0.1:5005&client_id=810529243230-h4qsu0ijm3pag6ik3kss4r40t4trh4cm.apps.googleusercontent.com    
    service = get_authenticated_service()
    channels_list_by_username(service, part='snippet,contentDetails,statistics',
      forUsername='GoogleDevelopers')
