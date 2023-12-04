from django.db import models

class Feedback(models.Model):
    full_name = models.CharField(max_length=60, blank=False)
    email = models.EmailField()
    feedback = models.TextField()
    checkbox = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.full_name}; {self.email}; {self.feedback}; {self.checkbox}'


