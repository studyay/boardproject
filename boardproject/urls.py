from django.urls import path
from board.views import BoardView, BoardDetailView

urlpatterns = [
    path('', BoardView.as_view(), name='board'),
    path('detail/<str:pblanc_id>/', BoardDetailView.as_view(), name='board_detail'),
]