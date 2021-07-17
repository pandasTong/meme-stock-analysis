*****
	Meme Stocks Analysis
*****
Reddit
#######

This small project will look into the birth place of meme stock, Subreddit `r/wallstreetbets <https://www.reddit.com/r/wallstreetbets/>`_ . The concept behind meme stock is so pure which overthrew the fundamentals wall street built on value investing and growth investingcan. The conecpt can be explained by one simple economic model **Supply and Demand**.


**Insights to obtain:**

	+ When did it actually start
	+ What are people's sentiment on stocks
	+ How much are people's sentiment related to stock's price
	+ Is chasing the rally a good move

Getting Started
####### 

**Crawl:**

Set up 

.. code-block:: python

	import praw
	from psaw import PushshiftAPI

	reddit = praw.Reddit(
		client_id = '',
		client_secret = '',
		username = '',  # optional
		password = '',  # optional
		user_agent = '')
	api = PushshiftAPI(r)

Search Posts
	title
	score
	upvote
	body domain

Credibility
#######

**Participation:**

**Sentiment**

Correlation
#######




