from django.db import models


class PropertyPublishedManager(models.Manager):
    def get_queryset(self):
        qs = super(PropertyPublishedManager, self).get_queryset()
        return qs.filter(published_status=True)
    

