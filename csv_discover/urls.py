from django.urls import path
from csv_discover.views import UploadFile, AggregateTable

urlpatterns = [
    path("get_aggregate", AggregateTable.as_view(), name='aggregate_table'),
    path("", UploadFile.as_view(), name='upload_file'),
]
