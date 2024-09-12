class Config:
    SECRET_KEY  = 'EEEEEEEEEEEEEEEEEEEEEEEEEEEEVUVOOKPOKOPjdppsnnvosoinigneionbooooooooinvioijio13h27r267foishvgg'
    DEBUG       = True

class DevelopmentConfig(Config):
    MSQL_HOST       = 'localhost'
    MYSQL_USER      = 'root'
    MSQL_PASSWORD   = ''
    MYSQL_DB        ='mytools'

config = {
    'development': DevelopmentConfig
}