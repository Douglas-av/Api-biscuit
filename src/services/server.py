import sys
from configparser import ConfigParser
CONFIG = ConfigParser()
CONFIG.read("config.ini", encoding="utf-8")
sys.path.insert(0, CONFIG['PATHS']['PROJECT_PATH'])

from src import app 
from src.routes import routes



if __name__ == "__main__":
    app.run(debug=True)