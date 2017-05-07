# pystae
pystae provides a simple interface to obtain stae datasets. datasets are returned in a data scientist friendly dataframe.

## Installation
install with `pip install pystae`

or from source:
``` 
git clone github.com/mynameisvinn/PyStae
cd PyStae
python setup.py install  # install
python setup.py develop  # or fetch requirements and install
```

## Requirements
pystae depends on [requests](http://docs.python-requests.org/en/latest/). other requirements in `requirements.txt`.

## Examples
```
from pystae import fetch_businesses
df = fetch_businesses(municipalityId='jers-nj')
print df.head()  # dataframe of jersey city businesses
```

## Stae Documentation
for official documentation on stae api, go [here](https://docs.municipal.systems/)

## Todo
* add local caching