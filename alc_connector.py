import config1
import sqlalchemy
from sqlalchemy import create_engine
import mysql.connector
config1.schema = 'Crimes1'
config1.port = 3306
sql_alchemy_connection = (
                               f'mysql+mysqlconnector://'
                               f'{config1.user}:{config1.password}'
                               f'@{config1.host}:{config1.port}'
                               f'/{config1.schema}'
                          )
db = create_engine(sql_alchemy_connection)
db.connect()