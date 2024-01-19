from django.urls import path
from posts.views import dummy_view, status_code_view, entry_list, redirect_back_home, MyClassView

app_name = 'posts'

urlpatterns = [
    path('', MyClassView.as_view(), name='entry-list'),
    path('<id>/', dummy_view, name='entry-detail'),
    # path('<?pid>/', dummy_view, name='entry-detail'),
    path('<id>/delete/', dummy_view, name='entry-delete'),
    path('<id>/update/', dummy_view, name='entry-update'),
]
