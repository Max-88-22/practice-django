from django.shortcuts import render, HttpResponse
from django.db.models import Count, F
from .models import Employee
from django_pandas.io import read_frame
import pandas as pd
import plotly.express as px

def hello(request):
    qs = Employee.objects.values('department').annotate(
    num_emp=Count('id'), dep=F('department__name'), office=F('department__location__city'),
    country=F('department__location__country__name'), region=F('department__location__country__region__name'))
    df = read_frame(qs)
    df.drop(columns=['department'], inplace=True)
    fig = px.sunburst(data_frame=df, values='num_emp', path=['region','country','office', 'dep'])
    chart = fig.to_html()
    
    return HttpResponse(chart)
    

# Create your views here.
