import snscrape.modules.twitter as ss
import pandas as pd
from datetime import datetime

scraper = ss.TwitterUserScraper("TGTM_Official")

tweets = []

for i, tweet in enumerate(scraper.get_items()):
    data = [
        tweet.date, 
        tweet.id,
        tweet.rawContent,
        tweet.url
    ]
    tweets.append(data)
    # if i > 20:
    #     break
# print(tweets)

tweet_df = pd.DataFrame(tweets, columns=['date', 'id', 'content', 'link'])
__dt = datetime.now()
dt_string = __dt.strftime("%Y-%m-%d %H-%M-%S")
tweet_df.to_csv("data/" + dt_string + ".csv")
print(tweet_df)