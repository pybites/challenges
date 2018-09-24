# ===============================================================
# Author: Rodolfo Ferro Pérez
# Email: ferro@cimat.mx
# Twitter: @FerroRodolfo
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script was originally created by Rodolfo Ferro. Any
# explicit usage of this script or its contents is granted
# according to the license provided and its conditions.
# ===============================================================

from shapely.geometry import Point
from geopandas import GeoDataFrame
from geojsonio import display
import pandas as pd
import googlemaps
import geocoder

# You might need to add your tokens to this file...
from credentials import *


class geo_app():
    """
    Geolocation application class to interact with DisAtBot, making
    him able to access and append data from the report database.
    """

    # Google Maps API authentication
    gmaps = googlemaps.Client(key=maps_token)

    def __init__(self, filename="../data/database.csv"):
        # Read data:
        self.data = pd.read_csv(filename)

        # Set a name to our data:
        self.name = "DisAtBot - Report database"

    def append_data(self, lat, lon):
        """
        Function to allow DisAtBot to append data to db.
        """
        n = len(self.data)
        lat_long = pd.DataFrame([[n, lat, lon]], columns=['ID', 'Lat', 'Long'])
        self.data = self.data.append(lat_long, ignore_index=True)
        self.data.to_csv("../data/database.csv")
        return

    def latlong_to_coords(self, filename=None, tags=None):
        """
        If we have the latitude and longitude, compute
        (lat, long) coordinates using geocoder.
        """
        self.data['Coordinates'] = [
            Point(xy) for xy in zip(self.data.Long, self.data.Lat)]
        return

    def get_geo(self):
        return(list(self.data['Coordinates']))

    def get_ID(self):
        return self.data.ID

    def get_gdf(self):
        crs = {'init': 'epsg:4326'}
        return GeoDataFrame(self.get_ID(), crs=crs, geometry=self.get_geo())

    def visualize(self):
        geovis = self.get_gdf()
        display(geovis.to_json())


if __name__ == "__main__":
    report_map = geo_app()
    # report_map.append_data(1,1)
    report_map.latlong_to_coords()
    report_map.visualize()
