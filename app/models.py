from django.db import models

# Memoモデルを作成する
class Memo(models.Model):

    # 新しい発見
    discovery = models.TextField(blank=True)

    # 新しい発見
    tired = models.TextField(blank=True)

    # 新しい発見
    dislike = models.TextField(blank=True)

    # 新しい発見
    happy = models.TextField(blank=True)

    # 新しい発見
    best = models.TextField(blank=True)

    # 新しい発見
    tomorrow = models.TextField(blank=True)

    # 新しい発見
    other = models.TextField(blank=True)

    # 新しい発見
    summarize = models.TextField(blank=True)

    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
