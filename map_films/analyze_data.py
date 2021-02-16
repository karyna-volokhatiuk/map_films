'''
The module that read data and analyze it.
'''
from math import cos, sin, asin, sqrt, radians
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable
from geopy.extra.rate_limiter import RateLimiter


def reading_file(year):
    '''
    Read 'locations.list' and return dict_year_location_movie
    with keys - input years and values - lists with movies and locations.
    >>> reading_file('2015')[1]
    ['"#15SecondScare" (2015) {Who Wants to Play with the Rabbit? (#1.2)}', 'West Hills, California, USA']
    >>> reading_file('2016')[0]
    ['"#ActorsLife" (2016)', 'New York City, New York, USA']
    >>> reading_file('2012')[0]
    ['"#ByMySide" (2012)', 'Alessandria, Piedmont, Italy']
    '''
    with open('locations.list', encoding='ISO-8859-1') as data:
        data = data.readlines()
        data = data[14:2000]
    list_location_movie = []
    for line in data:
        if '('+year+')' in line:
            line = line.strip().split('\t')
            line = filter(lambda x: x != '', line)
            line = list(line)
            list_location_movie.append(
                [line[0], ' '.join(line[1:]).split(' (')[0]])
    return list_location_movie


def find_coordinates(location_name):
    '''
    Return coordinates of the location_name.
    >>> find_coordinates('Kyiv, Ukraine')
    (50.4500336, 30.5241361)
    >>> find_coordinates('Kozelnytska St, 2, Lviv')
    (49.8175526, 24.023816249632155)
    '''
    try:
        geolocator = Nominatim(user_agent="Movies")
        geocode = RateLimiter(geolocator.geocode, min_delay_seconds=0.5)
        location = geolocator.geocode(location_name)
        if location:
            return location.latitude, location.longitude
    except GeocoderUnavailable:
        pass


def find_distance(latitude_1, longitude_1, latitude_2, longitude_2):
    '''
    Return distance in kilometers between points with coordinates (latitude_1, longitude_1) and
    (latitude_2, longitude_2).
    >>> find_distance(49.83826, 24.02324, 49.66299, 24.12828)
    20.89920918101454
    >>> find_distance(58.74244, 57.75205, 55.74924, 60.72420)
    377.7318556207476
    >>> find_distance(49.83826, 24.02324, 49.83826, 24.02324)
    0.0
    '''
    latitude_1, longitude_1, latitude_2, longitude_2 = map(
        radians, [latitude_1, longitude_1, latitude_2, longitude_2])

    radius_of_earth = 6371
    half_of_dif_latitude = (latitude_2-latitude_1)/2
    half_of_dif_longitude = (longitude_2-longitude_1)/2
    squared_sin_latitude = pow(sin(half_of_dif_latitude), 2)
    squared_sin_longitude = pow(sin(half_of_dif_longitude), 2)
    haversin = squared_sin_latitude + \
        cos(latitude_1)*cos(latitude_2)*squared_sin_longitude
    return 2*radius_of_earth*asin(sqrt(haversin))


def find_ten_nearest_locations(latitude_of_user, longitude_of_user, list_location_movie):
    '''
    Return ten nearest locations to the location with coordinates
    (latitude_of_user, longitude_of_user).
    >>> find_ten_nearest_locations(49.83826, 24.02324, reading_file('2016'))[0]
    ['"#VanLifeAttila" (2016) {Novel Reading: My Memoirs (#2.14)}', 'Budapest, Hungary',\
 (47.4983815, 19.0404707), 448.8279858866552]
    >>> find_ten_nearest_locations(49.83826, 24.02324, reading_file('2015'))[0]
    ['"1945: 12 Städte, 12 Schicksale" (2015) {Braunschweig - Die Ruinen (#1.7)}', \
'Warsaw, Mazowieckie, Poland', (52.2319581, 21.0067249), 339.5482438129518]
    '''
    ten_nearest_locations = []
    for movie in list_location_movie:
        location = movie[1].split('(')[0]
        if find_coordinates(location):
            latitude_and_longitude = find_coordinates(location)
            distance = find_distance(
                latitude_of_user, longitude_of_user, latitude_and_longitude[0], latitude_and_longitude[1])
            ten_nearest_locations.append(
                movie+[latitude_and_longitude]+[distance])
    ten_nearest_locations = sorted(
        ten_nearest_locations, key=lambda x: x[-1])[:10]
    return ten_nearest_locations
