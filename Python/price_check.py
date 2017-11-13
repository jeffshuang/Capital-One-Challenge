import csv

with open('price_location.csv', 'r', encoding="utf8") as listing_file:
    with open("price_location2.csv", mode='w') as newfile:
        csv_reader = csv.reader(listing_file)
        writer=csv.writer(newfile,delimiter=" ")
        for line in csv_reader:
            if line==[]: 
                continue
            print(line)
          