from django.db import models


class Tag(models.Model):
    name = models.CharField(
        max_length=63,
        blank=False,
        null=False,
        unique=True
    )

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    content = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["is_done", "-created"]

    def __str__(self) -> str:
        return f"{self.content} {'Done' if self.is_done else 'Not done'}"
