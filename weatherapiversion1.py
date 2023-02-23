import json
import requests
import time
import matplotlib.pyplot as plt
from pprint import pprint as pp

url = 'https://api.open-meteo.com/v1/forecast?latitude=40.71&longitude=-74.01&hourly=snowfall'
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
print("The snow:" )
time.sleep(1)
snowfall = dataobj['hourly']['snowfall']
print(snowfall)
print()

for snow in snowfall:
    if snow != 0:
        time.sleep(1)
        print("The chances of snowfall are :")
        print(snow)


xaxis = dataobj['hourly']['time']
yaxis = dataobj['hourly']['snowfall']

plt.figure(figsize=(15,10))

plt.title('Generated in 0.42, download in 467 ms, time in GMT+0', fontsize=20, color='white')
plt.plot(xaxis, yaxis)

plt.xlabel("<---------------------------------------------------------------- SNOWFALL ---------------------------------------------------------------->", size = 10, color = 'black')
plt.ylabel("<---------------------------------------------- CM ---------------------------------------------->",size = 10, color = 'black')

plt.tick_params(axis = 'x', colors = 'black')
plt.tick_params(axis = 'y', colors = 'black')

plt.show()