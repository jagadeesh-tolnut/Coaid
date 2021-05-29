from django.shortcuts import render
from .models import Active_cases, Death_cases, Covid_tests, updateinfo
from datetime import datetime, timedelta

# Create your views here.
def home(request):
    try:
        date = datetime.today().strftime('%Y-%m-%d')
        active_data = Active_cases.objects.get(date=date)
        death_cases = Death_cases.objects.get(date=date)
        covid_tests = Covid_tests.objects.get(date=date)
        update_info = updateinfo.objects.get(date=date)
    except:
        date = datetime.today() - timedelta(1)
        active_data = Active_cases.objects.get(date=date)
        death_cases = Death_cases.objects.get(date=date)
        covid_tests = Covid_tests.objects.get(date=date)
        update_info = updateinfo.objects.get(date=date)
    Active_labels = []
    Active_data = []
    Death_labels = []
    Death_data = []
    Test_labels = []
    Test_data = []

    queryset = Active_cases.objects.order_by('date')
    for data in queryset:
        Active_labels.append(data.date.strftime('%d-%m-%Y'))
        Active_data.append(data.active)

    queryset = Death_cases.objects.order_by('date')
    for data in queryset:
        Death_labels.append(data.date.strftime('%d-%m-%Y'))
        Death_data.append(data.new)

    queryset = Covid_tests.objects.order_by('date')
    for data in queryset:
        Test_labels.append(data.date.strftime('%d-%m-%Y'))
        Test_data.append(data.total)

    context = {'Active_cases':active_data,'Death_cases':death_cases,'Covid_test':covid_tests,'updateinfo':update_info,'Active_labels':Active_labels,'Active_data':Active_data, 'Death_labels':Death_labels, 'Death_data':Death_data, 'Test_labels': Test_labels, 'Test_data':Test_data}
    return render(request, 'home/index.html',context)