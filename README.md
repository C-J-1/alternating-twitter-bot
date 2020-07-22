# alternating-twitter-bot
A simple python script allowing a twitter bot to search for two separate terms in the public tweet stream, and retweet the results in an alternating pattern.

This is not intended to teach you how to set up your twitter bot with developers.twitter.com. 

Once you have your API keys and access tokens, copy-paste them into the script where indicated.

You can change the rate at which you retweet by editing the lines with "time.sleep(300)". 300 means 300 seconds.

You can change the search terms by replaceing any instance of "#cats", or "#dogs", & "#cats OR #dogs" with some other search terms.

If you can be bothered, you can introduce more search terms by following the format "#dogs OR #cats OR #horses OR ...", but if you decide to do this, you will need to change the rest of the code. 

Currently if the variable "a" is even it will retweet a popular post that contains "#cats". If it is odd, it will retweet a popular tweet that contains "#dogs". so adding more search terms will involve implementing some other system that has as many states as the search has search terms.

I should have thought about a more elegant way to alternate between the search terms, but this is what you get. It was just a quick solution to alternate between the two search terms without the need to search for 1, tweet it, search for the other, tweet it, search for the first one again... etc. It's all under the same search stream thing, so you won't be making unnecessary duplicate search requests and annoy the twitter overlords.

