from django.contrib import admin
from .models import Money
# Register your models here.

admin.site.register(Money)
"""
ここで指定したモデルは、管理者ページで編集可能になる
なお、ログイン先ではMoney's' として表示されているが、これは複数のデータが保管されているから
Moneysという理解でよろしい
"""