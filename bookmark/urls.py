from django.urls import path
from .views import *

urlpatterns = [
    # https://127.0.0.1/bookmark/???
    # ???
    path("", BookmarkListView.as_view(), name='list'),
    path("add/", BookmarkCreateView.as_view(), name='add'),
    path("detail/<int:pk>/", BookmarkDetailView.as_view(), name='detail'),
    path("update/<int:pk>/", BookmarkUpdateView.as_view(), name='update'),  # 클래스 뷰는 꼭 .as_view()를 입력해야 한다.
    path("delete/<int:pk>/", BookmarkDeleteView.as_view(), name='delete'),
]