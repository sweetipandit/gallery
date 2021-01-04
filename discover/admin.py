from django.contrib import admin

# Register your models here.

from .models import ImageModel
from .models import RegistrationModel


admin.site.register(ImageModel)
admin.site.register(RegistrationModel)
