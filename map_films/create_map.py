import folium


def generate_map(dict_year_location_movie):
    '''
    Create a world_map with movies and save it to 'world_map.html'.
    '''
    world_map = folium.Map(location=[49.817545, 24.023932], zoom_start=10)
    colours = ['darkpurple', 'blue', 'beige', 'black',
               'orange', 'darkgreen', 'purple', 'lightred', 'darkred',
               'pink', 'white', 'gray', 'red', 'lightgreen', 'green',
               'darkblue', 'lightgray', 'cadetblue', 'lightblue']
    index_colour = 0
    for year in dict_year_location_movie:
        fg = folium.FeatureGroup(name=year)
        for movie in dict_year_location_movie[year]:
            fg.add_child(folium.Marker(location=movie[2],
                                       popup=movie[0] + '\n' + movie[1],
                                       icon=folium.Icon(color=colours[index_colour], icon_color='white')))
        index_colour += 1
        world_map.add_child(fg)
        #world_map.add_child(folium.PolyLine(dict_year_location_movie[year], color="red", weight=2.5, opacity=1))
        folium.PolyLine(
            dict_year_location_movie[year], color="red", weight=2.5, opacity=1).add_to(world_map)

    folium.LayerControl().add_to(world_map)

    world_map.save('world_map.html')
