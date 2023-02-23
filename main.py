import twint
import pandas as pd
from datetime import datetime

# Configure
c = twint.Config()
c.Username = "TGTM_Official"
c.Limit = 20
# c.Until = "2022-06-06"
# c.Search = ""
c.Pandas = True
# FAQ: Twitter can shadow-ban accounts, which means that their tweets will not be available via search.
c.Profile_full = True

c.Store_csv = True
__dt = datetime.now()
dt_string = __dt.strftime("%Y-%m-%d %H-%M-%S")
c.Output = "data/" + dt_string + ".csv"

# Run
# twint.run.Search(c)
# df = twint.storage.panda.Tweets_df

df_sample = pd.read_csv("data/sample.csv")
df_sample['index'] = df_sample.index
# movies_df.set_index('index')

new_cols = ["index", "link", "date", "replies_count",
            "retweets_count", "likes_count", "tweet"]
df_sample = df_sample.reindex(columns=new_cols)
df_sample.rename(columns={'index': 'Tweet', 'link': 'URL',
                          'date': 'Date', 'replies_count': 'Replies',
                          'retweets_count': 'Retweets', 'likes_count': 'Likes',
                          'tweet': 'Tweet Content'}, inplace=True)

# df2=movies_df.reset_index()
print(df_sample)
# print(df2)
