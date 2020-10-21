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
        response = {}
        if form.is_valid():
            file_csv = form.save()
            df = pd.read_csv(file_csv.file, sep=' ', index_col=0).to_html()
            response['df'] = mark_safe(df)
            response['file_name'] = file_csv.file.__str__().split('/')[-1]
            response['form'] = FileForm()
            response['row_field'] = ['Date']
            response['column_field'] = ['Product', 'Sales', 'Person']
            response['value_field'] = ['Qty', 'Total']
            return render(request, 'index.html', response)
        return redirect('upload_file')


class AggregateTable(View):
    def get(self, request):
        row_field = request.GET['row_field']
        column_field = request.GET['column_field']
        value_field = request.GET['value_field']
        print(row_field, column_field, value_field)
        return render(request, 'aggregate_table.html')
# Create your views here.
