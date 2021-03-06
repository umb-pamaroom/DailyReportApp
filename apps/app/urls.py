from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:memo_id>', views.detail, name='detail'),
    # path('date/<int:dateData>', views.detail, name='date'),
    path('new_memo', views.new_memo, name='new_memo'),

    # 食事一覧
    path('meal_list', views.meal_list, name='meal_list'),
    path('breakfast_list', views.breakfast_list, name='breakfast_list'),
    path('lunch_list', views.lunch_list, name='lunch_list'),
    path('dinner_list', views.dinner_list, name='dinner_list'),
    
    path('delete_memo/<int:memo_id>', views.delete_memo, name='delete_memo'),
    path('edit_memo/<int:memo_id>', views.edit_memo, name='edit_memo'),
]
