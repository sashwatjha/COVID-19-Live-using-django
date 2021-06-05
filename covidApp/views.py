import requests
from django.shortcuts import render

# Create your views here.

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "1a911ae2a4msh9602f4244feb758p1b68c4jsn0cc1b8b42ec4",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers).json()


def helloworld(request):
    limit = int(response['results'])
    countrylist = []
    for x in range(0, limit):
        countrylist.append(response['response'][x]['country'])
    countrylist = sorted(countrylist)
    if request.method == "POST":
        selectcountry = request.POST['selectCountry']
        if selectcountry != "none":
            for x in range(0, limit):
                if selectcountry == response['response'][x]['country']:
                    new = response['response'][x]['cases']['new']
                    active = response['response'][x]['cases']['active']
                    critical = response['response'][x]['cases']['critical']
                    recovered = response['response'][x]['cases']['recovered']
                    total = response['response'][x]['cases']['total']
                    death = int(total) - int(active) - int(recovered)
            context = {'selectcountry': selectcountry, 'list': countrylist, 'new': new, 'active': active,
                       'critical': critical, 'recovered': recovered, 'death': death, 'total': total}
            return render(request, 'index.html', context)
        if selectcountry == "none":
            context = {'selectcountry': ' ', 'list': countrylist, 'new': '-', 'active': '-',
                       'critical': '-', 'recovered': '-', 'death': '-', 'total': '-'}
            return render(request, 'index.html', context)

    context = {'selectcountry': ' ', 'list': countrylist, 'new': '-', 'active': '-',
               'critical': '-', 'recovered': '-', 'death': '-', 'total': '-'}
    return render(request, 'index.html', context)
