from django.db import models


class WorldBankData(models.Model):
    country_name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=3)
    indicator_name = models.CharField(max_length=200)
    indicator_code = models.CharField(max_length=50)
    year = models.IntegerField()
    value = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['country_code', 'indicator_code', 'year']
        ordering = ['-year', 'country_name']
    
    def __str__(self):
        return f"{self.country_name} - {self.indicator_name} ({self.year})"