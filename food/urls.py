from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    # /food/
    path('', views.IndexClassView.as_view(), name='index'),
    # /food/1
    path('item/', views.item, name="item"),
    path('<int:pk>/', views.DetailCLassItem.as_view(), name='detail'),
    # delete
    path('<int:item_id>/delete', views.deleteItem , name='delete_item'),
    # add item
    path('add', views.CreateItem.as_view(), name="create_item"),
    # edit
    path('update/<int:item_id>/', views.update_item, name="update_item")
]