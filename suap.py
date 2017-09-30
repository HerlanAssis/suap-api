# -*- coding: utf-8 
import requests
import json
from pprint import pprint


class Suap(object):
    """docstring for Suap"""
    _token = ''
    _endpoint = 'https://suap.ifrn.edu.br/api/v2/'

    def __init__(self, token=False):
        super(Suap, self).__init__()
        if(token):
            self._token = token

    def autenticar(self, username, password, accessKey=False, setToken=True):
        # Se estiver acessando com uma chave de acesso...
        if accessKey:
            url = self._endpoint + 'autenticacao/acesso_responsaveis/'

            params = {
                'matricula': username,
                'chave': password,
            }
        else:
            url = self._endpoint + 'autenticacao/token/'

        params = {
            'username': username,
            'password': password,
        }
                
        req = requests.post(url, data=params)          

        data = False

        if req.status_code==200:
            data = json.loads(req.text)                
            if setToken and data['token'] :
                self.setToken(data['token'])                       

    def setToken(self, token):
        self._token = token

    def getMeusDados(self):
        url = self._endpoint + 'minhas-informacoes/meus-dados/'

        return self.doGetRequest(url)

    def doGetRequest(self, url):
        response = requests.get(url, headers =  {'Authorization': 'JWT ' + self._token, });

        data = False

        if (response.status_code == 200):
            data = json.loads(response.text)
    
        return data


# conecxao = Suap()
# conecxao.autenticar("sua_matricula", "sua_senha")
# dados = conecxao.getMeusDados()

# pprint(dict(dados))
