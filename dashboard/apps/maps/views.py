from email import message
from time import time

from numpy import tile
from apps.maps.models import Maps

# Maps Library Import ---------------------------------------------- #
from django.shortcuts import redirect, render
from django.views.generic import TemplateView 

#folium
import folium
from folium import plugins
import branca.colormap as cm

from apps.maps.forms import MapForm
from django.http import HttpResponse
from django import forms

import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def Map(request):
    figure = folium.Figure()
    m = folium.Map(
        location=[35, -125],
        zoom_start=6,
        height=900
    )

    m.add_to(figure)
    draw = plugins.Draw(export=False)
    draw.add_to(m)

    minimap = plugins.MiniMap(toggle_display=True, tile_layer="Stamen Toner")
    minimap.add_to(m)

    formatter = "function(num) {return L.Util.formatNum(num, 3) + ' º ';};"
    plugins.MousePosition(
        position="topright",
        separator=" | ",
        empty_string="NaN",
        lng_first=True,
        num_digits=20,
        prefix="Coordinates:",
        lat_formatter=formatter,
        lng_formatter=formatter,
    ).add_to(m)

    figure.render()
    form = MapForm()
    #form.fields['coords'].widget = forms.HiddenInput()
    return render(request, 'maps/plotmap.html', {"map": figure, "form" : form})