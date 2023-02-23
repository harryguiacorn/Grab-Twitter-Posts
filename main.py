import twint
from datetime import datetime

# Configure
c = twint.Config()
c.Username = "TGTM_Official"
c.Limit = 20
# c.Until = "2022-06-06"
# c.Search = ""
c.Pandas = True
df = twint.storage.panda.Tweets_df

# FAQ: Twitter can shadow-ban accounts, which means that their tweets will not be available via search.
c.Profile_full = True

c.Store_csv = True
__dt = datetime.now()
dt_string = __dt.strftime("%Y-%m-%d %H-%M-%S")
c.Output = "data/" + dt_string + ".csv"

# Run
twint.run.Search(c)

twint.run.Followers(c)

Followers_df = twint.storage.panda.Follow_df
list_of_followers = Followers_df['followers']['TGTM_Official']

print(list_of_followers)
