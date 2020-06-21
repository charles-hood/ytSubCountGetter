import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import urllib.request
import json
import os
import csv
import re
import requests
from datetime import datetime

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = 'YOUR UNIQUE GOOGLE SHEET ID'
SAMPLE_RANGE_NAME = 'Sheet1!C2:C250'

starttime = datetime.now()

start_time = starttime.strftime("%H:%M:%S")
print("Starting  at ", start_time)

key = "YOUR UNIQUE GOOGLE API KEY"

o = open('subs-output.csv', newline='', mode='w')
csv_o = csv.writer(o)

creds = None
# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)
service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range=SAMPLE_RANGE_NAME).execute()
values = result.get('values', [])

for row in values:
  x = row[0]
  y = os.path.basename(x.rstrip("/"))

  if "/c/" in x:
    response = requests.get(x)
    regex = re.compile(r'"og:url" content="(https://www.youtube.com/channel/\w+)"')
    d = regex.search(response.text).group(1)
    print(d)
    y = os.path.basename(d.rstrip("/"))
    print(y)
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+y+"&key="+key).read()
    subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    s = "{:,d}".format(int(subs))
    z = y + " has " + s + " subscribers!"
    print(z)
    csv_o.writerow([y,s])

  if "user" in x:
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+y+"&key="+key).read()
    subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    s = "{:,d}".format(int(subs))
    z = y + " has " + s + " subscribers!"
    print(z)
    csv_o.writerow([y,s])

  if "channel" in x:
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+y+"&key="+key).read()
    subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    s = "{:,d}".format(int(subs))
    z = y + " has " + s + " subscribers!"
    print(z)
    csv_o.writerow([y,s])

o.close
endtime = datetime.now()

end_time = endtime.strftime("%H:%M:%S")
print("Finishing at ", end_time)


