import os

bind = os.environ.get('GUNICORN_BIND', '0.0.0.0:8000')
workers = int(os.environ.get('GUNICORN_WORKERS', '3'))
timeout = int(os.environ.get('GUNICORN_TIMEOUT', '30'))
accesslog = '-'
errorlog = '-'
