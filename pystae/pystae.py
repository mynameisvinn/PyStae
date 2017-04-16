import pandas as pd 
import requests
 
def fetch_businesses(municipalityId):
    try:
        r = requests.get(municipalityId).json()
        return pd.DataFrame(r['results'])
    except ValueError:
        print "invalid municipalityId"