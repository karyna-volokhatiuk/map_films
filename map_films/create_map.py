import folium


def generate_map(latitude_of_user: float, longitude_of_user: float, ten_nearest_locations: list, year: str) -> None:
    '''
    Create a world_map with movies and save it to 'world_map.html'.
    '''

    world_map = folium.Map(
        location=(latitude_of_user, longitude_of_user), zoom_start=5)

    fg_user_location = folium.FeatureGroup(name='User location')
    folium.CircleMarker(location=(latitude_of_user, longitude_of_user), radius=10,
                        color='darkpurple', fill_color='darkpurple', popup='You are here:)').add_to(fg_user_location)
    world_map.add_child(fg_user_location)

    fg_markers = folium.FeatureGroup(name='Films of year '+str(year))
    for movie in ten_nearest_locations:
        fg_markers.add_child(folium.Marker(location=movie[2],
                                           popup=movie[0] + '\n' + movie[1],
                                           icon=folium.Icon(color='darkpurple', icon_color='white')))
    world_map.add_child(fg_markers)

    fg_distances = folium.FeatureGroup(name='Distances')
    points = [i[2] for i in ten_nearest_locations]
    for point in points:
        folium.PolyLine([point, (latitude_of_user, longitude_of_user)],
                        color='pink', weight=2.5, opacity=1).add_to(fg_distances)
    world_map.add_child(fg_distances)

    folium.LayerControl().add_to(world_map)

    world_map.save('world_map.html')
