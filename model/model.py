# -*- coding: utf-8 -*-
import requests
import json
import xml.etree.ElementTree as ET

class Model():
    SRV = "http://{}:8000/".format(None)
    terminal = 0
    service_id = 0
    current = None
    length = 0
    def __init__(self):
        Model.server = requests.session()
        tree = ET.parse('branches.xml')
        root = tree.getroot()
        self.set_server(root[0][0].attrib['name'])
    def get_branches(self):
        try:
            lst =[]
            tree = ET.parse('branches.xml')
            root = tree.getroot()
            for i in root[0]:
                lst.append([i.attrib['name'],i.attrib['ip']])
            return lst
        except:
            return []
    def set_server(self,name):
        ip = '127.0.0.1'
        tree = ET.parse('branches.xml')
        root = tree.getroot()
        for i in root[0]:
            if i.attrib['name'] == name:
                ip = i.attrib['ip']
                break
        self.SRV = "http://{}:8000/".format(ip)
    def get_services(self):
        r= requests.get(self.SRV+'queserver/services/')
        return r.content

    def get_terminals(self):
        r= requests.get(self.SRV+'queserver/terminals/')
        return r.content

    def get_username(self):
        r= requests.get(self.SRV+'queserver/users/')
        return r.content

    def login(self,username,password):
        print username,password
        try:
            res = Model.server.post(self.SRV+"api-token-auth/",{"username":"{}".format(username),"password":"{}".format(password)})
            if res.status_code == 200:
                self.TOKEN = json.loads(res.content)['token']
                print self.TOKEN
                Model.server.headers = {'Authorization': 'Token {}'.format(self.TOKEN)}
                print Model.server.headers
                return True
        except Exception as ex:
            print ex
            pass
        return False

    def get_reports(self,start,end,service,terminal,user):
        data = {"start": unicode(start), "end":unicode(end)}
        info = {}
        if service != u'الكل':info['service']=service
        if terminal != u'الكل':info['terminal']=terminal
        if user != u'الكل':info['user']=user
        data['info'] = info
        print data
        r = Model.server.get(self.SRV + "queserver/general-report/", json=json.dumps(data))
        ppp = json.loads(r.content)
        return ppp

    def get_reports_detailed(self,start,end,service):
        data = {"start": unicode(start), "end": unicode(end),"service":service}
        r = Model.server.get(self.SRV + "queserver/detailed-report/", json=json.dumps(data))
        ppp = json.loads(r.content)
        return ppp