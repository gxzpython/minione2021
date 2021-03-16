from django.urls import path

from . import views
###############################################################
app_name="society"  #################remember this ############
###############################################################
urlpatterns = [
    path('group/', views.group,name='group'),
    path('event/', views.event, name ='event'),
    path('people/', views.people, name ='people'),
    path('group/<int:group_id>/',views.group_detail,name='group_detail'),
    path('event/<int:event_id>/',views.event_detail,name='event_detail'),
    path('people/<int:people_id>/',views.people_detail,name='people_detail'),

    #ex : /society/login/
    path('',views.login, name = 'login'),
    path('index/',views.index,name = 'index'),

    #ex : /society/success/
    path('success/',views.success, name = 'success')


]

