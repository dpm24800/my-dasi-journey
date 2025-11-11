---
layout: post
title:  Pandas/Matplotlib Exercise – 1
description: 
# thumbnail: ../../../../../assets/Correl.png
author: Dipak Pulami Magar
date:   2025-11-10 20:12:45 +0545
categories: pandas exercises
status: published
---

#### Question: Write a Python program to create a plot (lines) of total deaths, confirmed, recovered and active cases country wise where deaths greater than 150.

**Solution**:
```py
import matplotlib.pyplot as plt
import pandas as pd

# Load and process data
df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-19-2020.csv')

# Add new column 'Active' from other columns
df['Active'] = df['Confirmed'] - df['Deaths'] - df['Recovered']
country_wise = df.groupby(["Country/Region"])[['Confirmed','Deaths','Recovered','Active']].sum()
df_above150 = country_wise[country_wise['Deaths'] > 150]

print("Summary:\n", df_above150)

# Plot each column with custom styles
plt.figure(figsize=(10,6))
plt.plot(df_above150.index, df_above150['Confirmed'], color='blue', linestyle='--', marker='s', label='Confirmed')
plt.plot(df_above150.index, df_above150['Deaths'], color='red', linestyle='-', marker='o', label='Deaths')
plt.plot(df_above150.index, df_above150['Recovered'], color='green', linestyle='-.', marker='o', label='Recovered')
plt.plot(df_above150.index, df_above150['Active'], color='maroon', linestyle=':', marker='s', label='Active')

plt.grid(axis="both", color='green', linestyle='--', linewidth=0.6) # axis='x/y/both(default)'
plt.xlabel("Country/Region", fontsize=12)
plt.ylabel("Number of Cases", fontsize=12)
plt.title("COVID-19 Cases by Country (Deaths > 150)", fontsize=14)
plt.legend()
plt.show()
```

---

**Output**, 
```
Summary:
                 Confirmed  Deaths  Recovered  Active
Country/Region                                      
China               81156    3249      70535    7372
France              10886     243         12   10631
Iran                18407    1284       5710   11413
Italy               41035    3405       4440   33190
Spain               17963     830       1107   16026
US                  13680     200        108   13372
United Kingdom       2705     369         67    2269
```

![COVID-19](../../../../../assets/covid-19.png)