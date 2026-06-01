from django.db import models
from shelters.models import Shelter

class Campaign(models.Model):
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE, related_name='campaigns')
    title = models.CharField(max_length=200)
    description = models.TextField()
    target_amount = models.BigIntegerField(help_text="هدف به تومان")
    collected_amount = models.BigIntegerField(default=0, help_text="جمع‌آوری شده به تومان")
    image_url = models.CharField(max_length=500, blank=True, help_text="لینک عکس حیوان")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.shelter.name}"

    def progress_percent(self):
        if self.target_amount == 0:
            return 0
        return int((self.collected_amount / self.target_amount) * 100)