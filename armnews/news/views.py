from django.shortcuts import render
from models import News
import explore

def index(request):
	qs = News.objects.all()
	# explore.stop()
	return render(request, 'news/home.html',{'items': qs})
	# {'data': sorted(results_dict.items())})