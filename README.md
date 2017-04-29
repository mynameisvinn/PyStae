# pystae
pystae provides a simple interface to obtain stae datasets and return them as a (data scientist friendly) pandas dataframe.

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
print df.head()  # dataframe containing businesses in jersey city
```

## Stae Documentation
for official documentation on stae api, go [here](https://docs.municipal.systems/)

## Todo
* add local caching mechanism