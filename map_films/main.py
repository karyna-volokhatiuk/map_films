from read_file import *
from create_map import *


def main(latitude_of_user, longitude_of_user, years):
    '''

    '''
    print('Map is generating...')
    print('Please wait...')
    latitude_of_user = float(latitude_of_user)
    longitude_of_user = float(longitude_of_user)
    dict_year_location_movie = reading_file(years)
    ten_nearest_locations = find_ten_nearest_locations(
        latitude_of_user, longitude_of_user, dict_year_location_movie)
    generate_map(ten_nearest_locations)
    print('Finished. Please, have look at the map movie_map.html.')


if __name__ == "__main__":
    years = input(
        'Please enter a year/years you would like to have a map for (format: year_1, year_2, ...): ').split(', ')
    latitude_of_user, longitude_of_user = input(
        'Please enter your location (format: lat, long): ').split(', ')
    main(latitude_of_user, longitude_of_user, years)
