from django.apps import apps
from django.contrib import admin

# Register all other models
models = apps.get_models()
for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
