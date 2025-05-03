pytest tests/test_jwt.py
pytest tests/test_user.py

gunicorn core:app -b :5000 -k gevent
