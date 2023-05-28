import numpy as np
import pandas as pd

R = 6371

def deg_to_rad(degrees):
    return degrees * (np.pi/180)

## Using the Haversine Formula
def distcalculate(lat1, lon1, lat2, lon2):
    d_lat = deg_to_rad(lat1 - lat2)
    d_long = deg_to_rad(lon1 - lon2)
    a1 = np.sin(d_lat / 2) ** 2 + np.cos(deg_to_rad(lon1))
    a2 = np.cos(deg_to_rad(lat2)) * np.sin(d_long / 2) ** 2
    a = abs(a1 * a2)
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    return R * c

def items_trip(df_delivery):
    d = {}
    mask_duplicate = df_delivery['trip_id']
    for i in range(len(mask_duplicate)):
        trip_id_temp = mask_duplicate.loc[i]
        if trip_id_temp not in d.keys():
            d[trip_id_temp] = 0
        d[trip_id_temp] += 1
    for j in range(len(mask_duplicate)):
        trip_id_temp = df_delivery.loc[j, 'trip_id']
        df_delivery.loc[j, 'items_per_trip'] = d[trip_id_temp]

