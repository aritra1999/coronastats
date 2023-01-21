from django.shortcuts import render
import requests

def home_view(request):
    r1 = requests.get('https://api.covid19india.org/states_daily.json')
    data = r1.json()

    # data_confirmed = []
    # data_recovered = []
    # data_deceased = []
    # dates = []
    #
    # for each_day in data["states_daily"]:
    #     if each_day["status"] == "Confirmed":
    #         data_confirmed.append(each_day["wb"])
    #         dates.append(each_day["date"])
    #     if each_day["status"] == "Recovered":
    #         data_recovered.append(each_day["wb"])
    #     if each_day["status"] == "Deceased":
    #         data_deceased.append(each_day["wb"])



    context = {
        'title': 'Home',
        # 'data_confirmed': data_confirmed,
        # 'data_recovered': data_recovered,
        # 'data_deceased': data_deceased,
        # 'dates': dates
    }
    return render(request, 'home/home.html', context)
