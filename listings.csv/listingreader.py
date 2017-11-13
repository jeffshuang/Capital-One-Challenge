import csv
import math

#finds the average price of each lattitude and longitdue rounded 
with open('listings_utf8.csv', 'r', encoding="utf8") as listing_file:
    csv_reader = csv.reader(listing_file)

    location_num=dict()
    average_price=dict()
    next(csv_reader)
    for line in csv_reader:
        lats=math.ceil(float(line[48])*100)/100
        longs=math.ceil(float(line[49])*100)/100
        x=line[60][1:]
        #print(x)
        x=x.replace(",","")
        #print(lats,longs)
        if ((lats,longs) in location_num):
            location_num[(lats,longs)]+=1
            average_price[(lats,longs)]+=float(x)
        else:
            location_num[(lats,longs)]=1
            average_price[(lats,longs)]=float(x)
   
    for key in average_price:
        average_price[key]=average_price[key]/location_num[key]
        average_price[key]=math.ceil(average_price[key]*100)/100

    with open("price_location.csv", mode='w') as newfile:
        writer=csv.writer(newfile,delimiter=",")
        for key in average_price:
            #print([key,average_price[key]])
            writer.writerow([key,average_price[key]])
        

 

#print(average_price)               
    #except:
     #   print('') b


