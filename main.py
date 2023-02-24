import twint
import pandas as pd
from datetime import datetime

# Configure
c = twint.Config()
c.Username = "TGTM_Official"
# c.Limit = 20
# c.Until = "2022-06-07"
# c.Search = ""
c.Pandas = True
# FAQ: Twitter can shadow-ban accounts, which means that their tweets will not be available via search.
c.Profile_full = True

c.Store_csv = True
__dt = datetime.now()
dt_string = __dt.strftime("%Y-%m-%d %H-%M-%S")
c.Output = "data/" + dt_string + ".csv"

# Run
twint.run.Search(c)
# df = twint.storage.panda.Tweets_df # this line is commented out as some of the column names are inconsistant if parsed directly, the alternative is to load csv instead.

df = pd.read_csv("data/" + dt_string + ".csv") # load csv from local
df = df.iloc[::-1]  # flip rows
df.reset_index(inplace=True, drop=True)  # reset index column after the flip as we want the index numbers to be ascending
df = df.reset_index()

new_cols = ["index", "link", "date", "user_id","replies_count",
            "retweets_count", "likes_count", "tweet", "language"]
df = df.reindex(columns=new_cols)

# print("--------------------------------------------")
# print(df.head().to_csv("test"))

dict_mainLanguage = {
    "zh": "1", "en": "2", "de": "3", "ja": "4", "ru": "5"
}

l_mainLanguage = []
for (i,value) in enumerate(df["language"]):
    # print(i, value, dict_mainLanguage.get(value, "6"))
    l_mainLanguage.append(dict_mainLanguage.get(value, "6"))
df['language'] = l_mainLanguage # insert converted items into a new column

df.rename(columns={'index': 'Tweet', 'link': 'URL',
                   'date': 'Date', 'replies_count': 'Replies',
                   'retweets_count': 'Retweets', 'likes_count': 'Likes',
                   'tweet': 'Tweet Content',
                   'language': 'Main language use'}, inplace=True)


df.to_csv("data/" + dt_string + "-generated.csv")
