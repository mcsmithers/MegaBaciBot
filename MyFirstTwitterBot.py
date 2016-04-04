import tweepy, time, sys

argfile = str(sys.argv[1])

#setting up access to my twitter 
CONSUMER_KEY = 'THEKEY'
CONSUMER_SECRET = 'THESECRETKEY'
ACCESS_TOKEN = 'THEACCESSTOKEN'
ACCESS_TOKEN_SECRET= 'THESECRETACCESSTOKEN'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#getting the tweet sources
filename = open(argfile,'r')
#reading the file
f = filename.readlines()
filename.close()

for line in f:
	api.update_status(line)
	print ("Tweeting...")
	time.sleep(86400) #tweets once a day and sleeps the rest


