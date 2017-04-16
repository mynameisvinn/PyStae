# PyStae

a tool for downloading datasets in a python pandas friendly format from stae-powered open data portals.

users can provide a 'stae' dataset resource url and retrieve a pandas dataframe.

## Installation
install with `pip install pystae`

from source:
``` 
git clone github.com/mynameisvinn/PyStae
cd PyStae
python setup.py install  # install
python setup.py develop  # fetch requirements and install
```

## Requirements
pystae depends on [requests](http://docs.python-requests.org/en/latest/). other requirements listed in `requirements.txt`.

## Examples
```
from pystae import fetch_businesses
df = fetch_businesses(municipalityId='jers-nj')
df.head()  # dataframe containing businesses in jersey city
```

## Stae Documentation
for official documentation on stae api, go [here](https://docs.municipal.systems/)