import pandas, folium, json

data = pandas.read_csv('mammoth_data.csv') # dataframe from csvfile

# Get all the fossils for one state and create a quantity column using the copy of the abd column.
# The abd column contains the number of fossils found at a site.
quantities = data['abd']
# Assume that the record is for one mammoth, when there no data.
quantities = quantities.fillna(value = 1)

# Add the abd column to the dataframe
data['quantity'] = quantities

# Group by state, and sum the columns. We only need the sum of the quantity column.
# groupby returns a Groupby object. reset_index() returns that object into a dataframe
# Sum the columns
state_data_groups = data.groupby(by=['state']).sum().reset_index()

# Add states that have no mammoths to the dataframe.
states_abbr = json.load(open('us_states_abbr.json'))
state_list = list(states_abbr.keys())

# Create a data frame from state names, with zero for each quantity
all_states_zeros = pandas.Dataframe({ 'state':state_list, 'quantity' : 0})

# append the zero dataframe to the end of state_data_groups
all_state_data = state_data_groups.append(all_states_zeros)

# Remove the zero version of duplicate value for states that were already in the dataframe.
all_state_data = all_state_data.drop_duplicates('state', Keep='first')

state_data_groups = all_state_data.replace(states_abbr)

print (state_data_groups)

# Create the Choropleth map
us_states_filen= r'us_states.json'

choromap = folium.Map(location=[40, -120], zoom_start=3)

choromap.Choropleth(
    geo_path=us_states_file,
    data =state_data_groups,
    columns = ['state', 'quantity'],
    key_on = 'id',
    # Use color schema.
    fill_color = 'BuPu', fill_capacity = 0.6, line_opacity = 0.4,
    threshold_scale = [0, 5, 10, 15, 20, 90],
    # Create a legend for the color schema and scale.
    legend_name = "mammoth finds per state"
)

choromap.save('mammoth_choropleth.html')
