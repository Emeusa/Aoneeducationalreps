"""
WSGI config for oneweb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/mrfashwork/onewebssss/oneweb')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oneweb.settings')

application = get_wsgi_application()
