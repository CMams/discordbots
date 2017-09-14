import praw
import config
import time
import os

def bot_login():
	print ("Logging into Reddit")
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "Vice's reddit bot")

	print ("Logged in!")
	return r

def run_bot(r, old_comment_list):
	###remove old scanned comments
	Tagwords = ['Legatum', 'legatum']

	for comment in r.subreddit('blackdesertonline').comments(limit=10):
		if Tagwords in comment.body and comment.id not in old_comment_list:
			print ("Comments of Keywords found")
			print(comment)
				
			old_comment_list.append(comment.id)

			with open('old_comment_list.txt', 'a') as f:
				f.write(comment.id + '\n')

			###sleep the script
			print ('Sleeping for 10 seconds...')
			time.sleep(10)

def get_saved_comments():
	if not os.path.isfile('old_comment_list.txt'):
		old_comment_list = []
	else:	
		with open("old_comment_list.txt", 'r') as f:
			old_comment_list = f.read()
			old_comment_list = old_comment_list.split("\n")

	return old_comment_list

r = bot_login()
old_comment_list = get_saved_comments()

while True:
	run_bot(r, old_comment_list)