import folium
from folium import plugins
import csv


# Create a dictionary of species and corresponding marker color.
mammoth_colors = {'Mammuthus columbi' : 'green',
    'Mammuthus primigenius': 'blue',
    'Mammuthus hayi' : 'purple',
    'Mammuthus exilis' : 'red',
    'Mammuthus' : 'ornage'}

# Use terrain tiles to create map
mammoth_map = folium.Map(location=[40, -120], zoom_start=3, tiles='Stamen Terrain')
lat_lng = []

# Read in mammoth_data.csv. Use data to Create markers, add to map_mn
# Use the mammoth_data.csv data to create markers
with open('mammoth_data.csv', 'r') as mammoth_csv:
    reader = csv.reader(mammoth_csv, quoting=csv.QUOTE_NONNUMERIC)
    firstline = reader.__next__()
    for line in reader:
        lat = line[3]
        lon = line[4]
        lat_lng.append([lat, lon])
        marker_text = '%s found in %s, %s, %s, ' % (line[0] , line[6] , line[5] , line[7])
        if line[1]:
            marker_text += ' %s %s ' % (line[1], line[2])

        color = mammoth_colors[line[0]]

        marker = folium.Marker([lat, lon], popup=marker_text, icon=folium.Icon(color=color))

        marker.add_to(mammoth_map)

mammoth_map.save('mammoth_map.html')

# Creates heat map representing where fossil finds are most concentrated.

heatmap = folium.Map(location=[40, -120], zoom_start=3)
# heatmap.add_children(plugins.HeatMap(lat_lng))
heatmap.add_child(plugins.HeatMap(lat_lng))
heatmap.save('mammoth_heatmap.html')
