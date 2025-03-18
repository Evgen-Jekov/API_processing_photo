from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'


if __name__ == "__main__":
    app.run(debug=True)