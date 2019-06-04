from django.contrib import admin
from .models import Money, Message
# Register your models here.

admin.site.register(Money)
admin.site.register(Message)
"""
ここで指定したモデルは、管理者ページで編集可能になる
なお、ログイン先ではMoney's' として表示されているが、これは複数のデータが保管されているから
Moneysという理解でよろしい
"""