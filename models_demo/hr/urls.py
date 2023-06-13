from django.urls import path
from models_demo.hr.views import home, show_employees, show_departments, show_positions, delete_employee, \
    details_employee, details_by_slug_employee, show_test_form, show_edit_employee_form, show_success

urlpatterns = [
    path('', home, name='home'),
    path('employees/', show_employees, name='show-employees'),
    path('delete/<int:pk>', delete_employee, name='delete-employee'),
    path('details/<int:pk>', details_employee, name='details-employee'),
    path('detailsbyslug/<slug:slug>', details_by_slug_employee, name='details-by-slug-employee'),
    path('departments/', show_departments, name='show-departments'),
    path('positions/', show_positions, name='show-positions'),
    path('forms/', show_test_form, name='show-forms'),
    path('edit-employee/<slug:slug>', show_edit_employee_form, name='edit-employee'),
    path('success/', show_success, name='success')
]