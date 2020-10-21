from django.forms import ModelForm
from csv_discover.models import CSVFile


class FileForm(ModelForm):
    class Meta:
        model = CSVFile
        fields = '__all__'
