import csv

mammoth_data = []

with open('pbdb_data.csv', 'r') as csvfile:

    reader = csv.reader(csvfile)

    # Creates column heading(types)
    columns = reader.__next__()

    # Get columns 9, 22, 23, 24, 25, 27, 28 and 32
    for row in reader:
        # Read the data and convert any numerical fields
        # (latitude, longitude) to floats, and the data to a new CSV.
        name = row[9]
        abd = row[22]
        abd_unit = row[23]
        lat = float(row[25])
        lng = float(row[24])
        State = row[27]
        county = row[28]
        comment = row[32]

        mammoth_data.append([name, abd, abd_unit, lat, lng, State, county, comment])
        # This creates a cleaned data for mapping.
    with open('mammoth_data.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(['name', 'abd', 'abd_unit', 'lat', 'lng', 'State', 'county', 'comment'])
        writer.writerows(mammoth_data)
