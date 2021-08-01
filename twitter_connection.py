from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import json

consumer_key='CONSUMER_KEY'
consumer_secret='CONSUMER_SECRET'
access_token ='ACCESS_TOKEN'
access_secret='ACCESS_SECRET'

csv = open('OutputStreaming.csv','a')

class TweetsListener(StreamListener):
    def __init__(self):
        self.num_tweets = 0

    def on_data(self, data):
      try:
        if(self.num_tweets>10):
            return False
        msg = json.loads( data )
        self.num_tweets += 1
        print("new message")
        # if tweet is longer than 140 characters
        if "extended_tweet" in msg:
          # add at the end of each tweet "t_end"


          csv.write(msg['extended_tweet']['full_text'].replace('\n', '').replace('\r','') + '\n')
          print(msg['extended_tweet']['full_text'])
        else:
          # add at the end of each tweet "t_end"


          csv.write(msg['text'].replace('\n', '').replace('\r', '') +'\n')
          print(msg['text'])

        return True
      except BaseException as e:
          print("Error on_data: %s" % str(e))
          return True
    def on_error(self, status):
      print(status)
      return True

print('start sending data from Twitter to socket')
# authentication based on the credentials
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
# start sending data from the Streaming API
twitter_stream = Stream(auth, TweetsListener())
twitter_stream.filter(track=['crypto'], languages=["en"])



