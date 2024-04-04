from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    views = models.IntegerField(default = 0)

    def increase_views(self):
        self.views += 1
        self.save()