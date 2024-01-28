from django.test import TestCase

from django.test import TestCase
from django.contrib.gis.geos import Point
import pytest

# from app.upload.models import Hotel

from .models import Hotel



# @pytest.mark.django_db
def test_create_shop():
    longitude = -80.191_788
    latitude = 25.761_681
    user_location = Point(longitude, latitude, srid=4326)
    Hotel.objects.create(name="Eugines",address="Kilimani",location=user_location)
    assert Hotel.objects.count==1
# Create your tests here.
