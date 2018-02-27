import folium

# Center map on downtown minneapolis
map_mn = folium.Map(location=[45, -93.2])
folium.Marker(location=[45, -93.2])

# Add a marker for MCTC, at 44.9729, -93.2831
map_mn.save('map.html')

# Create a new map showing the whole os US
map_us = folium.Map(location=[40, -120], zoom_start=3)

map_us.save('map_us.html')
