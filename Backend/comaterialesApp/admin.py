from django.contrib import admin

from .models.user import User
from .models.categoria import Categoria
from .models.familia import Familia
from .models.producto import Producto

admin.site.register(User)
admin.site.register(Categoria)
admin.site.register(Familia)
admin.site.register(Producto)