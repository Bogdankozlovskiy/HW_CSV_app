from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
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
            df = pd.read_csv(file_csv.file).to_html()
            df = mark_safe(df)
            file_name = file_csv.file.__str__().split('/')[-1]
            form = FileForm()
            return render(request, 'index.html', {'df': df, 'file_name': file_name, 'form': form})
        return redirect('upload_file')
# Create your views here.
