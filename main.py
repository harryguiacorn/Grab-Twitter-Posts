import twint

# Configure
c = twint.Config()
c.Username = "TGTM_Official"
# c.Search = ""

c.Store_csv = True
c.Output = "none"

# Run
twint.run.Search(c)
