from django.shortcuts import render
from .models import City
from .services import get_weather_data


# Create your views here.
def index(request):
	if request.method == 'POST':
		city_name = request.POST.get('city')
		weather = get_weather_data(city_name)

		if weather:
			city = City.objects.create(name=city_name)
			context ={'city':city, 'weather' : weather}
			return render(request, 'weather/weather.html', context)
		else:
			error_message = 'Failed to fetch weather data.Please try again.'
			return render(request, 'weather/index.html',{'error_message': error_message})
	return render(request, 'weather/index.html')
