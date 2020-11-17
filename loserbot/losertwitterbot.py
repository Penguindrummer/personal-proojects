import tweepy

print("this is my dumb twitter bot!")

#have to have a twitter developers account
#insert your own keys here
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

#obtains last seen id
def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

#changes former id in the txt file
def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

last_seen_id = retrieve_last_seen_id(FILE_NAME)
mentions = api.mentions_timeline(
last_seen_id,tweet_mode = 'extended')


mentions = api.mentions_timeline()
for mention in mentions:
    print(str(mention.id) + "-" + mention.text)
    if '#hiyataaaaaaaaa' in mention.text.lower():
        print('found #hiyataaaaaaaaa')
        print('response in progress...')
