from django.db import models

class InfoFAQs(models.Model):
    faq_title = models.CharField(max_length=100)
    faq_details = models.TextField()
    faq_type = models.IntegerField()

    def __str__(self):
        return self.faq_title
