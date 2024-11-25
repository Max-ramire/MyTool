class Config:
    SECRET_KEY  = 'EEEEEEEEEEEEEEEEEEEEEEEEEEEEVUVOOKPOKOPjdppsnnvosoinigneionbooooooooinvioijio13h27r267foishvgg'
    DEBUG       = True

class DevelopmentConfig(Config):
    #localhost
    MYSQL_HOST       = 'localhost'
    MYSQL_USER      = 'root'
    MSQL_PASSWORD   = 'myql'
    MYSQL_DB        ='mytools'
    
    #pythonanywhere
    '''MYSQL_HOST       = 'mytool.mysql.pythonanywhere-services.com'
    MYSQL_USER      = 'mytool'
    MSQL_PASSWORD   = 'juan123loZ'
    MYSQL_DB        ='mytools' '''

class ConfigMail(Config):
    MAIL_SERVER         = 'smtp.gmail.com'
    MAIL_PORT           = 587
    MAIL_USE_TLS        = True
    MAIL_USE_SSL        = False
    MAIL_USERNAME       = 'juan.ramirez1750@alumnos.udg.mx'
    MAIL_PASSWORD       = 'wqjt aple bskv gbby'            
    MAIL_DEFAULT_SENDER = 'juan.ramirez1750@alumnos.udg.mx'
    MAIL_ASCII_ATTACHEMENT = True
config = {
    'development': DevelopmentConfig,
    'mail'       :MailConfig   
}