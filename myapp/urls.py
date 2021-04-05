
from django.urls import path,include
from . import views

urlpatterns = [
  path('textdata',views.testfunction,name='textdata'),
  path('call',views.testfunction,name='call'),
  path('text',views.testfunction,name='text'),
  path('text1',views.testfunction,name='text1'),
  path('text2',views.testfunction,name='text2'),
  path('text3',views.testfunction,name='text3'),
  path('text4',views.formfunction,name='text4'),
  path('fb',views.testfunction,name='fb'),
  path('fb1',views.fb1function,name='fb1'),
  path('js2',views.js2function,name='js2'),
  path('jstext',views.jstextfunction,name='jstext'),
  path('cal',views.calfunction,name='cal')
  
]