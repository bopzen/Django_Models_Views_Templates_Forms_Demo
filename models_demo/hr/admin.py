import datetime

from django.contrib import admin
from models_demo.hr.models import Employee, Department, Position, JobLevel, Project, Location, Username


@admin.register(Username)
class UsernameAdmin(admin.ModelAdmin):
    list_display = ['username', 'password']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email_address', 'position', 'department', 'created_on', 'updated_on']
    list_filter = ['first_name', 'last_name', 'email_address', 'position', 'department', 'created_on', 'updated_on']
    search_fields = ['first_name', 'last_name', 'email_address', 'position', 'department', 'created_on', 'updated_on']
    prepopulated_fields = {"slug": ("first_name", "last_name")}


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department_name']
    list_filter = ['department_name']
    search_fields = ['department_name']


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['position_name']
    list_filter = ['position_name']
    search_fields = ['position_name']


@admin.register(JobLevel)
class JobLevelAdmin(admin.ModelAdmin):
    list_display = ['level_name']
    list_filter = ['level_name']
    search_fields = ['level_name']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'deadline']
    list_filter = ['name', 'description', 'deadline']
    search_fields = ['name', 'description', 'deadline']


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['city']
    list_filter = ['city']
    search_fields = ['city']

