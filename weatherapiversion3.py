import json
import requests
import time
import matplotlib.pyplot as plt
from pprint import pprint as pp
import datetime 
from datetime import datetime

url = 'https://api.open-meteo.com/v1/forecast?latitude=40.71&longitude=-74.01&hourly=rain'
r = requests.get(url)
        
print("The requested data: ")
dataobj = r.json()
time.sleep(1)
print(json.dumps(dataobj, indent= 4))
print()

print("The keys of the requested data are:")
time.sleep(1)
pp(((list(dataobj.keys()))))
print()

#Printing the timezone of the town
timezone_attribute = dataobj['timezone']
time.sleep(1)
print("The timezone is:", timezone_attribute)
print()

#Nested Data from the API
print("The Rain:" )
time.sleep(1)
rain_chances = dataobj['hourly']['rain']
print(rain_chances)
print()

for rain_occurence in rain_chances:
    if rain_occurence != 0:
        print("The chances of rain are :")
        print(rain_occurence)


xaxis = dataobj['hourly']['time']
yaxis = dataobj['hourly']['rain']

xaxis = [datetime.fromisoformat(datestring) for datestring in xaxis]

plt.figure(figsize=(15,10))

plt.title('Generated in 0.24, download in 145ms, time in GMT+0', fontsize=20, color='white')
plt.plot(xaxis, yaxis)

plt.xlabel("<---------------------------------------------------------------- RAIN ---------------------------------------------------------------->", size = 10, color = 'black')
plt.ylabel("<---------------------------------------------- CM ---------------------------------------------->",size = 10, color = 'black')

plt.xticks(rotation = 10)
plt.tick_params(axis = 'x', colors = 'black')
plt.tick_params(axis = 'y', colors = 'black')

plt.show()