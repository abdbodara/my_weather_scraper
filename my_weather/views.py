from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import csv
from .models import guest
from .forms import guestForm
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)


def weather(request):
    page = requests.get("https://www.bbc.com/weather/1275339")
    soup = BeautifulSoup(page.text, 'html.parser')

    weather = soup.find(class_="wr-day-carousel__scrollable")

    days = weather.find_all('li')

    file_name = "weather.csv"

    f = csv.writer(open(file_name, 'w', newline=''))

    f.writerow(['Day', 'Description', 'Temperature'])

    day_data = []
    desc_data = []
    temp_data = []

    for weather in days:
        day = weather.find(class_="wr-date").get_text()

        description = weather.find(
            class_="wr-day__weather-type-description-container").get_text()

        temp = weather.find(class_="wr-day-temperature").get_text()

        day_data.append(day)
        desc_data.append(description)
        temp_data.append(temp)

        f.writerow([day, description, temp])

    payload = {
        'day': day_data,
        'desc': desc_data,
        'temp': temp_data,
    }

    contex = {'data': payload}
    return render(request, 'weather.html', contex)


def create_view(request):
    context = {}

    form = guestForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create_view.html", context)


def list_view(request):
    context = {}

    context["dataset"] = guest.objects.all()

    return render(request, "list_view.html", context)


def detail_view(request, id):
    context = {}

    context["data"] = guest.objects.get(id=id)

    return render(request, "detail_view.html", context)


def update_view(request, id):
    context = {}

    obj = get_object_or_404(guest, id=id)

    form = guestForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/list")

    context["form"] = form

    return render(request, "update_view.html", context)


def delete_view(request, id):
    context = {}

    obj = get_object_or_404(guest, id=id)

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/list")

    return render(request, "delete_view.html", context)
