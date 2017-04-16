import pandas as pd
import requests

def to_dataframe(func):
    def wrapper(municipalityId):
        return pd.DataFrame(func(municipalityId))
    return wrapper


@to_dataframe
def fetch_businesses(municipalityId):
    try:
    	identifier = 'https://municipal.systems/v1/municipalities/' + municipalityId + '/businesses'
        r = requests.get(identifier).json()
        return r['results']
    except ValueError:
        print "invalid municipalityId"


@to_dataframe
def fetch_building_permits(municipalityId):
    try:
    	identifier = 'https://municipal.systems/v1/municipalities/' + municipalityId + '/building_permits'
        r = requests.get(identifier).json()
        return r['results']
    except ValueError:
        print "invalid municipalityId"