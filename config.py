#discord config file



# Flask configuration

SECRET_KEY = 'cc1234'

# credentials for HTTP Basic auth
BASIC_AUTH_USERNAME = 'zandibot'
BASIC_AUTH_PASSWORD = 'guest1234!'

# enable HTTP Basic auth
BASIC_AUTH_FORCE = True

# create in-memory database
DATABASE_FILE = 'discordbot.db'
SQLALCHEMY_DATABASE_URI = 'sqlite:////var/www/discordbot/' + DATABASE_FILE

# disable SQLAlchemy from tracing modifications to objects
SQLALCHEMY_TRACK_MODIFICATIONS = False

# bot configuration
DEBUG = False
COMMAND_SYMBOL = '?'
DISCORD_TOKEN = 'MzU3MjgyNjg2MzQwOTU2MTYx.DJnpiw.UQD6zQ5TUoQToHIuX6VdRmI-f9c'