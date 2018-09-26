from The_List import views
from django.urls import path, include, re_path

urlpatterns = [
    path('',views.HomePageView),
    path('Add/',views.AddWaala),
    path('View/',views.SeeAllPage),
    path('Add/submitBucket',views.AddPage),
    path('Delete/',views.deletePage),
    path('Delete/deleteEle',views.deleteEle),

    re_path(r'individual[?P<sel_id> \d+]/', views.indiPage),
    path('Edit/', views.editPage),

]
