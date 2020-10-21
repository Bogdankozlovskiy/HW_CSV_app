from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from csv_discover.forms import FileForm
import pandas as pd


class UploadFile(View):
    def get(self, request):
        form = FileForm()
        return render(request, 'index.html', {'form': form})

    def post(self, request):
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file_csv = form.save()
        print(file_csv.file)
        return render(request, 'explorer_file.html')
# Create your views here.
