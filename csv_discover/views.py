import numpy as np
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
            df = pd.read_csv(file_csv.file, sep=' ', index_col=0)
            response['df'] = mark_safe(df.to_html())
            response['file_name'] = file_csv.file.__str__().split('/')[-1]
            response['full_name'] = file_csv.file.__str__()
            response['form'] = FileForm()
            response['row_field'] = [df.index.name] + list(df.dtypes[df.dtypes == np.object].index)
            response['column_field'] = [df.index.name] + list(df.dtypes[df.dtypes == np.object].index)
            response['value_field'] = df.dtypes[df.dtypes != np.object].index
            return render(request, 'index.html', response)
        return redirect('upload_file')


class AggregateTable(View):
    def get(self, request):
        row_field = request.GET['row_field']
        column_field = request.GET['column_field']
        value_field = request.GET['value_field']
        full_name = f"./media/{request.GET['full_name']}"
        df = pd.read_csv(full_name, sep=' ', index_col=0)
        result = df.groupby([row_field, column_field]).agg({value_field: 'sum'}).to_html()
        result = mark_safe(result)
        return render(request, 'aggregate_table.html', {'result': result})
# Create your views here.
