from pprint import pprint
import requests
import time

def fromedate(number_of_days_ago):
    return str(int((time.time() - number_of_days_ago * 24 * 60*60) // 1))

class Site_Stackexchange:
    API_BASE_URL = 'https://api.stackexchange.com/'
    params = {'order': 'desc', 'site': 'stackoverflow'}
    # def __init__(self, token=''):
    #     self.token = token
    def articles(self, number_of_days_ago=None, tag=None):
        titles = []
        if number_of_days_ago != None:
            from_data = fromedate(number_of_days_ago)
            self.params ={**self.params, **{'fromdate': from_data}}
        response = requests.get(self.API_BASE_URL + '/2.3/articles', params=self.params)
        for item in response.json()['items']:
            if tag != None:
                if tag.lower() in ','.join(item['tags']).lower():
                    titles += [item['title']]
            else:
                titles += [item['title']]
        if len(titles) == 0:
            print('По данному запросу не чего не найдено')
        else:
            print('\n'.join(titles))
        # pprint(response.json())

if __name__ == '__main__':
    # number_of_days_ago = int(input())
    number_of_days_ago = 2
    tag = 'python'
    new_request = Site_Stackexchange()
    result =new_request.articles(number_of_days_ago, tag)
    # url = 'https://api.stackexchange.com/'
    # params = {'order': 'desc', 'site': 'stackoverflow'}
    # params.update({'fromdate': from_data})
    # print(params)
    # response = requests.get(url+'/2.3/articles', params=params)
    # pprint(response.json())