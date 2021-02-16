'''
The main module.
'''
from analyze_data import *
from create_map import *


def main(latitude_of_user: float, longitude_of_user: float, year: str) -> None:
    print('Map is generating...')
    print('Please wait...')
    latitude_of_user = float(latitude_of_user)
    longitude_of_user = float(longitude_of_user)
    list_location_movie = reading_file(year)
    ten_nearest_locations = find_ten_nearest_locations(
        latitude_of_user, longitude_of_user, list_location_movie)
    generate_map(latitude_of_user, longitude_of_user,
                 ten_nearest_locations, year)
    print('Finished. Please, have look at the map movie_map.html.')


if __name__ == "__main__":
    year = input(
        'Please enter a year/years you would like to have a map for: ')
    latitude_of_user, longitude_of_user = input(
        'Please enter your location (format: lat, long): ').split(', ')
    main(latitude_of_user, longitude_of_user, year)
