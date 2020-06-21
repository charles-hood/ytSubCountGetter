import urllib.request
import json
import os
import csv
from datetime import datetime

starttime = datetime.now()

start_time = starttime.strftime("%H:%M:%S")
print("Starting  at ", start_time)

key = "MUST PUT YOUR GOOGLE API HERE"

f = open('youtubelist.csv')
csv_f = csv.reader(f)

next(csv_f)

o = open('subs-output.csv', newline='', mode='w')
csv_o = csv.writer(o)

for row in csv_f:
  x = row[2]
  y = os.path.basename(x.rstrip("/"))

  if "user" in x:
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+y+"&key="+key).read()
    subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    s = "{:,d}".format(int(subs))
    z = y + " has " + s + " subscribers!"
    #print(z)
    csv_o.writerow([y,s])

  if "channel" in x:
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+y+"&key="+key).read()
    subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    s = "{:,d}".format(int(subs))
    z = y + " has " + s + " subscribers!"
    #print(z)
    csv_o.writerow([y,s])

o.close
f.close
endtime = datetime.now()

end_time = endtime.strftime("%H:%M:%S")
print("Finishing at ", end_time)


