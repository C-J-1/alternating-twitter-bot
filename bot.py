import tweepy
import time

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

    a=2
    for tweet in tweepy.Cursor(api.search, "#dogs OR #cats").items():
        try:
            if "#cats" in tweet.text:
                if (a % 2 == 0):
                    print(tweet.text)
                    a = a+1
                    time.sleep(300)
            if "#dogs" in tweet.text:
                if (a % 2 != 0):
                    print(tweet.text)
                    a = a+1
                    time.sleep(300)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
        
main()
