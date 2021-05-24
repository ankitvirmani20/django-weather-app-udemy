from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json
    if request.method == "POST":
       zipcode = request.POST['zipcode']
       api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+ zipcode + "&distance=25&API_KEY=6082764B-8CE5-4D5A-BEC3-AE8648E30387")
       try:
            api = json.loads(api_request.content)
       except Exception as e:
            api = "Error"
       return render(request,'home.html',{'api':api})
    

    else:	


        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=60015&distance=25&API_KEY=6082764B-8CE5-4D5A-BEC3-AE8648E30387")
    
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error"

        return render(request,'home.html',{'api':api})

def about(request):
    return render(request, 'about.html', {})
