import csv

mammoth_data = []

with open('pbdb_data.csv', 'r') as csvfile:

    reader = csv.reader(csvfile)

    # The first row is the column types, read this line. Keep if needed, but we can discard.
    columns = reader.__next__()

    # are interested in col 9, accepted_name
    # Abundance val and Abundance unit 22 and 23
    # lat, lng, cols 24 and 25
    # State, country, in 27, 28
    # geocomment
    for row in reader:

        # get data of interests. Convert numeric types to floats
        # write out to new CVS file that another module can reader
        name = row[9]
        abd = row[22]
        abd_unit = row[23]
        lat = float(row[25]) # These are reversed from the expected order
        lng = float(row[24]) # lng first, then lat
        State = row[27]
        country = row[28]
        comment = row[32]

        mammoth_data.append([name, abd, abd_unit, lat, lng, State. country, comment])

    with open('mammoth_data.cvs', 'w') as cvsfile:
        writer = cvs.writer(cvsfile, quoting=cvs.QUOTE_NONNUMERIC)
        writer.writerow(['name', 'abd', 'abd_unit', 'lat', 'lng', 'State', 'country', 'comment'])
        write.writerows(mammoth_data)
