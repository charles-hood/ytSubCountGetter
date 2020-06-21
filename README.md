# ytSubCountGetter
Quick and dirty Python script to get YouTube channel urls from a Google Sheet and lookup the subscriber count using the YouTube API

This program started out based on https://github.com/howCodeORG/Python-Sub-Count then glommed together with the examples from the Google API docs. (THANK YOU howCodeORG for sharing your code and getting me jump started.)

Notes:
You *must* have a Google API key to make this work. Modify key= with your API key.
Enable both the Google Sheets API and the YouTube API on the Google Developer site.
You must also have the unique identifier of your Google Sheet as input.
(modify SAMPLE_SPREADSHEET_ID with your Google Sheet ID)
(modify SAMPLE_RANGE_NAME with your input range from your Google Sheet)

No comments, no docs, no error checking -- when I say quick and dirty, I'm not kidding.
This program works perfectly *for me* -- I make no guarrantees.

Reference:
https://developers.google.com/sheets/api/quickstart/python

Reference:
https://developers.google.com/youtube/v3/docs/channels/list

Special case of input URL being a Custom URL for the YouTube Channel handled using Requests HTTP library
Reference:
https://requests.readthedocs.io/en/master/

Special shout-out to the #python-general channel on Discord for all the assistance! THANK YOU!
Reference:  https://discord.gg/python

