import calendar
from django.shortcuts import render, redirect
from django.utils import timezone
import pytz
from datetime import datetime
import matplotlib
matplotlib.use('Agg')
# https://teratail.com/questions/137426
# https://qiita.com/TomokIshii/items/3a26ee4453f535a69e9e
from matplotlib import pyplot as plt

from django.views import View
# models/pyからMoneyオブジェクトをインポートしますよ、という宣言
from .models import Money
from .forms import SpendingForm, FindForm
# plt.rcParams['font.family'] = 'IPAPGothic' #日本語の文字化け防止
from .utils import index_utils

TODAY = str(timezone.now()).split('-')


# Create your views here.
"""
ビューをクラス化して、GET時の挙動とPOST時の挙動を分ける。


"""

# クエリメソッド一覧  https://qiita.com/okoppe8/items/66a8747cf179a538355b


class MainView(View):
    def get(self, request, year=TODAY[0], month=TODAY[1]):
        # today = str(timezone.now()).split('-') #[year, month, day+time]の配列ができる

        # Moneyモデルからインポートしたレコードがここで読み込まれる
        money = Money.objects.filter(exchange_date__month=month).order_by('exchange_date')

        total = index_utils.calc_month_pay(money)
        index_utils.format_date(money)

        form = SpendingForm() # フォームのインスタンス化。ここでは、ページ上に入力フォームを呼び出すだけ
        next_year, next_month = index_utils.get_next(year, month)   # 多分間違ってる
        prev_year, prev_month = index_utils.get_prev(year, month)

        """
        ここで、exchange_dateの表示形式を整える（なので、無くても問題ない）。
        exchane_dateはdatetimeの情報を持つので、このままだと"2019年2月12日0:00"
        といった表示形式になる。（フォームでは時間の入力を受け付けていないため、自動的に0:00が割り当てられるみたい)
        そのため、split, joinメソッドを用いて必要な情報のみを取り出す。
        結果として、"02/11"という表記になる。
        """

        """
        for m in money:
            date = str(m.exchange_date).split(' ')[0]  # datetime.datetime(2019, 2, 23, 15, 49, 14, 205902)
            # ?? '/'.join()は、joinの引数と、/ を組み合わせるという解釈でOK?
            m.exchange_date = '/'.join(date.split('-')[1:3])
            total += m.amount
        """

        #  next_year, next_month = get_next(year, month)
        #  prev_year, prev_month = get_prev(year, month)

        context ={
                'year': year,
                'month': month,
                'prev_year': prev_year,
                'prev_month': prev_month,
                'next_year': next_year,
                'next_month': next_month,
                'money': money,
                'total': total,
                'form': form
                }
        draw_graph(year, month)

        return render(request, 'money/index.html', context)


    """ ここからフォームに関する処理の記述 """

    def post(self, request, year=TODAY[0], month=TODAY[1]):

        # ?? これ、formがインスタンスとして存在してるから、
        # POSTが実行されるときにそのインスタンスが生成されて、
        # dataにPOST内容が格納されるってこと？
        """ 本当はform.is_valid()メソッドを用いて入力値のバリデーションを行いたい """

        m_obj = Money()
        data = SpendingForm(request.POST, instance=m_obj)

        data.save()
        return redirect(to='/money/{}/{}'.format(year, month))


    """ ここまでフォームに関する記述 """




def edit(request,num):
    m_obj = Money.objects.get(id=num)

    if (request.method=='POST'):
        data = SpendingForm(request.POST,instance=m_obj)
        data.save()
        return redirect(to='/money')
    params={
        'id': num,
        'form': SpendingForm(instance=m_obj),
    }
    return render(request, 'money/edit.html', params)


def delete(request,num):
    money = Money.objects.get(id=num)
    if (request.method =='POST'):
        money.delete()
        return redirect(to='/money')
    params = {
        'id': num,
        'obj': money,
    }
    return render(request, 'money/delete.html', params)

def find(request):
    if (request.method == 'POST'):
        msg = 'search result:'
        form = FindForm(request.POST)
        s_word = request.POST['find']
        data = Money.objects.filter(detail__contains=s_word)
    else:
        msg = 'search words...'
        form = FindForm()
        data = Money.objects.all()
    params = {
        'message': msg,
        'form': form,
        'data': data,
    }
    return render(request, 'money/find.html', params)



def draw_graph(year, month):
    money = Money.objects.filter(exchange_date__year=year, exchange_date__month=month).order_by('exchange_date')
    last_day = calendar.monthrange(int(year), int(month))[1] + 1
    day = [i for i in range(1, last_day)]
    amount = [0 for i in range(len(day))]
    for m in money:
        temp_date = str(m.exchange_date).split('-')[2]
        amount[int(temp_date.split(' ')[0])-1] += int(m.amount)
        # amount[int(str(m.exchange_date).split('-')[2])-1] += int(m.amount)
        # date = str(m.exchange_date).split(' ')[0] #datetime.datetime(2019, 2, 23, 15, 49, 14, 205902)

    plt.figure()
    plt.bar(day, amount, color='#00bfff', edgecolor='#0000ff')
    plt.grid(True)
    plt.xlim([0, 31])
    plt.xlabel('Day', fontsize=16)
    plt.ylabel('Amount(Yen)', fontsize=16)
    # staticフォルダの中にimagesというフォルダを用意しておきその中に入るようにしておく
    plt.savefig('money/static/images/bar_{}_{}.svg'.format(year, month), transparent=True)
    return None


"""
def get_next(year, month):
    year = int(year)
    month = int(month)

    if month == 12:
        return str(year + 1), '1'
    else:
        return str(year), str(month + 1)


def get_prev(year, month):
    year = int(year)
    month = int(month)

    if month ==1:
        return str(year -1), '12'
    else:
        return str(year), str(month - 1)
"""