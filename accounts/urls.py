from django.urls import path, register_converter
from accounts import views
from common.utils import HashIdConverter


app_name = "api_accounts"

register_converter(HashIdConverter, "hashid")

urlpatterns = [
    path("", views.AccountsListView.as_view()),
    path("<int:pk>/", views.AccountDetailView.as_view()),
    path("<int:pk>/create_mail/", views.AccountCreateMailView.as_view()),
    path("comment/<int:pk>/", views.AccountCommentView.as_view()),
    path("attachment/<int:pk>/", views.AccountAttachmentView.as_view()),
]
