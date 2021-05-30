from django.shortcuts import render, redirect
from .models import Search_by_pin
from .forms import SearchByPinForm
from datetime import datetime, timedelta

# Create your views here.
def vacpage(request):
    def vaccine_available(Age,Pincode,Date):
        if Age>44:
            set_age = 45
        elif Age<45 and Age>17:
            set_age = 18
        else:
            set_age = "not availabe"
        import requests
        url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin"
        headers = {
            'Host': 'cdn-api.co-vin.in',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
        }
        params = {"pincode": Pincode, "date": Date}
        resp = requests.get(url, headers=headers, params=params)
        data = resp.json()
        return get_vaccine(set_age,data["centers"])

    def get_vaccine(Age,data):
        accept = '''<a class="bg-green-500 text-white px-4 py-2 border rounded-md hover:bg-white hover:border-green-500 hover:text-black " href="https://selfregistration.cowin.gov.in">
                              Register
                            </a>'''
        booked = '''<button class="bg-red-500 text-white px-4 py-2 border rounded-md">
                              Booked
                            </button>'''
        availabe_vaccine=[]
        for hos in data:
            for session in hos["sessions"]:
                if (session["min_age_limit"] == Age):
                    if (session["available_capacity"]==0):
                        session["status"]=booked
                    elif (session["available_capacity"]>0):
                        session["status"]=accept
                    session["hos_name"]= hos["name"]
                    availabe_vaccine.append(session)
        return availabe_vaccine


    if request.method == 'POST':
        form = SearchByPinForm(request.POST)
        if form.is_valid():
            pincode = request.POST['pincode']
            age = request.POST['age']
            date = datetime.today().strftime("%d-%m-%Y")
            vaccine = vaccine_available(int(age),pincode,date)
        context = {'form':form, 'name':vaccine}
    else:
        form = SearchByPinForm()
        context = {'form':form}
        
    return render(request, 'vacpage/index.html', context)