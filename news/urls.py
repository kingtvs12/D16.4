from django.urls import path
from .views import PostsList, PostDetail, PostSearch, PostCreate, PostUpdate, PostDelete, CategoryListView, upgrade_me, subscribe
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', PostsList.as_view(), name='post_list'),
    path('<int:pk>/', cache_page(60*10)(PostsList.as_view()), name='product_detail'),
    path('<int:pk>', PostDetail.as_view(), name='posts_detail'),
    path('search/', PostSearch.as_view(), name='posts_search'),
    path('create/', PostCreate.as_view(), name='new_create'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='new_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='new_delete'),
    path('articles/create/', PostCreate.as_view(), name='articles_create'),
    path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='articles_edit'),
    path('articles/<int:pk>/delete/', PostDelete.as_view(), name='articles_delete'),
    path('upgrade/', upgrade_me, name='upgrade'),
    path('categories/<int:pk>', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),

]