from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from models_demo.hr.views import home, show_employees, show_departments, show_positions, delete_employee, \
    details_employee, details_by_slug_employee, show_test_form, show_edit_employee_form, show_success, show_upload_image, show_validation_form

urlpatterns = [
    path('', home, name='home'),
    path('employees/', show_employees, name='show-employees'),
    path('delete/<int:pk>', delete_employee, name='delete-employee'),
    path('details/<int:pk>', details_employee, name='details-employee'),
    path('detailsbyslug/<slug:slug>', details_by_slug_employee, name='details-by-slug-employee'),
    path('departments/', show_departments, name='show-departments'),
    path('positions/', show_positions, name='show-positions'),
    path('forms/', show_test_form, name='show-forms'),
    path('validation-forms/', show_validation_form, name='show-validation-forms'),
    path('edit-employee/<slug:slug>', show_edit_employee_form, name='edit-employee'),
    path('upload-image/', show_upload_image, name='show-upload-image'),
    path('success/', show_success, name='success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)