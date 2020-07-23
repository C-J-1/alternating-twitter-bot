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

    a=0
    for tweet in tweepy.Cursor(api.search, '-filter:retweets AND -filter:replies "#cats" OR "#dogs"', result_type="recent", lang="en").items():
        try:
            if "#cats" in tweet.text:
                if (a % 2 == 0):
                    print(tweet.text)
                    tweet.retweet()
                    a = a+1
                    time.sleep(61)
            if "#dogs" in tweet.text:
                if (a % 2 != 0):
                    print(tweet.text)
                    tweet.retweet()
                    a = a+1
                    time.sleep(60)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
        
main()
