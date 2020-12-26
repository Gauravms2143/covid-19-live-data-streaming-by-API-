from django.shortcuts import render

# Create your views here.
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "2850959111msh53c45ad03629c34p1c49b0jsn5a57b59a1882",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

# print(response)
def index(request):
    # context={"response":response}
      # Selected country
    list_of_countries=[]
    for x in range(int(response['results'])):
        list_of_countries.append(response['response'][x]['country'])
    if request.method=="POST":
        selected_country=request.POST['selected_country']
        # print(selected_country)
        for case in range(int(response['results'])):
            # print(response['response'][case]['cases'])
            if selected_country == response['response'][case]['country']:
                new=response['response'][case]['cases']['new']
                active=response['response'][case]['cases']['active']
                critical=response['response'][case]['cases']['critical']
                recovered=response['response'][case]['cases']['recovered']
                total=response['response'][case]['cases']['total']
                
                context={
                    "list_of_countries":list_of_countries,
                    "selected_country":selected_country,
                    "new":new,
                    "active":active,
                    "critical":critical,
                    "recovered":recovered,
                    "total":total
                }
                # print(context)
        return render (request,"index.html",context)

    context={'list_of_countries':list_of_countries}

  
    return render (request,"index.html",context)