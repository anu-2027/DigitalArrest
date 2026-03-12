import sys
import os

# Add project root to path so Flask can import app.py
# and find templates/ and static/ directories
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, ROOT)
os.chdir(ROOT)  # Flask resolves templates/ relative to cwd

import serverless_wsgi
from app import app

def handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)
