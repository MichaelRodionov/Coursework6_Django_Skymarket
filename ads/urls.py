from django.urls import path

from ads.views import *


# ----------------------------------------------------------------
# urlpatterns
urlpatterns = [
    path('', AdvertisementListCreateView.as_view(), name='advertisement-list-create'),
    path('me/', AdvertisementPersonalListView.as_view()),
    path('<int:pk>/', AdRetrieveUpdateDestroyView.as_view(), name='advertisement-retrieve-update-destroy'),
    # path('<int:pk>/', AdvertisementUpdateView.as_view()),
    # path('<int:pk>/', AdvertisementDeleteView.as_view()),
    path('<int:ad_pk>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('<int:ad_pk>/comments/<int:id>/', CommentRetrieveUpdateDestroyView.as_view(), name='comment-retrieve-update-destroy'),
]
