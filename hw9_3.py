from pprint import pprint
import requests
import datetime

url = 'https://api.stackexchange.com/'

now = datetime.datetime.now()
print(now.microsecond)
print(now)

# response = requests.get(url+'/2.3/articles?order=desc&sort=activity&tagged=python&site=stackoverflow')
# pprint(response.json())