from django.shortcuts import render
from rest_framework.authtoken.views import APIView
from rest_framework.response import Response
import requests
import csv

# Create your views here.
class GetData(APIView):

    def get(self, request, gid, *args, **kwargs):
        # URL zum Abrufen der CSV-Daten vom Blatt $AAPL
        url = f"https://docs.google.com/spreadsheets/d/1AVv0gcu6WAWd2pfD-FdbSSeMUPafb52gslGXAPa48YA/export?format=csv&gid={gid}"
    
        # Abrufen der Daten von Google Sheets
        response = requests.get(url)
        response.raise_for_status()  # Überprüfen, ob die Anfrage erfolgreich war

        # Daten decodieren und als CSV lesen
        decoded_content = response.content.decode('utf-8')
        csv_reader = csv.reader(decoded_content.splitlines(), delimiter=',')
        data_list = list(csv_reader)

        return Response(data_list)


class GetQuarters(APIView):
    def get(self, request, gid, *args, **kwargs):
        pass

class GetRevenueData(APIView):
    def get(self, request, gid, *args, **kwargs):
        pass

class GetNetIncome(APIView):
    def get(self, request, gid, *args, **kwargs):
        pass

class GetGrossMargin(APIView):
    def get(self, request, gid, *args, **kwargs):
        pass