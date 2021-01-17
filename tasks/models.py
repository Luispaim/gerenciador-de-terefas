from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=254, verbose_name='Nome')
    status = models.BooleanField(default=False, verbose_name="Status")

    class Meta:
        ordering = ["name"]
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"

    def __str__(self):
        return self.name
