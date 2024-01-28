from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.contrib.gis.geos import Point

from .models import Hotel


def image_upload(request):
    if request.method == "POST" and request.FILES["image_file"]:
        image_file = request.FILES["image_file"]
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        image_url = fs.url(filename)
        print(image_url)
        
        print(shop1)
        
        return render(request, "upload.html", {
            "image_url": image_url
        })
    return render(request, "upload.html")
