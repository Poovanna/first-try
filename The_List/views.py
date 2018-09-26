from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Bucket


def HomePageView(request, **kwargs):
	return render(request, 'home.html', context=None)
def AddWaala(request, **kwargs):
	return render(request, 'add.html', context=None)
def AddPage(request, **kwargs):
	#return render(request, 'add.html', context=None)
	it=request.POST.get("item")
	ta=request.POST.get("T_Age")
	st=request.POST.get("status")
	co=request.POST.get("country")
	Buck=Bucket(item=it,target_age=ta,status=st,country=co)
	Buck.save()
	qs=Bucket.objects.all()
	return render(request, 'tabler.html', {"elements" :qs})
def deletePage(request,**kwargs):
	bu_l=Bucket.objects.all()
	to_print={
		"elements": bu_l }
	return render(request, 'Deltabler.html', to_print)
def deleteEle(request,**kwargs):
	checks=request.POST.getlist('sel')
	for i in checks:
		Bucket.objects.filter(id=i).delete()
	bu_l=Bucket.objects.all()
	to_print={
		"elements": bu_l }
	return render(request, 'tabler.html', to_print)

def SeeAllPage(request, **kwargs):
	bu_l=Bucket.objects.all()
	to_print={
		"elements": bu_l }
	return render(request, 'tabler.html', to_print)

def editPage(request, **kwargs):
	bu_l=Bucket.objects.all()
	to_print={
		"elements": bu_l }
	return render(request, 'editer.html', to_print)
def indiPage(request, sel_id):
	bu_l=Bucket.GET.filter(id=sel_id)
	to_print={
		"elements": bu_l }
	return render(request, 'tabler.html', to_print)
def SearchPage(request, **kwargs):
	#bu_l=Bucket.objects.filter("""""")
	to_print={
		"elements": bu_l }
	return render(request, 'tabler.html', to_print)
