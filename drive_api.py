from __future__ import print_function
import pprint
import six
import httplib2
from googleapiclient.discovery import build
import googleapiclient.http
import oauth2client.client

OAUTH2_SCOPE = 'path of google drive'
CLIENT_SECRETS = 'client_data.json'
FILENAME = 'document.txt'
MIMETYPE = 'text/plain'
TITLE = 'My New Text Document'
DESCRIPTION = 'Hello world.'
flow = oauth2client.client.flow_from_clientsecrets(CLIENT_SECRETS, OAUTH2_SCOPE)
flow.redirect_uri = oauth2client.client.OOB_CALLBACK_URN
authorize_url = flow.step1_get_authorize_url()
print('Following link in your browser: ' + authorize_url)
code = six.moves.input('Enter verify code: ').strip()
credentials = flow.step2_exchange(code)
http = httplib2.Http()
credentials.authorize(http)
drive_service = build('drive', 'v2', http=http)
media_body = googleapiclient.http.MediaFileUpload(
    FILENAME,
    mimetype=MIMETYPE,
    resumable=True
)
body = {
  'title': TITLE,
  'description': DESCRIPTION,
}
new_file = drive_service.files().insert(
  body=body, media_body=media_body).execute()
pprint.pprint(new_file)