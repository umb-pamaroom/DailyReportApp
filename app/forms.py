from django.forms import ModelForm
from .models import Memo


class MemoForm(ModelForm):
    class Meta:
        model = Memo
        fields = ['discovery', 'tired', 'dislike','happy', 'best', 'tomorrow', 'other', 'summarize']
        labels = {
            'discovery': '新しい発見',
            'tired': '疲れたこと',
            'dislike': '嫌だったこと',
            'happy': '嬉しかったこと',
            'best': '頑張ったこと',
            'tomorrow': '明日したいこと',
            'other': 'その他',
            'summarize': '1日のまとめ',
        }
