
Heroes of Pymoli Data Observations:
    
Males are the dominate percentage of players at 81%.

Players under 24 are the largest demographics of players, specifically the age group (20-24), which is 45% of players. 
Although players over 25 spend more on average per purchase.

The top five most popular items is not the most profitable.



```python
import pandas as pd
import numpy as np
import json
```


```python
data_file = "purchase_data.json"
gamedata = pd.read_json(data_file)

```

# PLAYER COUNT


```python
players = gamedata["SN"].nunique()
player_count = pd.DataFrame({"Total Number of Players":[players]})

player_count
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
      <th>Total Number of Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>



# PURCHASING ANALYSIS (TOTAL)


```python
products = gamedata["Item ID"].nunique()
avgprice = gamedata["Price"].mean()
purchases = gamedata["Item Name"].nunique()
totrevenue = gamedata["Price"].sum()


purchase_analysis = pd.DataFrame({"Number of Unique Items":[products], "Avg Purchase Price":[avgprice], 
                                  "Number of Purchases":[purchases], "Total Revenue":[totrevenue]})
purchase_analysis = purchase_analysis[["Number of Unique Items","Avg Purchase Price", "Number of Purchases", "Total Revenue"]]
purchase_analysis = purchase_analysis.round(2)
purchase_analysis
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
      <th>Number of Unique Items</th>
      <th>Avg Purchase Price</th>
      <th>Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>183</td>
      <td>2.93</td>
      <td>179</td>
      <td>2286.33</td>
    </tr>
  </tbody>
</table>
</div>



# GENDER DEMOGRAPHICS


```python
databy = gamedata.groupby(["SN","Gender"])
genderdata = databy.sum()
genderdata = genderdata.reset_index()

male = genderdata["Gender"].value_counts()['Male']
female = genderdata["Gender"].value_counts()['Female']
other = players - male - female

male_percent = (male/players)*100
female_percent = (female/players)*100
other_percent = (other/players)*100

gender_demo = pd.DataFrame({'Gender':['Male','Female','Other / Non-Disclosed'],
                            'Percentage of Players':[male_percent,female_percent,other_percent],
                            'Total Count':[male,female,other]})
gender_demo = gender_demo.round(2)
gender_demo
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
      <th>Gender</th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Male</td>
      <td>81.15</td>
      <td>465</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Female</td>
      <td>17.45</td>
      <td>100</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Other / Non-Disclosed</td>
      <td>1.40</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>



# PURCHASING ANALYSIS (GENDER)


```python
databy_price = pd.DataFrame(gamedata.groupby("Gender")["Price"].sum())
male_totprice = databy_price.loc["Male", "Price"]
female_totprice = databy_price.loc["Female", "Price"]
other_totprice = databy_price.loc["Other / Non-Disclosed", "Price"]

dnorm = pd.DataFrame(gamedata.groupby("Gender")["Price"].mean())
male_normprice = dnorm.loc["Male", "Price"]
female_normprice = dnorm.loc["Female", "Price"]
other_normprice = dnorm.loc["Other / Non-Disclosed", "Price"]

male_avgprice = male_totprice/male
female_avgprice = female_totprice/female
other_avgprice = other_totprice/other

gender_purchase = pd.DataFrame({'Gender':['Male','Female','Other / Non-Disclosed'],'Purchase Count':[male,female,other],
                                'Average Purchase Price':[male_avgprice,female_avgprice,other_avgprice],
                               'Total Purchase Value':[male_totprice,female_totprice,other_totprice], 
                                'Normalized Price':[male_normprice,female_normprice,other_normprice]})
gender_purchase = gender_purchase[["Gender","Purchase Count", "Average Purchase Price", "Total Purchase Value", 
                                   "Normalized Price"]]
gender_purchase = gender_purchase.round(2)
gender_purchase
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
      <th>Gender</th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Male</td>
      <td>465</td>
      <td>4.02</td>
      <td>1867.68</td>
      <td>2.95</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Female</td>
      <td>100</td>
      <td>3.83</td>
      <td>382.91</td>
      <td>2.82</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Other / Non-Disclosed</td>
      <td>8</td>
      <td>4.47</td>
      <td>35.74</td>
      <td>3.25</td>
    </tr>
  </tbody>
</table>
</div>



# AGE DEMOGRAPHICS


```python
agedata = gamedata.groupby(["SN","Age"])
d = agedata.sum()
d = d.reset_index()

age10 = d.loc[(d["Age"] < 10), :].count()['Age']
age10_14 = d.loc[(d["Age"] >= 10) & (d["Age"] <= 14), :].count()['Age']
age15_19 = d.loc[(d["Age"] >= 15) & (d["Age"] <= 19), :].count()['Age']
age20_24 = d.loc[(d["Age"] >= 20) & (d["Age"] <= 24), :].count()['Age']
age25_29 = d.loc[(d["Age"] >= 25) & (d["Age"] <= 29), :].count()['Age']
age30_34 = d.loc[(d["Age"] >= 30) & (d["Age"] <= 34), :].count()['Age']
age35_39 = d.loc[(d["Age"] >= 35) & (d["Age"] <= 39), :].count()['Age']
age40 = d.loc[(d["Age"] >= 40), :].count()['Age']

agecount = pd.DataFrame({"Age Range":["<10","10-14","15-19","20-24","25-29","30-34","35-39","40+"],
                         "Percentage of Players":[(age10/players)*100,(age10_14/players)*100,(age15_19/players)*100,
                                                 (age20_24/players)*100,(age25_29/players)*100,(age30_34/players)*100,
                                                 (age35_39/players)*100,(age40/players)*100],
                         "Total Count":[age10,age10_14,age15_19,age20_24,age25_29,age30_34,age35_39,age40]})
agecount = agecount.round(2)
agecount
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
      <th>Age Range</th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>&lt;10</td>
      <td>3.32</td>
      <td>19</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10-14</td>
      <td>4.01</td>
      <td>23</td>
    </tr>
    <tr>
      <th>2</th>
      <td>15-19</td>
      <td>17.45</td>
      <td>100</td>
    </tr>
    <tr>
      <th>3</th>
      <td>20-24</td>
      <td>45.20</td>
      <td>259</td>
    </tr>
    <tr>
      <th>4</th>
      <td>25-29</td>
      <td>15.18</td>
      <td>87</td>
    </tr>
    <tr>
      <th>5</th>
      <td>30-34</td>
      <td>8.20</td>
      <td>47</td>
    </tr>
    <tr>
      <th>6</th>
      <td>35-39</td>
      <td>4.71</td>
      <td>27</td>
    </tr>
    <tr>
      <th>7</th>
      <td>40+</td>
      <td>1.92</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>



# PURCHASING ANALYSIS (AGE)


```python
age10totp = d.loc[(d["Age"] < 10), :].sum()['Price']
age10_14totp = d.loc[(d["Age"] >= 10) & (d["Age"] <= 14), :].sum()['Price']
age15_19totp = d.loc[(d["Age"] >= 15) & (d["Age"] <= 19), :].sum()['Price']
age20_24totp = d.loc[(d["Age"] >= 20) & (d["Age"] <= 24), :].sum()['Price']
age25_29totp = d.loc[(d["Age"] >= 25) & (d["Age"] <= 29), :].sum()['Price']
age30_34totp = d.loc[(d["Age"] >= 30) & (d["Age"] <= 34), :].sum()['Price']
age35_39totp = d.loc[(d["Age"] >= 35) & (d["Age"] <= 39), :].sum()['Price']
age40totp = d.loc[(d["Age"] >= 40), :].sum()['Price']

age10norm = gamedata.loc[(gamedata["Age"] < 10), :].mean()['Price']
age10_14norm = gamedata.loc[(gamedata["Age"] >= 10) & (gamedata["Age"] <= 14), :].mean()['Price']
age15_19norm = gamedata.loc[(gamedata["Age"] >= 15) & (gamedata["Age"] <= 19), :].mean()['Price']
age20_24norm = gamedata.loc[(gamedata["Age"] >= 20) & (gamedata["Age"] <= 24), :].mean()['Price']
age25_29norm = gamedata.loc[(gamedata["Age"] >= 25) & (gamedata["Age"] <= 29), :].mean()['Price']
age30_34norm = gamedata.loc[(gamedata["Age"] >= 30) & (gamedata["Age"] <= 34), :].mean()['Price']
age35_39norm = gamedata.loc[(d["Age"] >= 35) & (gamedata["Age"] <= 39), :].mean()['Price']
age40norm = gamedata.loc[(gamedata["Age"] >= 40), :].mean()['Price']

agepurchase = pd.DataFrame({"Age Range":["<10","10-14","15-19","20-24","25-29","30-34","35-39","40+"],
                            "Total Count":[age10,age10_14,age15_19,age20_24,age25_29,age30_34,age35_39,age40],
                         "Average Purchase Price":[(age10totp/age10),(age10_14totp/age10_14),(age15_19totp/age15_19),
                                                   (age20_24totp/age20_24),(age25_29totp/age25_29),(age30_34totp/age30_34),
                                                  (age35_39totp/age35_39),(age40totp/age40)],
                            "Total Purchase Value":[age10totp,age10_14totp,age15_19totp,age20_24totp,age25_29totp,
                                                    age30_34totp,age35_39totp,age40totp],
                            "Normalized Price":[age10norm,age10_14norm,age15_19norm,age20_24norm,age25_29norm,age30_34norm,
                                                age35_39norm,age40norm]})
agepurchase = agepurchase[["Age Range","Total Count", "Average Purchase Price", "Total Purchase Value", "Normalized Price"]]
agepurchase = agepurchase.round(2)
agepurchase
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
      <th>Age Range</th>
      <th>Total Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>&lt;10</td>
      <td>19</td>
      <td>4.39</td>
      <td>83.46</td>
      <td>2.98</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10-14</td>
      <td>23</td>
      <td>4.22</td>
      <td>96.95</td>
      <td>2.77</td>
    </tr>
    <tr>
      <th>2</th>
      <td>15-19</td>
      <td>100</td>
      <td>3.86</td>
      <td>386.42</td>
      <td>2.91</td>
    </tr>
    <tr>
      <th>3</th>
      <td>20-24</td>
      <td>259</td>
      <td>3.78</td>
      <td>978.77</td>
      <td>2.91</td>
    </tr>
    <tr>
      <th>4</th>
      <td>25-29</td>
      <td>87</td>
      <td>4.26</td>
      <td>370.33</td>
      <td>2.96</td>
    </tr>
    <tr>
      <th>5</th>
      <td>30-34</td>
      <td>47</td>
      <td>4.20</td>
      <td>197.25</td>
      <td>3.08</td>
    </tr>
    <tr>
      <th>6</th>
      <td>35-39</td>
      <td>27</td>
      <td>4.42</td>
      <td>119.40</td>
      <td>2.57</td>
    </tr>
    <tr>
      <th>7</th>
      <td>40+</td>
      <td>11</td>
      <td>4.89</td>
      <td>53.75</td>
      <td>3.16</td>
    </tr>
  </tbody>
</table>
</div>



# TOP SPENDERS


```python
sn_sort = d.sort_values("Price", ascending=False)
topval = sn_sort.loc[:, ["SN","Price"]]
topval = topval.rename(columns={"Price": "Total Purchase Value"})

tcount = agedata.count()
tcount = tcount.reset_index()
tcount = tcount.sort_values("Price",ascending=False)
tcount = tcount.drop(columns=['Age', 'Gender','Item Name','Price'])
tcount = tcount.rename(columns={"Item ID": "Purchase Count"})

topmerge = pd.merge(topval,tcount,how='inner')

newtop_merge = pd.DataFrame(topmerge["Total Purchase Value"]/topmerge["Purchase Count"],columns=['Average Purchase Price'])
ntopmerge = pd.merge(topmerge,newtop_merge, how='outer',left_index=True,right_index=True)
ntopmerge = ntopmerge[["SN","Purchase Count","Average Purchase Price","Total Purchase Value"]]
ntopmerge = ntopmerge.round(2)
ntopmerge.head()
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
      <th>SN</th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Undirrala66</td>
      <td>5</td>
      <td>3.41</td>
      <td>17.06</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Saedue76</td>
      <td>4</td>
      <td>3.39</td>
      <td>13.56</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Mindimnya67</td>
      <td>4</td>
      <td>3.18</td>
      <td>12.74</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Haellysu29</td>
      <td>3</td>
      <td>4.24</td>
      <td>12.73</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Eoda93</td>
      <td>3</td>
      <td>3.86</td>
      <td>11.58</td>
    </tr>
  </tbody>
</table>
</div>



# MOST POPULAR ITEMS


```python
itemdata = gamedata.groupby(["Item ID","Price"])
icount = itemdata.count()
icount = icount.reset_index()
icount = icount.sort_values("Item Name",ascending=False)
icount = icount.drop(columns=['Age', 'Gender','Item Name'])
icount = icount.rename(columns={"SN": "Purchase Count"})

iname = gamedata.groupby(["Item ID","Item Name"])
popname = iname.sum()
popname = popname.reset_index()
popname = popname.drop(columns=['Age','Price'])
popitem = pd.merge(icount,popname,how='inner')

popi_totvalue = pd.DataFrame(popitem["Price"]*popitem["Purchase Count"],columns=['Total Purchase Value'])
popimerge = pd.merge(popitem,popi_totvalue, how='outer',left_index=True,right_index=True)
popimerge = popimerge[["Item ID","Item Name","Purchase Count","Price","Total Purchase Value"]]
popimerge.head()
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
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Purchase Count</th>
      <th>Price</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>39</td>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>11</td>
      <td>2.35</td>
      <td>25.85</td>
    </tr>
    <tr>
      <th>1</th>
      <td>84</td>
      <td>Arcane Gem</td>
      <td>11</td>
      <td>2.23</td>
      <td>24.53</td>
    </tr>
    <tr>
      <th>2</th>
      <td>31</td>
      <td>Trickster</td>
      <td>9</td>
      <td>2.07</td>
      <td>18.63</td>
    </tr>
    <tr>
      <th>3</th>
      <td>175</td>
      <td>Woeful Adamantite Claymore</td>
      <td>9</td>
      <td>1.24</td>
      <td>11.16</td>
    </tr>
    <tr>
      <th>4</th>
      <td>13</td>
      <td>Serenity</td>
      <td>9</td>
      <td>1.49</td>
      <td>13.41</td>
    </tr>
  </tbody>
</table>
</div>



# MOST PROFITABLE ITEM


```python
profit_sort = popimerge.sort_values("Total Purchase Value",ascending=False)
profit_sort.head()
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
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Purchase Count</th>
      <th>Price</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>34</td>
      <td>Retribution Axe</td>
      <td>9</td>
      <td>4.14</td>
      <td>37.26</td>
    </tr>
    <tr>
      <th>13</th>
      <td>115</td>
      <td>Spectral Diamond Doomblade</td>
      <td>7</td>
      <td>4.25</td>
      <td>29.75</td>
    </tr>
    <tr>
      <th>39</th>
      <td>32</td>
      <td>Orenmir</td>
      <td>6</td>
      <td>4.95</td>
      <td>29.70</td>
    </tr>
    <tr>
      <th>24</th>
      <td>103</td>
      <td>Singed Scalpel</td>
      <td>6</td>
      <td>4.87</td>
      <td>29.22</td>
    </tr>
    <tr>
      <th>9</th>
      <td>107</td>
      <td>Splitter, Foe Of Subtlety</td>
      <td>8</td>
      <td>3.61</td>
      <td>28.88</td>
    </tr>
  </tbody>
</table>
</div>


