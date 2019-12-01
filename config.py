import os

class Config:
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	UPLOADED_PHOTOS_DEST ='app/static/photos'
	SECRET_KEY = os.environ.get('SECRET_KEY')
	SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://aphya5:NewPasword@localhost/blog_post'

	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
	MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

	@staticmethod
	def init_app(app):
		pass


class TestConfig(object):
	"""docstring for TestConfig."""

	SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://aphya5:NewPasword@localhost/blog_post_test'


class ProdConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://aphya5:NewPasword@localhost/blog_post'

	DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}
