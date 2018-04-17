import folium

# Create a map showing mn
map_mn = folium.Map(location=[45, -93.2])
map_mn.save('map.html')

# Create a map showing the whole of US
map_us = folium.Map(location=[40, -120], zoom_start=3)

map_us.save('map_us.html')
