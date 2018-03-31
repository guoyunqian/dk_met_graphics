# _*_ coding: utf-8 _*_

"""
Retrieve resource dataset.
"""

import pkg_resources
import pandas as pd
import numpy as np
from netCDF4 import Dataset


def get_nation_station_info(limit=None):
    """
    Get the national surface weather station information.

    :param limit: region limit, [lon0, lon1, lat0, lat1]

    :return: pandas data frame, weather station information, column names:
    ['province', 'ID', 'name', 'grade', 'lat', 'lon', 'alt', 'pressureAlt']
    """

    file = pkg_resources.resource_filename(
        "dk_met_graphics", "resources/stations/cma_national_station_info.dat")

    if limit is None:
        return pd.read_csv(file, dtype={"ID": np.str})
    else:
        sta_info = pd.read_csv(file, dtype={"ID": np.str})
        return sta_info.loc[
            (sta_info['lon'] >= limit[0]) & (sta_info['lon'] <= limit[1]) &
            (sta_info['lat'] >= limit[2]) & (sta_info['lat'] <= limit[3])]


def read_china_topo():
    """
    read china topography data and lon, lat topography.

    :return: {lon, lat, topo} dictionary.
    """

    # get topography filename
    filename = pkg_resources.resource_filename(
        'dk_met_graphics', "resources/topo/topo_china.nc")

    # read topo data
    fio = Dataset(filename, 'r')
    lon = fio.variables['Longitude'][:]
    lat = fio.variables['Latitude'][:]
    topo = fio.variables['topo'][:]

    # return
    return {'lon': lon, 'lat': lat, 'topo': topo}


def get_mpl_style(name):
    """Get the matplotlib style file path.
    Matplotlib stylesheets can be passed via their full path. This function
    takes a style name and returns the absolute path to the typhon stylesheet.

    refer to:
      https://github.com/nirum/mplstyle
      https://github.com/tonysyu/matplotlib-style-gallery
      http://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html

    Arguments:
        name {string} -- style file name.
    """

    return pkg_resources.resource_filename(
        'dk_met_graphics', 'resources/stylelib/'+name+'.mplstyle')
