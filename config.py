import os

class Config:
    '''
    General configuration parent class
    '''
    
    GIPHY_API_BASE_URL='https://api.giphy.com/v1/gifs/trending?api_key={}&limit=50&rating=g'
    # GIPHY_API_KEY=''
    GIPHY_API_KEY = os.environ.get('GIPHY_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kate:Kanini12@localhost/giphy'

    SQLALCHEMY_TRACK_MODIFICATIONS=False   

    UPLOADED_PHOTOS_DEST ='app/static/photos' 

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")



class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kate:Kanini12@localhost/giphy'
    
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}