from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Daily
from .forms import DailyForm

# Create your views here.
def index(request):
	daily_list=Daily.objects.order_by('id')
	form = DailyForm()
	context = {'daily_list': daily_list, 'form': form}

	return render(request, 'daily_tasks/index.html', context)


@require_POST
def addDaily(request):
	form = DailyForm(request.POST)
	if form.is_valid():
		new_daily=Daily(text=request.POST['text'])
		new_daily.save()

	return redirect('index')

def completeDaily(request, daily_id):
    daily = Daily.objects.get(pk=daily_id)
    daily.complete = True
    daily.save()
    return redirect('index')


def deleteComplete(request):
	Daily.objects.filter(complete__exact=True).delete()

	return redirect('index')

def deleteAll(request):
	Daily.objects.all().delete()

	return redirect('index')