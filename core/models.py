from django.db import models

class TranslationHistory(models.Model):
    english_text = models.TextField()
    german_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.english_text[:40]}..."
