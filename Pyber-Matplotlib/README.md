
# PYBER RIDE SHARING ANALYSIS

Pyber Data Analysis

Urban cities has the most rides and drivers per city but has a lower fare on average compared to other city types.

Rural riders spend the most on fares but use the ride sharing service the least.

Suburban cities has less than 20% of all driver counts, but still make up more than 25% of the total fares and rides produced.


```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```


```python
citydata_file = "generated_data/city_data.csv"
citydata = pd.read_csv(citydata_file)

ridedata_file = "generated_data/ride_data.csv"
ridedata = pd.read_csv(ridedata_file)
```


```python
#count the number of rides per city
ride_count = pd.DataFrame(ridedata["city"].value_counts())
ride_count = ride_count.reset_index()
ride_count = ride_count.rename(columns={"index":"city", "city":"ride count"})
```


```python
#total fares per city
fares = pd.DataFrame(ridedata.groupby("city")["fare"].sum())
fares = fares.reset_index()
fares = fares.rename(columns={"fare":"total fare"})
```


```python
#Merge ride count with total fare
newride = pd.merge(ride_count,fares)
```


```python
#calculate average fare and merge with previous table
avgfare = pd.DataFrame(newride["total fare"]/newride["ride count"],columns=['average fare'])
newride_data = pd.merge(newride,avgfare, how='outer',left_index=True,right_index=True)
newride_data = newride_data.round(1)
```

# RIDE SHARING TABLE


```python
#merge new ride data with city data for graphs
citynride = pd.merge(newride_data,citydata, how='inner')
citynride.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>ride count</th>
      <th>total fare</th>
      <th>average fare</th>
      <th>driver_count</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>North Audreyfort</td>
      <td>37</td>
      <td>874.2</td>
      <td>23.6</td>
      <td>36</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1</th>
      <td>East Karenmouth</td>
      <td>35</td>
      <td>832.2</td>
      <td>23.8</td>
      <td>46</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Alexisfort</td>
      <td>33</td>
      <td>903.1</td>
      <td>27.4</td>
      <td>24</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Mathewfurt</td>
      <td>33</td>
      <td>842.1</td>
      <td>25.5</td>
      <td>3</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Port Meghanton</td>
      <td>32</td>
      <td>712.9</td>
      <td>22.3</td>
      <td>22</td>
      <td>Urban</td>
    </tr>
  </tbody>
</table>
</div>




```python
#create tables for each city type
urban = citynride.query('type == "Urban"')
suburban = citynride.query('type == "Suburban"')
rural = citynride.query('type == "Rural"')

#create series array for scatter plot
urbanx = np.array(urban['ride count'])
urbany = np.array(urban['average fare'])
urbans = np.array(urban['driver_count'])

suburbanx = np.array(suburban['ride count'])
suburbany = np.array(suburban['average fare'])
suburbans = np.array(suburban['driver_count'])

ruralx = np.array(rural['ride count'])
ruraly = np.array(rural['average fare'])
rurals = np.array(rural['driver_count'])
```

# BUBBLE PLOT FOR RIDE SHARING DATA


```python
#Create scatter plot data points
up = plt.scatter(urbanx, urbany, s=urbans, c='gold',  edgecolors="black", label='Urban')
sp = plt.scatter(suburbanx, suburbany, s=suburbans, c='xkcd:light sky blue',  edgecolors="black", label='Suburban')
rp = plt.scatter(ruralx, ruraly, s=rurals, c='xkcd:pinkish orange',  edgecolors="black", label='Rural')

# Create a title, x label, y label and legend for chart
plt.title("Pyber Ride Sharing (2017)")
plt.xlabel("Total Rides (Per City)")
plt.ylabel("Average Fare ($)")
plt.legend(handles=[up, sp, rp], loc="best")
plt.text(5,12,"Note: Circle sizes corresponds to driver count per city")

plt.savefig("Pyberchart.png")
plt.show()
```


![png](output_12_0.png)


# TOTAL FARES BY CITY TYPE


```python
#calculate total fare of all rides
totfare = newride['total fare'].sum()

#calculate fare percentage by city type
totf1 = (urban['total fare'].sum()/totfare)*100
totf2 = (suburban['total fare'].sum()/totfare)*100
totf3 = (rural['total fare'].sum()/totfare)*100

#values for chart
totfare_citytype = [totf1,totf2,totf3]
```


```python
citylabels = ["Urban", "Suburban", "Rural"]
colors = ["gold","lightskyblue", "lightcoral"]
explode = (0, 0.05, 0.1)

plt.pie(totfare_citytype, explode=explode, labels=citylabels, colors=colors,
        autopct="%1.1f%%",startangle=60, shadow=True)
plt.title("Total Fares by City Type")
plt.axis("equal")
plt.show()
```


![png](output_15_0.png)


# TOTAL RIDES BY CITY TYPE


```python
#calculate total count of all rides
totrides = newride['ride count'].sum()

#calculate ride percentage by city type
totr1 = (urban['ride count'].sum()/totrides)*100
totr2 = (suburban['ride count'].sum()/totrides)*100
totr3 = (rural['ride count'].sum()/totrides)*100

#values for chart
totrides_citytype = [totr1,totr2,totr3]
```


```python
plt.pie(totrides_citytype, explode=explode, labels=citylabels, colors=colors,
        autopct="%1.1f%%",startangle=60, shadow=True)
plt.axis("equal")
plt.title("Total Rides by City Type")
plt.show()
```


![png](output_18_0.png)


# TOTAL DRIVERS BY CITY TYPE


```python
#calculate total drivers of all rides
totdrivers = citynride['driver_count'].sum()

#calculate driver percentage by city type
totd1 = (urban['driver_count'].sum()/totdrivers)*100
totd2 = (suburban['driver_count'].sum()/totdrivers)*100
totd3 = (rural['driver_count'].sum()/totdrivers)*100

#values for chart
totdriver_citytype = [totd1,totd2,totd3]
```


```python
plt.pie(totdriver_citytype, explode=explode, labels=citylabels, colors=colors,
        autopct="%1.1f%%", startangle=45, shadow=True)
plt.axis("equal")
plt.title("Total Drivers by City Type")
plt.show()
```


![png](output_21_0.png)

