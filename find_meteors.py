import math
import requests

def calc_dist(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    h = math.sin((lat2 - lat1)/2) **2 + \
    math.cos(lat1) * \
    math.cos(lat2) * \
    math.sin( (lon2 - lon1) / 2 ) ** 2

    return 6372.8 * 2 * math.asin(math.sqrt(h))

def get_dist(m):
    return m.get('distance',math.inf)

if __name__ == '__main__':
    resp = requests.get('https://data.nasa.gov/resource/gh4g-9sfh.json')
    meteors = resp.json()
    my_loc = (-37.813629, 144.963058)

    for m in meteors:
        if 'reclat' not in m or 'reclong' not in m: continue
        m['distance'] = calc_dist(float(m['reclat']),
                                float(m['reclong']),
                                my_loc[0],
                                my_loc[1])


    meteors.sort(key = get_dist)
    print(meteors[0:10])
