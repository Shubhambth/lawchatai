# api.py
from core.wsgi import application

# Vercel Python runtime looks for a variable named `app`
app = application
