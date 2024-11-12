class Config:
    SECRET_KEY  = 'EEEEEEEEEEEEEEEEEEEEEEEEEEEEVUVOOKPOKOPjdppsnnvosoinigneionbooooooooinvioijio13h27r267foishvgg'
    DEBUG       = True

class DevelopmentConfig(Config):
    #localhost
   ''' MYSQL_HOST       = 'localhost'
    MYSQL_USER      = 'root'
    MSQL_PASSWORD   = 'myql'
    MYSQL_DB        ='mytools' '''
    
    #pythonanywhere
    MYSQL_HOST       = 'mytool.mysql.pythonanywhere-services.com'
    MYSQL_USER      = 'mytool'
    MSQL_PASSWORD   = 'juan123loZ'
    MYSQL_DB        ='mytools'

config = {
    'development': DevelopmentConfig
}