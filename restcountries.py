import requests
from accessmongo import *

REST_EU_ROOT_URL = "http://restcountries.eu/rest/v1"

def REST_country_request(field='all', name=None, params=None):

    headers={'User-Agent':'Mozilla/5.0'}

    if not params:
        params = {}

    if field == 'all':
        return requests.get(REST_EU_ROOT_URL + '/all')

    url = '%s/%s/%s'%(REST_EU_ROOT_URL, field, name)
    print('Requesting URL:'+url)
    response = requests.get(url,params=params,headers=headers)

    if not response.status_code == 200:
        raise Exception('Request failed with status code ' + str(response.status_code))

    return response


# response = REST_country_request('currency','usd')
# print response.json()

db_nobel = get_mongo_database('nobel_prize')
col = db_nobel['country_data'] 

# Get all the RESTful country-data
response = REST_country_request()

country_data = response.json()
#Insert the JSON objects straight to our collection
col.insert(country_data)


