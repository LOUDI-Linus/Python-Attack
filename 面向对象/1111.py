"""
@file: 1111
@author: Cooper.wy_zou1103@163.com
@date: 2021/07/29
@decs

"""
import requests
import json



class RestartService(object):
    def __init__(self):
        self.login_url = 'http://oneops-plus.beisen-inc.com/login'
        self.app_mate_url = 'https://oneops-plus.beisen-inc.com/api/asset/servers/simple'
        self.app_service_url = 'http://oneops-plus.beisen-inc.com/api/appmetas/{}/environments/{}/service/permission'
        self.restart_url = 'http://oneops-plus.beisen-inc.com/api/services/{}/restart'
        self.header = {'content-type': 'application/json',
                       'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
        self.payload = {
            'username': 'lihe1',
            'password': 'Yxhy40#703'
        }
        self.environment = {
            'Development': 1,
            'Testing': 3,
            'Labs': 4,
            'Production': 5,
            'SandBox': 6
        }

    def get_cookie(self):
        res = requests.post(self.login_url, data=self.payload)
        return res.cookies

    def get_meta_id(self):
        url_get_mate = '{}?environmentId={}&serverNumber={}'.format(self.app_mate_url, '3', '100')
        res_1 = requests.get(url_get_mate, headers=self.header, cookies=self.get_cookie())
        meta_info = json.loads(res_1.content)
        return meta_info['data']

if __name__ =='__main__':
    test = RestartService()
    res = test.get_meta_id()
    dict_host_ip = {}
    for i in res:
        dict_host_ip[i['hostname']] = i['ip']
    print(dict_host_ip)
    print(dict_host_ip['BYVW-WEB-49-197'])