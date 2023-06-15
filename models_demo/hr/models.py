from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


class CreateUpdateMixin(models.Model):
    class Meta:
        abstract = True

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class Department(CreateUpdateMixin, models.Model):
    department_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.department_name}'


class Position(CreateUpdateMixin, models.Model):
    position_name = models.CharField(max_length=50)
    department = models.ForeignKey(to=Department, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.position_name}'


class JobLevel(CreateUpdateMixin, models.Model):
    level_name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.level_name}'


class Project(CreateUpdateMixin, models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    deadline = models.DateField()

    def __str__(self):
        return f'{self.name}'


class Location(CreateUpdateMixin, models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.city}'


class Employee(CreateUpdateMixin, models.Model):
    class Meta:
        ordering = ['first_name']

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email_address = models.EmailField(unique=True)
    birth_date = models.DateField()
    works_full_time = models.BooleanField()
    city = models.ForeignKey(to=Location, on_delete=models.RESTRICT)
    department = models.ForeignKey(to=Department, on_delete=models.RESTRICT, null=True, blank=True)
    position = models.ForeignKey(to=Position, on_delete=models.RESTRICT, null=True, blank=True)
    job_level = models.ForeignKey(to=JobLevel, on_delete=models.RESTRICT, null=True, blank=True)
    project = models.ManyToManyField(Project)
    slug = models.SlugField(unique=True)


    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def all_projects(self):
        return ", ".join([pr.name for pr in self.project.all()])

    def get_absolute_url(self):
        return reverse('details-employee', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.position}'

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.first_name}-{self.last_name}')
        return super().save(*args, **kwargs)


class Username(CreateUpdateMixin, models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.username}'


class Image(CreateUpdateMixin, models.Model):
    image = models.ImageField(upload_to='images')