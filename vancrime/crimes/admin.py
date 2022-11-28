from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django import forms
from .models import crime 

# Register your models here.

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

class CrimeAdmin(admin.ModelAdmin):
    list_display = ('cType', 'year', 'month', 'day', 'hour', 'minute','hundredBlock', 'neighbourhood', 'x', 'y' )

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request): 

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]

            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data:
                fields = x.split(",")
                created = crime.objects.update_or_create(
                    cType = fields[0],
                    year = fields[1],
                    month = fields[2],
                    day = fields[3],
                    hour = fields[4],
                    minute = fields[5],
                    hundredBlock = fields[6],
                    neighbourhood = fields[7],
                    x = fields[8],
                    y = fields[9],
                )

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

admin.site.register(crime, CrimeAdmin)