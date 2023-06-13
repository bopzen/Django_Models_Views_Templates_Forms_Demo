from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Models Demo'
admin.site.index_title = 'Models Demo Administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('models_demo.hr.urls')),
    path('barbershops/', include('models_demo.barbershops.urls'))
]
