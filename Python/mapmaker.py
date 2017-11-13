import gmplot
import csv
import math

#generates mapfiles
#mapfiles later edited into to png files
# uses gmplot api

total=0;
total_reviews=0;

with open('listings_utf8.csv', 'r', encoding="utf8") as listing_file:
    csv_reader = csv.reader(listing_file)
    latitudes= []
    longitudes=[]
    next(csv_reader)
    for line in csv_reader:
        latitudes.append(float(line[48]))
        longitudes.append(float(line[49]))
        x=line[60][1:]
        #print(x)
        x=x.replace(",","")
      
        total+=float(x)
        total_reviews+=float(line[76])

    gmap = gmplot.GoogleMapPlotter(37.76, -122.45, 13)

    gmap.heatmap(latitudes, longitudes)

    gmap.draw("all_listings.html")
    print('done')

average = total/8706
sd_total=0
average_reviews= total_reviews/8706
sd_review_total=0;

with open('listings_utf8.csv', 'r', encoding="utf8") as listing_file2:
    csv_reader2 = csv.reader(listing_file2)
    latitudes2= []
    longitudes2=[]
    next(csv_reader2)
    for line in csv_reader2:
        x=line[60][1:]
        x=x.replace(",","")
        sd_total+=(float(x)-average)**2
        sd= math.sqrt(sd_total/8706)
        if (float(x) > average+2*sd): 
            latitudes2.append(float(line[48]))
            longitudes2.append(float(line[49]))

    gmap2 = gmplot.GoogleMapPlotter(37.76, -122.45, 13)

    gmap2.heatmap(latitudes2, longitudes2)

    gmap2.draw("highest_average.html")
    print('done')

with open('listings_utf8.csv', 'r', encoding="utf8") as listing_file3:
    csv_reader3 = csv.reader(listing_file3)
    latitudes3= []
    longitudes3=[]
    next(csv_reader3)
    for line in csv_reader3:
        sd_review_total+=(float(line[76])-average_reviews)**2
        sd_reviews= math.sqrt(sd_review_total/8706)
        if (float(line[76]) > average_reviews+2*sd_reviews): 
            latitudes3.append(float(line[48]))
            longitudes3.append(float(line[49]))

    gmap3 = gmplot.GoogleMapPlotter(37.76, -122.45, 13)

    gmap3.heatmap(latitudes3, longitudes3)

    gmap3.draw("most_popular.html")
    print('done')

with open('listings_utf8.csv', 'r', encoding="utf8") as listing_file4:
    csv_reader4 = csv.reader(listing_file4)
    latitudes4= []
    longitudes4=[]
    next(csv_reader4)
    for line in csv_reader4:
        #print(line[79])
        if (line[79]!="" and float(line[79]) == 100): 
            latitudes4.append(float(line[48]))
            longitudes4.append(float(line[49]))

    gmap4 = gmplot.GoogleMapPlotter(37.76, -122.45, 13)

    gmap4.heatmap(latitudes4, longitudes4)

    gmap4.draw("best_reviewd.html")
    print('done')


#print(average)
#print(average_reviews)
#print(sd)
#print(latitudes2,longitudes2)
#print(sd_reviews)
