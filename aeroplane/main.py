import os
import sys

from django.conf import settings
from django.apps import apps
from django.core.asgi import get_asgi_application


from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aeroplane.settings")
apps.populate(settings.INSTALLED_APPS)


from aeroplane.endpoints import router


app = FastAPI(title="Aeroplane", debug=settings.DEBUG)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router, prefix="/api")
app.mount("/dj", get_asgi_application())
