# _*_ coding: utf-8 _*_

"""
Define customer color maps.
"""

import numpy as np
import matplotlib as mpl
from dk_met_graphics.cmap.cm import make_cmap


def cm_precipitation_metpy():
    """
    https://unidata.github.io/python-gallery/examples/Precipitation_Map.html
    :return:
    """
    colors = [
        (1.0, 1.0, 1.0),
        (0.3137255012989044, 0.8156862854957581, 0.8156862854957581),
        (0.0, 1.0, 1.0), (0.0, 0.8784313797950745, 0.501960813999176),
        (0.0, 0.7529411911964417, 0.0),
        (0.501960813999176, 0.8784313797950745, 0.0), (1.0, 1.0, 0.0),
        (1.0, 0.6274510025978088, 0.0),
        (1.0, 0.0, 0.0), (1.0, 0.125490203499794, 0.501960813999176),
        (0.9411764740943909, 0.250980406999588, 1.0),
        (0.501960813999176, 0.125490203499794, 1.0),
        (0.250980406999588, 0.250980406999588, 1.0),
        (0.125490203499794, 0.125490203499794, 0.501960813999176),
        (0.125490203499794, 0.125490203499794, 0.125490203499794),
        (0.501960813999176, 0.501960813999176, 0.501960813999176),
        (0.8784313797950745, 0.8784313797950745, 0.8784313797950745),
        (0.9333333373069763, 0.8313725590705872, 0.7372549176216125),
        (0.8549019694328308, 0.6509804129600525, 0.47058823704719543),
        (0.6274510025978088, 0.42352941632270813, 0.23529411852359772),
        (0.4000000059604645, 0.20000000298023224, 0.0)]
    return mpl.colors.ListedColormap(colors, 'precipitation')


def cm_precipitation_nws(atime=24):
    """
    http://jjhelmus.github.io/blog/2013/09/17/plotting-nsw-precipitation-data/

    :param atime: accumulative time period.
    :return: colormap function, normalization boundary.
    """

    if atime == 1:
        clevs = [0.01, 1, 2, 3, 4, 6, 8, 10, 15, 20, 30, 40, 60, 80, 100]
    elif atime == 3:
        clevs = [0.01, 1, 2, 3, 4, 6, 8, 10, 15, 20, 30, 40, 60, 80, 100]
    elif atime == 6:
        clevs = [0.01, 1, 3, 5, 10, 15, 20, 25, 30, 40, 50, 60, 80, 100, 120]
    else:
        clevs = [0.1, 2.5, 5, 10, 15, 20, 25, 30, 40, 50, 75, 100, 150, 200, 250]
    colors = ["#04e9e7", "#019ff4", "#0300f4", "#02fd02",
              "#01c501", "#008e00", "#fdf802", "#e5bc00",
              "#fd9500", "#fd0000", "#d40000", "#bc0000",
              "#f800fd", "#dd1c77", "#9854c6"]
    cmap, norm = mpl.colors.from_levels_and_colors(clevs, colors, extend='max')
    return cmap, norm


def cm_rain_nws(atime=24, pos=None):
    """
    Rainfall color map.

    Keyword Arguments:
        atime {int} -- [description] (default: {24})
        pos {[type]} -- specify the color position (default: {None})
    """

    # set colors
    _colors = [
        [144, 238, 144], [0, 127, 0], [135, 206, 250],
        [0, 0, 255], [255, 0, 255], [127, 0, 0]
    ]
    _colors = np.array(_colors)/255.0
    if pos is None:
        if atime == 24:
            _pos = [0.1, 10, 25, 50, 100, 250]
        elif atime == 6:
            _pos = [0.1, 4, 13, 25, 60, 120]
        else:
            _pos = [0.1, 2, 7, 13, 30, 60]
    else:
        _pos = pos
    cmap, norm = mpl.colors.from_levels_and_colors(_pos, _colors, extend='max')
    return cmap, norm


def cm_qpf_nws(atime=24, pos=None):
    """
    Quantitative Precipitation Forecasts color map.

    Keyword Arguments:
        atime {int} -- [description] (default: {24})
        pos {[type]} -- specify the color position (default: {None})
    """

    # set colors
    _colors = ["#FFFFFF", "#BABABA", "#A6A1A1", "#7E7E7E", "#6C6C6C",
               "#B2F8B0", "#94F397", "#56EE6C", "#2EB045", "#249C3B", 
               "#2562C6", "#347EE4", "#54A1EB", "#94CEF4", "#B2EEF6", 
               "#FDF8B2", "#FDE688", "#FDBC5C", "#FD9E42", "#FB6234",
               "#FB3D2D", "#DD2826", "#BA1B21", "#9F1A1D", "#821519",
               "#624038", "#88645C", "#B08880", "#C49C94", "#F0DAD1",
               "#CBC4D9", "#A99CC1", "#9687B6", "#715C99", "#65538B",
               "#73146F", "#881682", "#AA19A4", "#BB1BB5", "#C61CC0",
               "#D71ECF"]

    # set precipitation accumultated time
    if pos is None:
        if atime == 24:
            _pos = np.concatenate((
                np.array([0, 0.1, 0.5, 1]), np.arange(2.5, 25, 2.5),
                np.arange(25, 50, 5), np.arange(50, 150, 10),
                np.arange(150, 475, 25)))
        elif atime == 6:
            _pos = np.concatenate(
                (np.array([0, 0.1, 0.5]), np.arange(1, 4, 1),
                 np.arange(4, 13, 1.5), np.arange(13, 25, 2),
                 np.arange(25, 60, 2.5), np.arange(60, 105, 5)))
        else:
            _pos = np.concatenate(
                (np.array([0, 0.01, 0.1]), np.arange(0.5, 2, 0.5),
                 np.arange(2, 8, 1), np.arange(8, 20, 2),
                 np.arange(20, 55, 2.5), np.arange(55, 100, 5)))
    else:
        _pos = pos

    # construct color map and normalized boundary
    cmap, norm = mpl.colors.from_levels_and_colors(_pos, _colors, extend='max')
    return cmap, norm


def cm_sleet_nws(atime=24, pos=None):
    """
    Sleet color map.

    Keyword Arguments:
        atime {int} -- [description] (default: {24})
        pos {[type]} -- specify the color position (default: {None})
    """

    # set colors
    _colors = [
        [253, 216, 213], [251, 174, 185], [247, 109, 163],
        [211, 41, 146], [146, 1, 122], [81, 0, 108]
    ]
    _colors = np.array(_colors)/255.0
    if pos is None:
        if atime == 24:
            _pos = [0.1, 10, 25, 50, 100, 250]
        elif atime == 6:
            _pos = [0.1, 4, 13, 25, 60, 120]
        else:
            _pos = [0.1, 2, 7, 13, 30, 60]
    else:
        _pos = pos
    cmap, norm = mpl.colors.from_levels_and_colors(_pos, _colors, extend='max')
    return cmap, norm


def cm_snow_nws(atime=24, pos=None):
    """
    Snowfall color map.

    Keyword Arguments:
        atime {int} -- [description] (default: {24})
        pos {[type]} -- specify the color position (default: {None})
    """

    # set colors
    _colors = [
        [234, 234, 234], [200, 200, 200], [154, 154, 154],
        [108, 108, 108], [58, 58, 58], [6, 6, 6]
    ]
    _colors = np.array(_colors)/255.0
    if pos is None:
        if atime == 24:
            _pos = [0.1, 2.5, 5, 10, 20, 30]
        elif atime == 6:
            _pos = [0.1, 1, 3, 5, 10, 15]
        else:
            _pos = [0.1, 1, 2, 4, 8, 12]
    else:
        _pos = pos
    cmap, norm = mpl.colors.from_levels_and_colors(_pos, _colors, extend='max')
    return cmap, norm


def cm_precipitation_type_nws(pos=None):
    """
    Precipitation type color map.

    Keyword Arguments:
        pos {[type]} -- specify the color position (default: {None})
    """
    _colors = [
        '#FFFFFF', '#4169E1', '#DC143C', '#708090', '#228B22',
        '#EE82EE', '#FFD700']
    # '无降水', '雨', '冻雨', '纯雪', '湿的雪', '雨夹雪', '冰粒'
    if pos is None:
        _pos = [0, 1, 3, 5, 6, 7, 8]
    else:
        _pos = pos
    cmap, norm = mpl.colors.from_levels_and_colors(_pos, _colors, extend='max')
    return cmap, norm


def cm_qsf_nws(atime=24, pos=None):
    """
    Quantitative Snow Forecasts color map.

    Keyword Arguments:
        atime {int} -- [description] (default: {24})
        pos {[type]} -- specify the color position (default: {None})
    """

    # set colors
    _colors = [
        '#BBBBBB', '#949494', '#6D6D6D', '4F4F52', '#97D0F6',
        '#76B5FA', '#50A5F1', '#4097EC', '2F7FE4', '#256AE5',
        '#1C64CA', '#155BBB', '#400A80', '4F0687', '#5A0888',
        '#6A0785', '#860C83', '#9F0F81', 'C9117C', '#C9117C',
        '#E31B73', '#E31B73', '#F33E96', 'FC5DAD', '#FD6CB1',
        '#F883BA', '#ED8EBF', '#EC93C5', 'EA9ACA', '#D7A8D1',
        '#D3B0D3', '#BFC6DC', '#B3D4E8', 'A5E4E9', '#9BEFF0',
        '#92F9F7', '#90F2F0', '#7ED9D8', '76B5C6', '#6FBBC3',
        '#7DB5C4', '#7FB2C6', '#89B1CB', '88ABC8', '#8CA8CB',
        '#91A8D3', '#92A8CF', '#95A0DB', '98A3D4', '#A19DDE',
        '#A39CD9', '#A99CD2', '#AB95E7', 'AF95ED', '#B394E3',
        '#BA8DE8', '#BA90E8', '#BF8DEC']

    # set precipitation accumultated time
    if pos is None:
        if atime == 24:
            _pos = np.concatenate((
                np.array([0.1]), np.arange(0.5, 15, 0.5),
                np.arange(15, 43, 1)))
        elif atime == 6:
            _pos = np.concatenate((
                np.array([0.1]), np.arange(0.5, 20, 0.5),
                np.arange(20, 38, 1)))
        else:
            _pos = np.concatenate((
                np.array([0.01]), np.arange(0.5, 25, 0.5),
                np.arange(25, 33, 1)))
    else:
        _pos = pos

    # construct color map and normalized boundary
    cmap, norm = mpl.colors.from_levels_and_colors(_pos, _colors, extend='max')
    return cmap, norm


def cm_snow_depth_nws(pos=None):
    """
    Snow depth color map.

    Keyword Arguments:
        pos {[type]} -- specify the color position (default: {None})
    """
    _colors = [
        '#FFFFFF', '#E0E0E0', '#C6C6C6', '#ADADAD', '#949494',
        '#A8E6F0', '#72BDD4', '#3F96B7', '#126F9C', '#0C47AA',
        '#2D63B6', '#4F80C3', '#749ECF', '#99BCDC', '#BFDAE9',
        '#C7ABD7', '#BF93CE', '#B77DC4', '#AE66BC', '#A650B2',
        '#9E3AA9', '#851547', '#942359', '#A4326C', '#B3427E',
        '#C35191', '#D462A4', '#E9A5B5', '#E69A9F', '#E48E8A',
        '#E18175', '#DF7660', '#DC6A4D', '#DA8056', '#DF946C',
        '#E4A781', '#EABB98', '#F0CFB0', '#F5E4C6', '#FAF8DE']
    if pos is None:
        _pos = np.concatenate((
            np.array([0, 0.1, 0.5]), np.arange(1, 12, 1),
            np.arange(12, 60, 4), np.arange(60, 100, 10),
            np.arange(100, 1100, 100)))

    # construct color map and normalized boundary
    cmap, norm = mpl.colors.from_levels_and_colors(_pos, _colors, extend='max')
    return cmap, norm


def cm_snow_density_nws(pos=None):
    """
    Snow density color map.

    Keyword Arguments:
        pos {[type]} -- specify the color position (default: {None})
    """
    _colors = [
        '#FFFFFF', '#E0E0E0', '#C6C6C6', '#ADADAD', '#949494',
        '#A8E6F0', '#72BDD4', '#3F96B7', '#126F9C', '#0C47AA',
        '#2D63B6', '#4F80C3', '#749ECF', '#99BCDC', '#BFDAE9',
        '#C7ABD7', '#BF93CE', '#B77DC4', '#AE66BC', '#A650B2',
        '#9E3AA9', '#851547', '#942359', '#A4326C', '#B3427E',
        '#C35191', '#D462A4', '#E9A5B5', '#E69A9F', '#E48E8A',
        '#E18175', '#DF7660', '#DC6A4D', '#DA8056', '#DF946C',
        '#E4A781', '#EABB98', '#F0CFB0', '#F5E4C6', '#FAF8DE']
    if pos is None:
        _pos = np.concatenate((
            np.array([0, 0.1, 0.5]), np.arange(1, 12, 1),
            np.arange(12, 60, 4), np.arange(60, 100, 10),
            np.arange(100, 1100, 100)))

    # construct color map and normalized boundary
    cmap, norm = mpl.colors.from_levels_and_colors(_pos, _colors, extend='max')
    return cmap, norm


def cm_temperature_nws(pos=None):
    """
    Construct 2m temperature color maps.

    Keyword Arguments:
        pos {[type]} -- specify the color position (default: {None})

    >>> ax.pcolormesh(x, y, data, cmap=cm_temperature_nws(), vmin=-45, vmax=45)
    """
    _colors = [
        [61, 2, 57], [250, 0, 252], [9, 0, 121], [94, 157, 248], 
        [46, 94, 127], [6, 249, 251], [254, 254, 254], [32, 178, 170],
        [11, 244, 11], [0, 97, 3], [173, 255, 47], [254, 254, 0],
        [255, 140, 0], [255, 99, 61], [90, 3, 3], [253, 253, 253]]
    if pos is None:
        _pos = np.array([
            -45, -30, -20, -10, -5, 0, 0, 5, 5, 10, 20, 20, 30, 30, 40, 45])
    else:
        _pos = pos
    return make_cmap(_colors, position=_pos, rgb=True)


def cm_temperature_trend_nws(pos=None):
    """
    Construct temperature trend color map.
    
    Keyword Arguments:
        pos {[type]} -- specify the color position (default: {None})
    """
    
    _colors = [
        '#Fcdcf7', '#F795E7', '#F378E0', '#F059D8', '#EC2ACE',
        '#C022A8', '#A01F8C', '#811C70', '#6B195E', '#54154B',
        '#342799', '#402FA8', '#4A40BB', '#6E60D0', '#7E6EDF',
        '#9D89F3', '#BCB0F7', '#DDDDFE', '#DDDDFE', '#B2F8B0',
        '#94F397', '#78F384', '#56EE6C', '#42CE5A', '#2EB045',
        '#249C3B', '#2562C6', '#2C6CDF', '#4492EB', '#54A1EB',
        '#78B5F2', '#94CEF4', '#B2EEF6', '#FFFFFF', '#FDFCFC',
        '#FDFFB1', '#FDE099', '#FDC083', '#FDA56D', '#FD8858',
        '#FC6D46', '#FB5337', '#E5372A', '#CD3126', '#B72B22',
        '#A0251F', '#8C1F1B', '#761A18', '#621215', '#4E0F12',
        '#624039', '#74524A', '#88645C', '#9C766E', '#B08880',
        '#C49C94', '#DDBAB2', '#EEDAD0', '#F8EEE4', '#FDE4E4',
        '#FDC4C6', '#F29E9E', '#E28082', '#DD6466', '#DD6466',
        '#BF4345', '#AE3335']
    if pos is None:
        _pos = np.concatenate((
            np.arange(-42, -18, 2), np.arange(-18, -3, 1),
            np.arange(-3, 0, 0.5),  np.arange(0.5, 3, 0.5),
            np.arange(3, 18, 1), np.arange(18, 43, 2)))

    # construct color map and normalized boundary
    cmap, norm = mpl.colors.from_levels_and_colors(
        _pos, _colors, extend='both')
    return cmap, norm


def cm_wind_speed_nws(pos=None):
    """
    Construct 10m wind speed color maps.

    Keyword Arguments:
        pos {[type]} -- specify the color position (default: {None})
    """
    _colors = [
        [255, 255, 255], [99, 99, 99], [28, 99, 207], [177, 238, 239],
        [60, 206, 77], [197, 254, 189], [251, 249, 173], [163, 14, 19],
        [95, 61, 54], [221, 186, 177], [241, 218, 209], [209, 83, 80]
    ]
    if pos is None:
        _pos = np.array(
            [0, 3.6, 3.6, 10.8, 10.8, 17.2, 17.2, 24.5, 24.5, 32.7, 32.7, 42])
    else:
        _pos = pos
    return make_cmap(_colors, position=_pos, rgb=True)


def cm_relative_humidity_nws(pos=None):
    """
    Construct 10m relative humidity color maps.
    
    Keyword Arguments:
        pos {[type]} -- specify the color position (default: {None})
    """
    _colors = [
        [99, 68, 46], [125, 84, 54], [153, 98, 62], [168, 115, 79],
        [181, 137, 99], [206, 178, 148], [218, 198, 178], [221, 215, 198],
        [185, 199, 170], [170, 193, 156], [135, 187, 138], [108, 165, 145],
        [79, 105, 143], [79, 98, 143], [157, 24, 177], [121, 20, 97]
    ]
    _colors = np.array(_colors)/255.0
    if pos is None:
        _pos = [0, 1, 5, 10, 20, 30, 40, 50, 60, 65, 70, 75, 80, 85, 90, 99]
    else:
        _pos = pos

    # construct color map and normalized boundary
    cmap, norm = mpl.colors.from_levels_and_colors(
        _pos, _colors, extend='max')
    return cmap, norm


def cm_cloud_cover_nws(pos=None):
    """
    Construct total cloud cover color maps.

    Keyword Arguments:
        pos {[type]} -- specify the color position (default: {None})
    """
    _colors = [
        '#000000', '#3C3C3C', '#7C7C7C', '#BFBFBF', '#E3E3E3', '#FFFFFF']
    if pos is None:
        _pos = [0, 25, 50, 75, 90, 100]
    else:
        _pos = pos

    return make_cmap(_colors, position=_pos, hex=True)


def cm_visibility_nws(pos=None):
    """
    Construct visibility color map.

    Keyword Arguments:
        pos {[type]} -- specify the color position (default: {None})
    """
    _colors = [
        '#31007E', '#0032B3', '#007DFF', '#00BDFF', 
        '#FF2290', '#FFAED7', '#FFFF00', '#FF9800', 
        '#17D78B', '2AA92A', '53FF00']
    if pos is None:
        _pos = [0, 0.05, 0.2, 0.5, 1, 2.5, 5, 10, 20, 30, 40]
    else:
        _pos = pos

    # construct color map and normalized boundary
    cmap, norm = mpl.colors.from_levels_and_colors(
        _pos, _colors, extend='max')
    return cmap, norm


def cm_mslp_nws(pos=None):
    """
    Constrcut mean sea level pressure color map.

    Keyword Arguments:
        pos {[type]} -- specify the color position (default: {None})
    """
    _colors = [
        '#FD90EB', '#EB78E5', '#EF53E0', '#F11FD3', '#F11FD3', '#A20E9B',
        '#880576', '#6D0258', '#5F0853', '#2A0DA8', '#2F1AA7', '#3D27B4',
        '#3F3CB6', '#6D5CDE', '#A28CF9', '#C1B3FF', '#DDDCFE', '#1861DB',
        '#206CE5', '#2484F4', '#52A5EE', '#91D4FF', '#B2EFF8', '#DEFEFF',
        '#C9FDBD', '#91F78B', '#53ED54', '#1DB31E', '#0CA104', '#FFF9A4',
        '#FFE27F', '#FAC235', '#FF9D04', '#FF5E00', '#F83302', '#E01304',
        '#A20200', '#603329', '#8C6653', '#B18981', '#DDC0B3', '#F8A3A2',
        '#DD6663', '#CA3C3B', '#A1241D', '#6C6F6D', '#8A8A8A', '#AAAAAA',
        '#C5C5C5', '#D5D5D5', '#E7E3E4']
    if pos is None:
        _pos = np.arange(940, 1067.5, 2.5)
    else:
        _pos = pos

    # construct color map and normalized boundary
    cmap, norm = mpl.colors.from_levels_and_colors(
        _pos, _colors, extend='max')
    return cmap, norm


def cm_height_nws(start=488, step=2.5, pos=None):
    """
    Construct geopotential height color map (44 colors).
    
    Keyword Arguments:
    start {int} -- start value (default: {24})
    step {int} -- step value (default: {2})
    pos {numpy array} -- specify the color position (default: {None})
    
    Returns:
        matplotlib.colors.ListedColormap -- color map.
    """
    
    _colors = [
        '#333637', '#50514C', '#676467', '#888888', '#9F9F9F',
        '#B3ADB3', '#C5C5C3', '#DBDBE6', '#B2AEE5', '#7C70D2',
        '#6E60CF', '#483FB8', '#32289A', '#2C6CDF', '#347DE2',
        '#4493EB', '#54A1EB', '#95CFF5', '#B2F8B0', '#95F398',
        '#56EC6B', '#2EB146', '#249D3B', '#624039', '#74524A',
        '#89645C', '#9A736A', '#AE8781', '#C49C94', '#DDBBB3',
        '#FDF9B3', '#FDE788', '#FDBD5C', '#FD9F43', '#FB6234',
        '#FB3D2D', '#DD2826', '#BB1B21', '#9F181D', '#F29F9F',
        '#E38183', '#D55B58', '#CF5251', '#C54043']
    if pos is not None:
        _pos = pos
    else:
        _pos = np.arange(len(_colors)) * step + start

    # construct color map and normalized boundary
    cmap, norm = mpl.colors.from_levels_and_colors(
        _pos, _colors, extend='max')
    return cmap, norm


def cm_high_wind_speed_nws(start=6, step=1.5, pos=None):
    """
    Construct high wind speed color map (32 colors).
    
    Keyword Arguments:
        start {int} -- start value (default: {24})
        step {int} -- step value (default: {2})
        pos {numpy array} -- specify the color position (default: {None})
            like pos = np.concatenate((np.arange(4,22,1), np.arange(22,38,2),
                                       np.arange(38,62,4)))  # 925
                 pos = np.concatenate((np.arange(6,24,1), np.arange(24,40,2),
                                       np.arange(40,64,4)))  # 850
                 pos = np.concatenate((np.arange(8,26,1), np.arange(26,42,2),
                                       np.arange(42,68,4)))  # 700
                 pos = np.concatenate((np.arange(18,36,1), np.arange(36,50,2),
                                       np.arange(50,85,5)))  # 500
                 pos = np.concatenate((np.arange(24,48,2),
                                       np.arange(48,128,4)))  # 200
    
    Returns:
        matplotlib.colors.ListedColormap -- color map.
    """

    _colors = [
        '#DEEBF7', '#B7EBFA', '#91D1F5', '#52A2EF', '#2F80E2',
        '#1F61D0', '#41AB5D', '#3ECE4D', '#54EE60', '#76F678',
        '#B4F8B1', '#C6FDBC', '#FDF6B2', '#FDE687', '#F7BD50',
        '#FC6123', '#FB5E24', '#F73A1E', '#E21D19', '#C11015',
        '#9D0E11', '#633B33', '#785144', '#8C645A', '#B48A82',
        '#DFBDB5', '#F1DBD4', '#FDC4C5', '#F0A1A4', '#E67F81',
        '#DB6464', '#D75052']
    if pos is not None:
        _pos = pos
    else:
        _pos = np.arange(len(_colors)) * step + start

    # construct color map and normalized boundary
    cmap, norm = mpl.colors.from_levels_and_colors(
        
        _pos, _colors, extend='max')
    return cmap, norm


def cm_vertical_velocity_nws(pos=None):
    """
    Construct vertical velocity color map.

    Keyword Arguments:
        pos {numpy array} -- specify the color position (default: {None})
    """

    _colors = [
        '#9D0001', '#C90101', '#F10202', '#FF3333', '#FF8585',
        '#FFBABA', '#FEDDDD', '#FFFFFF', '#E1E1FF', '#BABAFF',
        '#8484FF', '#2C2CF7', '#0404F1', '#0101C8', '#020299']
    if pos is not None:
        _pos = pos
    else:
        _pos = [
            -30, -20, -10, -5, -2.5, -1, -0.5,
            0.5, 1, 2.5, 5, 10, 20, 30]
    
    # construct color map and normalized boundary
    cmap, norm = mpl.colors.from_levels_and_colors(
        _pos, _colors, extend='both')
    return cmap, norm


def cm_precipitable_water_nws(pos=None):
    """
    Construct precipitable water color map.
    
    Keyword Arguments:
        pos {[type]} -- specify the color position (default: {None})
    """

    _colors = [
        '#C5C5C5', '#B5B5B5', '#A1A1A1', '#8B8B8B', '#787878',
        '#636363', '#505050', '#3B3B3B', '#5B431F', '#6D583B',
        '#866441', '#9C7B46', '#B28C5D', '#CA9D64', '#D8AC7D',
        '#B9B5FF', '#A7A8E1', '#989ACD', '#8686C6', '#6B6CA4',
        '#5A5B91', '#474880', '#016362', '#1D6C59', '#2C774E',
        '#398545', '#589A39', '#6FA720', '#8BB41A', '#A29E54',
        '#AEAD43', '#C4C732', '#D9DB18', '#F0EC11', '#E96F57',
        '#C55645', '#B04035', '#9D2527', '#8A121C', '#7B0007',
        '#7A0076', '#8E0096', '#AE00B8', '#C300C0', '#E200E1',
        '#A002DB', '#7901DD', '#6201DE', '#3C00DC', '#2500D9',
        '#0028DD', '#004ED6', '#0571E0', '#0C98E7', '#02B8DD']
    if pos is not None:
        _pos = pos
    else:
        _pos = np.concatenate((np.arange(25), np.arange(26, 86, 2)))
   
    # construct color map and normalized boundary
    cmap, norm = mpl.colors.from_levels_and_colors(
        _pos, _colors, extend='both')
    return cmap, norm


def cm_specific_humidity_nws(pos=None):
    """
    Construct specific humidity color map.

    Keyword Arguments:
        pos {[type]} -- specify the color position (default: {None})
    """

    _colors = [
        '#FFFFB3', '#463F35', '#F3F1D7', '#E5F4E6', '#124E19',
        '#62A1AC', '#1A2F2E', '#656596', '#302361', '#D3B8DA',
        '#845574']
    if pos is not None:
        _pos = pos
    else:
        _pos = [0, 4, 8, 8, 12, 12, 16, 16, 20, 20, 24]

    return make_cmap(_colors, position=_pos, hex=True)


def cm_high_temperature_nws(pos=None):
    """
    Construct high temperature color map.

    Keyword Arguments:
        pos {[type]} -- specify the color position (default: {None})
    """

    _colors = [
        '#EDC4EF', '#F25AB1', '#F31E83', '#EA2283', '#C6478D',
        '#BD68B4', '#6C429B', '#CACEEB', '#484BB0', '#387DF0',
        '#1FFBFD', '#66EAAE', '#159929', '#FDFE89', '#F09450',
        '#BF231B', '#A83750', '#E27185', '#F5B3F0', '#9550AA']
    if pos is not None:
        _pos = pos
    else:
        _pos = [-60, -50, -40, -35, -30, -25, -20, -15, -10, -5, 0,
                0, 5, 10, 15, 20, 25, 30, 35, 40]

    return make_cmap(_colors, position=_pos, hex=True)


def cm_high_thermal_temperature_nws(pos=None):
    """
    Construct high thermal temperature color map.

    Keyword Arguments:
        pos {[type]} -- specify the color position (default: {None})
    """

    _colors = [
        '#996035', '#F2DACD', '#1E6EC8', '#AAFFFF', '#01F6E2',
        '#00FF00', '#03E19F', '#26BC0D', '#88DB07', '#FFFF13',
        '#FFE100', '#264CFF', '#FF7F00', '#FF0000', '#B5003C',
        '#7F0067', '#9868B4', '#F2EBF5', '#ED00ED']
    if pos is not None:
        _pos = pos
    else:
        _pos = [270, 280, 285, 290, 295, 300, 305,
                310, 315, 320, 330, 335, 340, 345, 350,
                355, 360]

    # construct color map and normalized boundary
    cmap, norm = mpl.colors.from_levels_and_colors(
        _pos, _colors, extend='both')
    return cmap, norm


def cm_cape_nws(pos=None):
    """
    Construct CAPSE color map.

    Keyword Arguments:
        pos {[type]} -- specify the color position (default: {None})
    """

    _colors = [
        '#FFFFFF', '#1E68E4', '#479BEC', '#22FBFB', '#1CD78B',
        '#1CAE30', '#52C636', '#BAEA41', '#FEFF4A', '#FA8D2C',
        '#FD3B4B', '#A40F4D', '#5A0B76', '#F1EBF5']
    if pos is not None:
        _pos = pos
    else:
        _pos = np.array([
            0, 100, 150, 500, 900, 1300, 1500, 1800,
            2000, 2850, 3600, 3900, 4200, 4950])
    
    return make_cmap(_colors, position=_pos, hex=True)

