import requests
import csv
import datetime

# GroupMe Bot ID
botID = 'a43130d9c99882a6c98e28824c'  # insert your Bot ID here

# List of names with a birthday on the current date
birthdayBoys = []

# Current Date
datetimeObject = datetime.datetime.now()
currentDate = str(datetimeObject.month) + "/" + str(datetimeObject.day)
# currentDate = '12/30' # used for testing (best birthday)

# Turn birthday-list.csv into a dictionary and create a list of birthday bois
with open('birthday-list.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        if row['Birthday'] == currentDate:
            birthdayBoys += {row['Full Name']}

# get last names of the birthday bois
lastNames = []
if len(birthdayBoys) == 1:
    split = birthdayBoys[0].split(' ')
    lastNames += split[-1:]
elif len(birthdayBoys) > 1:
    for boi in birthdayBoys:
        split = boi.split(' ')
        lastNames += split[-1:]

# construct message text
postText = ''
if len(lastNames) == 1:
    postText = '🎉 Happy Birthday to ' + lastNames[0]
elif len(lastNames) > 1:
    for i, name in enumerate(lastNames):
        if i != (len(lastNames) - 1):
            postText += '🎉 Happy Birthday to ' + name + '\n\n'
        else:
            postText += '🎉 Happy Birthday to ' + name

# construct and send the post
postData = {'bot_id': botID,
            'text': postText}

r = requests.post('https://api.groupme.com/v3/bots/post', data=postData)
