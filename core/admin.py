from django.contrib import admin
from . import models

# Registra automáticamente todos los modelos "no abstractos"
for name in dir(models):
    obj = getattr(models, name)
    try:
        if hasattr(obj, '_meta') and obj._meta.abstract is False:
            admin.site.register(obj)
    except Exception:
        # algunos modelos pueden fallar por claves compuestas; ignóralos o regístralos a mano
        pass
