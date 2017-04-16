import pandas as pd 
import requests
 
def fetch_businesses(municipalityId):
    try:
    	identifier = 'https://municipal.systems/v1/municipalities/' + municipalityId + '/businesses'
        r = requests.get(identifier).json()
        return pd.DataFrame(r['results'])
    except ValueError:
        print "invalid municipalityId"