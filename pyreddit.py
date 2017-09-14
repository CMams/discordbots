import praw
import config

def run_bot(reddit):
	print ("Logging into Reddit")
	reddit = praw.Reddit(username = config.username,
						password = config.password,
						client_id = config.client_id,
						client_secret = config.client_secret,
						user_agent = "Vice's reddit bot")
			
print("Log In Success")

subreddit = reddit.subreddit('blackdesertonline')

legatum_reddit = subreddit.hot(limit = 5)

for submission in legatum_reddit:
		print(submission)

while True:
	run_bot()
