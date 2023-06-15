from django.shortcuts import render, get_object_or_404, redirect

from models_demo.hr.forms import TestForm, EmployeesForm, UsernameForm, ImageForm
from models_demo.hr.models import Employee, Department, Position, Image


def home(request):
    employees = Employee.objects.all()
    employees2 = Employee.objects.filter(birth_date__year__gte=1985)\
        .order_by("-first_name")
    context = {
        'employees': employees,
        'employees2': employees2,
    }
    return render(request, 'index.html', context)


def show_employees(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'employees.html', context)


def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('home')


def details_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    context = {
        'employee': employee
    }
    return render(request, 'details-employee.html', context)


def details_by_slug_employee(request, slug):
    employee = get_object_or_404(Employee, slug=slug)
    context = {
        'employee': employee
    }
    return render(request, 'details-employee.html', context)


def show_departments(request):
    departments_list = Department.objects.all()
    context = {
        'department_list': departments_list
    }
    return render(request, 'departments.html', context)


def show_positions(request):
    positions_list = Position.objects.all()
    context = {
        'positions_list': positions_list
    }
    return render(request, 'positions.html', context)


def show_test_form(request):
    test_form = TestForm(request.POST or None)
    model_form = EmployeesForm(request.POST or None)
    username_form = UsernameForm(request.POST or None)
    context = {
        'test_form': test_form,
        'model_form': model_form,
        'username_form': username_form
    }
    if test_form.is_valid():
        return redirect('success')
    if model_form.is_valid():
        model_form.save()
        return redirect('success')
    if username_form.is_valid():
        username_form.save()
        return redirect('success')
    return render(request, 'forms.html', context)


def show_edit_employee_form(request, slug):
    employee = get_object_or_404(Employee, slug=slug)
    edit_employee_form = EmployeesForm(request.POST or None, instance=employee)
    context = {
        'edit_employee_form': edit_employee_form
    }
    if edit_employee_form.is_valid():
        edit_employee_form.save()
        return redirect('details-by-slug-employee', slug)
    return render(request, 'edit-employee.html', context)


def show_upload_image(request):
    image_form = ImageForm()
    images = Image.objects.all()
    if request.method == 'POST':
        image_form = ImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            image = image_form.save()
            image.save()
            # return redirect('success')

    context = {
        'image_form': image_form,
        'images': images
    }
    return render(request, 'upload-image.html', context)


def show_success(request):
    return render(request, 'success.html')