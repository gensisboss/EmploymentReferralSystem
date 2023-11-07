from import_export import resources
from .models import *


class StuResource(resources.ModelResource):
    class Meta:
        model = stu


# class JobResource(resources.ModelResource):
#     class Meta:
#         model = job
