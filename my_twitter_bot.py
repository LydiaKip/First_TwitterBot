import tweepy
import time
# NOTE: I put my keys in the keys.py to separate them
# from this main file.
# Please refer to keys_format.py to see the format.
from keys import *

# NOTE: flush=True is just for running this script
# with PythonAnywhere's always-on task.

print('This is my Twitter bot!', flush=True)

CONSUMER_KEY='cjolHdsyJ5G5ILOUPL8Ioxzf3'
CONSUMER_SECRET='pE8jcl26oPdFT2WfFRN8vVkl9MWOrpan2341CX4AHn21Conkiv'
ACCESS_KEY='1334011257058435072-FkZ2hjj9K9QpwdGMz6gcBZKXE8g9es'
ACCESS_SECRET='yTUCfRADFg6eba4niJMzHU6fgopKbZdHLmgGYmCrMm90V'

#Three comands below

auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api=tweepy.API(auth)



FILE_NAME = 'last_seen_id.txt'

#the function below takes the last last_seen_id and
#saves it in the last_seen_id.txt file
#rem id is an int

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

#the function below  does the same by replacing
#the last seen id with a new one

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
        # NOTE: We need to use tweet_mode='extended' below to show
        # all full tweets (with full_text). Without it, long tweets
        # would be cut off.
        # Also we the arg last_seen_id is for us to exclude
        # the previous id we had in our file and start from the recent ones.

    mentions = api.mentions_timeline(
                            last_seen_id,
                            tweet_mode='extended')


    for mention in reversed(mentions):
    # We reversse the list to start from the oldest tweet to the newest ones.
    # tweet1 first then 2,3,4..
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#hellosmiley' in mention.full_text.lower():
            print('found #hellosmiley!', flush=True)
            print('responding back...', flush=True)
            api.update_status('@' + mention.user.screen_name +
                    '#Hello Smiley back to you!', mention.id)

while True:
    reply_to_tweets()
    time.sleep(2)#starts process after every 15sec.
