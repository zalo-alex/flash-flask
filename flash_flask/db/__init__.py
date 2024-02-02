try:
    from flash_flask.db.mysql import MySQL
except:
    pass # MySQL (mysql-connector-python) is not installed

from flash_flask.db.sqlite import Sqlite