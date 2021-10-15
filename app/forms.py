from django.forms import ModelForm
from .models import Memo


class MemoForm(ModelForm):
    class Meta:
        model = Memo
        fields = ['discovery', 'tired', 'happy', 'best', 'tomorrow', 'dislike','other', 'summarize']
        labels = {
            'discovery': '新しい発見',
            'tired': '一番印象に残ったこと',
            'dislike': '改善点',
            'happy': '嬉しかったこと',
            'best': '頑張ったこと',
            'tomorrow': '明日したいこと',
            'other': 'その他',
            'summarize': '1日のまとめ',
        }
