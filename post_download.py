import praw
from psaw import PushshiftAPI

import pandas as pd
from datetime import datetime
from time import sleep

r = praw.Reddit(
    client_id = '',
    client_secret = '',
    username = '',
    password = '',
    user_agent = '')
api = PushshiftAPI(r)

start_time = int(datetime(2020, 1, 1).timestamp())
end_time = int(datetime(2020, 11, 11).timestamp())

def download(start, end, per_limit, order_by):
	count = 0
	df = pd.DataFrame()
	while True:
		if start:
			start = start
		try:
			submissions = list(api.search_submissions(
				after = start,
				before = end,
				subreddit = 'wallstreetbets',
				sort = order_by,
				limit = per_limit
			))
			start = int(submissions[-1].created_utc)
			for post in submissions:
				uid = post.id
				title = post.title
				selftext = post.selftext
				upvote = post.upvote_ratio
				score = post.score
				created = post.created_utc
				domain = post.domain
				if(post.author != 'AutoModerator'):
					df = df.append({
						'id': uid,
						'created':  datetime.fromtimestamp(created).strftime("%Y/%m/%d %H:%M:%S"),
						'title': title,
						'body': selftext,
						'domain': domain,
						'score': score,
						'upvote': upvote
					}, ignore_index=True)
					count += 1
		except:
			print('error 1')
			df.to_csv('%s.csv' %count, index = False)
			pass
		if len(submissions) == 0:
			break
		sleep(61)
	df.to_csv('df.csv', index = False)

download(start_time, end_time, 300, 'asc')
