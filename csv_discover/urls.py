from django.urls import path
from csv_discover.views import UploadFile

urlpatterns = [
    path("", UploadFile.as_view(), name='upload_file'),
]
