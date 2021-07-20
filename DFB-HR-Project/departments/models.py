from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# class Role(models.Model):
#     name = models.CharField(max_length=30)
#     department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="roles")
#
#     def __str__(self):
#         return self.name