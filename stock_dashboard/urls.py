"""
URL configuration for stock_dashboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from dashboard.views import GetData, GetQuarters, GetRevenueData, GetNetIncome, GetGrossMargin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/<int:gid>/', GetData.as_view()),
    path('quarter-data/<int:gid>/', GetQuarters.as_view()),
    path('revenue-data/<int:gid>/', GetRevenueData.as_view()),
    path('net-income-data/<int:gid>/', GetNetIncome.as_view()),
    path('gross-margin-data/<int:gid>/', GetGrossMargin.as_view()),
]
