import csv
import math
 
with open("data.csv", newline='') as f:
    reader = csv.reader(f)
    file_data=list(reader)
data=file_data[0]

#step one(finding mean)

def mean(data):
    n=len(data)
    total=0
    for x in data:
        total+=int(x)

    mean=total / n
    return mean


#step 2 (squaring and getting values)
squared_list=[]
for number in data:
    a=int(number)-mean(data)
    a=a**2
    squared_list.append(a)


#step 3(finding the sum)

sum=0
for i in squared_list:
    sum=sum+i

#step4(divide the sum by total value)

result = sum/ (len(data)-1)

#step5 (get the deviation by getting square root)

standard_deviation=math.sqrt(result)
print(standard_deviation)