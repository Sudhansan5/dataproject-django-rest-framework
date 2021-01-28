"""dataproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from company_master.views import home_view, plot_one, plot_two, plot_three,\
    plot_four, problem_one_view, problem_two_view, problem_three_view,\
    problem_four_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('plot1/', plot_one),
    path('plot2/', plot_two),
    path('plot3/', plot_three),
    path('plot4/', plot_four),
    path('problem1/', problem_one_view),
    path('problem2/', problem_two_view),
    path('problem3/', problem_three_view),
    path('problem4/', problem_four_view),

]
