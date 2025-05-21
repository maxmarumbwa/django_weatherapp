from django.shortcuts import render


# Createf your views here.
def home(request):
    import json
    import requests

    api_request = requests.get(
        "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=5269525E-87B5-47A7-875C-C8D9FA5278A9"
    )
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."

    return render(request, "home.html", {"api": api})


def about(request):
    return render(request, "about.html", {})
