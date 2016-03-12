import requests

class Jobs():
    JENKIN_URL = 'http://10.89.104.33:9090'

    def create(self, jobtitle, config):
        headers = {'content-type': 'application/xml'}
        r = requests.post(self.JENKIN_URL + '/createItem?name=' + jobtitle, data=config, headers=headers)
        return r.status_code == requests.codes.ok

    def get(self, view):
        r = requests.get('http://10.89.104.33:9090/view/' + view + '/api/json')
        body = r.json()
        jobs = body['jobs']
        return jobs