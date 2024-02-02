from flash_flask.db import Sqlite

from flash_flask import App

app = App(__name__)

if __name__ == "__main__":
    app.run(debug=True)