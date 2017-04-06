# coding=utf-8
import web
import json


"""ssl = True #activate ssl certificate 

if ssl == True:
    from web.wsgiserver import CherryPyWSGIServer
    '''
    Use OpenSSL to generate  keys

    user@host$ openssl genrsa -out server.key 1024
    user@host$ openssl req -new -key server.key -out server.csr
    user@host$ openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt

    '''
    CherryPyWSGIServer.ssl_certificate = "ssl/server.crt" 
    CherryPyWSGIServer.ssl_private_key = "ssl/server.key"
    """


urls = (
	'/','Index',
    '/download', 'Download',
    '/help', 'Help',
    '/info', 'Info',
)

db_host = 'localhost'
db_name = 'proacademy'
db_user = 'root'
db_pw = ''

app = web.application(urls, globals())
render = web.template.render('templates', base='master')


class Index:        
    def GET(self):
        return render.index()
    
class Download:
    def GET(self):
        return render.download()
    
class Help:
    def GET(self):
        return render.help()
    
class Info:
    def GET(self):
        return render.info()
                    
    
if __name__ == "__main__":
    #web.config.debug = False
    app.run()