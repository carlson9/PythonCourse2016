#############################################
##################### HOMEWORK 3 #############
##############################################

import time
import tweepy
import csv 


auth = tweepy.OAuthHandler('your consumer key', '')
auth.set_access_token('your consumer secret', '')    
api = tweepy.API(auth)


# check rate limit
api.rate_limit_status()


def TreatErrors(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.TweepError:
            time.sleep(20 * 60)

			
def Find_Tweets(User_List):
	User_Tweets = {}
	for user in User_List:
		username = str(user)
		while True:
			try:
				new_user = api.get_user(username)
				User_Tweets[username] =  new_user.statuses_count
				break
			except tweepy.TweepError:
				time.sleep(20 * 60)
	return User_Tweets

def Find_Followers(User_List):
	User_Followers = {}
	for user in User_List:
		username = str(user)
		while True:
			try:
				new_user = api.get_user(username)
				User_Followers[username] = new_user.followers_count
				break
			except tweepy.TweepError:
				time.sleep(20 * 60)
	return User_Followers 

			
# find a user (Belarusian opposition leader)
target = api.get_user('lahviniec') #=UM

# status count
target_tweets = target.statuses_count #UMTweets

# followers
target_followers = [] #UMFriends
for user in TreatErrors(tweepy.Cursor(api.followers,'lahviniec').items()):
    target_followers.append(user.screen_name)

	   
#### Section 1: 1st degree of separation
def find_max(Dictionary):
	top_user = max(Dictionary, key=Dictionary.get)
	top_value = Dictionary[top_user]
	print '%s: %s' % (top_user, top_value)

# find most active follower
most_active_follower = Find_Tweets(target_followers)
find_max(most_active_follower)

# find most popular/followed follower
most_popular_follower = Find_Followers(target_followers)
find_max(most_popular_follower)

# find most active type of follower (layman, expert or celebrity)
type_follower = Find_Tweets(target_followers)
Layman = {}
Expert = {}
Celebrity = {}

for follower in type_follower:
	if type_follower[follower] < 100:
		Layman[follower] = type_follower[follower]
	if type_follower[follower] > 1000:
		Celebrity = type_follower[follower]
	else:
		Expert[follower] = type_follower[follower]

find_max(Layman)
find_max(Expert)
find_max(Celebrity)

# find most popular friend of the follower?
follower_friends = Find_Followers(target_followers)
find_max(follower_friends)

##### Section 2: 2nd degree of separation
# get rid of the celebrities
new_followers = Layman.copy() # Not_Celebs_Foll
new_followers.update(Expert)
new_followers = new_followers.keys()

# among the FOLLOWERS of your target and their followers, 
# who is the most active? 
def find_followers_of_followers (follower_list):
  	all_followers = []
  	for follower in follower_list:
  		user_followers = []
  		for user in TreatErrors(tweepy.Cursor(api.followers,follower).items()):
			print user.screen_name
  			user_followers.append(user.screen_name)
  		all_followers.append(user_followers)
  	return all_followers


followerfollowers = find_followers_of_followers(new_followers)
most_active_ff_tweets = {}
	for i in followerfollowers:
	followerfollowers_tweets.update(Find_Tweets(i))

find_max(followerfollowers_tweets)


# among the FRIENDS of your target and their friends, 
# who is the most active?

def find_friends_of_followers (friend_list)
	all_friends = []
 	for friend in friend_list:
 		follower_friends = []
 		for user in TreatErrors(tweepy.Cursor(api.friends, friend).items()):
 			print user.screen_name
 			follower_friends.append(user.screen_name)
 		all_friends.append(follower_friends)
 	return all_friends

followerfriends =  find_friends_of_followers (target_followers)
followerfriends_tweets = {}
	for i in followerfriends:
 	followerfriends_tweets.update(Find_Tweets(i))
 
 find_max(followerfriends_tweets)


@@ -94,15 +122,33 @@ def Find_Followers(User_List):
  				time.sleep(20 * 60)
  	return user_followers

