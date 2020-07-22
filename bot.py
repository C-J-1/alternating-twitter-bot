import tweepy
import time

# Enter your credentials here
CONSUMER_KEY = "x"
CONSUMER_SECRET = "x"
ACCESS_TOKEN = "x"
ACCESS_TOKEN_SECRET = "x"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True, 
                 wait_on_rate_limit_notify=True)

def main():

    
    a=0 # this is just to keep track of the state of the system, odd or even.
    for tweet in tweepy.Cursor(api.search, "#dogs OR #cats").items(): #replace #cats and #dogs with your own terms, but keep the OR.
        try:
            if "#cats" in tweet.text:
                if (a % 2 == 0):
                    tweet.retweet() # retweet a #cats tweet if the state of the system is even.
                    a = a+1
                    time.sleep(300) # pause for 5 minutes
            if "#dogs" in tweet.text:
                if (a % 2 != 0):
                    print(tweet.text) # retweet a #dogs tweet if the state of the system is odd.
                    a = a+1
                    time.sleep(300) # pause for 5 minutes
        except tweepy.TweepError as e:
            print(e.reason) # gives error messages when a retweet doesn't work, e.g. when it's a duplicate.
        except StopIteration:
            break
        
main()
