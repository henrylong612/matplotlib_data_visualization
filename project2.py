import json
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np


units=[]
with open('/Users/hankilong/Documents/Henry Long Claremont McKenna College/CMC Sophomore/FA 2022/CSCI/project_02/airlines.json') as f:
    text=f.read()
    units+=json.loads(text)

dates = range(2004,2017)
date_old=0
date_new=0
flight=0

ATL_flights=[]
for unit in units:
    if unit["Airport"]["Code"]=='ATL':
        date_new=unit["Time"]["Year"]
        if date_new!=date_old:
            ATL_flights.append(flight)
            flight=unit["Statistics"]["Flights"]["Total"]
            date_old=date_new
        elif date_new==date_old:
            flight+=unit["Statistics"]["Flights"]["Total"]
ATL_flights=ATL_flights[1:]
plt.plot(dates,ATL_flights,label="ATL")

DFW_flights=[]
for unit in units:
    if unit["Airport"]["Code"]=='DFW':
        date_new=unit["Time"]["Year"]
        if date_new!=date_old:
            DFW_flights.append(flight)
            flight=unit["Statistics"]["Flights"]["Total"]
            date_old=date_new
        elif date_new==date_old:
            flight+=unit["Statistics"]["Flights"]["Total"]
DFW_flights=DFW_flights[1:]
plt.plot(dates,DFW_flights,label="DFW")

LAX_flights=[]
for unit in units:
    if unit["Airport"]["Code"]=='LAX':
        date_new=unit["Time"]["Year"]
        if date_new!=date_old:
            LAX_flights.append(flight)
            flight=unit["Statistics"]["Flights"]["Total"]
            date_old=date_new
        elif date_new==date_old:
            flight+=unit["Statistics"]["Flights"]["Total"]
LAX_flights=LAX_flights[1:]
plt.plot(dates,LAX_flights,label="LAX")

ORD_flights=[]
for unit in units:
    if unit["Airport"]["Code"]=='ORD':
        date_new=unit["Time"]["Year"]
        if date_new!=date_old:
            ORD_flights.append(flight)
            flight=unit["Statistics"]["Flights"]["Total"]
            date_old=date_new
        elif date_new==date_old:
            flight+=unit["Statistics"]["Flights"]["Total"]
ORD_flights=ORD_flights[1:]
plt.plot(dates,ORD_flights,label="ORD")

CLT_flights=[]
for unit in units:
    if unit["Airport"]["Code"]=='CLT':
        date_new=unit["Time"]["Year"]
        if date_new!=date_old:
            CLT_flights.append(flight)
            flight=unit["Statistics"]["Flights"]["Total"]
            date_old=date_new
        elif date_new==date_old:
            flight+=unit["Statistics"]["Flights"]["Total"]
CLT_flights=CLT_flights[1:]
plt.plot(dates,CLT_flights,label="CLT")

MCO_flights=[]
for unit in units:
    if unit["Airport"]["Code"]=='MCO':
        date_new=unit["Time"]["Year"]
        if date_new!=date_old:
            MCO_flights.append(flight)
            flight=unit["Statistics"]["Flights"]["Total"]
            date_old=date_new
        elif date_new==date_old:
            flight+=unit["Statistics"]["Flights"]["Total"]
MCO_flights=MCO_flights[1:]
plt.plot(dates,MCO_flights,label="MCO")

LAS_flights=[]
for unit in units:
    if unit["Airport"]["Code"]=='LAS':
        date_new=unit["Time"]["Year"]
        if date_new!=date_old:
            LAS_flights.append(flight)
            flight=unit["Statistics"]["Flights"]["Total"]
            date_old=date_new
        elif date_new==date_old:
            flight+=unit["Statistics"]["Flights"]["Total"]
LAS_flights=LAS_flights[1:]
plt.plot(dates,LAS_flights,label="LAS")

PHX_flights=[]
for unit in units:
    if unit["Airport"]["Code"]=='PHX':
        date_new=unit["Time"]["Year"]
        if date_new!=date_old:
            PHX_flights.append(flight)
            flight=unit["Statistics"]["Flights"]["Total"]
            date_old=date_new
        elif date_new==date_old:
            flight+=unit["Statistics"]["Flights"]["Total"]
PHX_flights=PHX_flights[1:]
plt.plot(dates,PHX_flights,label="PHX")

MIA_flights=[]
for unit in units:
    if unit["Airport"]["Code"]=='MIA':
        date_new=unit["Time"]["Year"]
        if date_new!=date_old:
            MIA_flights.append(flight)
            flight=unit["Statistics"]["Flights"]["Total"]
            date_old=date_new
        elif date_new==date_old:
            flight+=unit["Statistics"]["Flights"]["Total"]
MIA_flights=MIA_flights[1:]
plt.plot(dates,MIA_flights,label="MIA")

plt.title('Annual Total Number of Flights by Airport since 2004')
plt.xlabel('Year')
plt.xticks(np.arange(2003, 2017, 1))
plt.ylabel('Total Number of Flights')
plt.legend(bbox_to_anchor=(1,1), loc='upper left', borderaxespad=0)
plt.show()


with open('/Users/hankilong/Documents/Henry Long Claremont McKenna College/CMC Sophomore/FA 2022/CSCI/project_02/AH_Provisional_COVID-19_Deaths_by_County_and_Age_for_2020.csv') as f:
    spreadsheet=list(csv.reader(f))

youth=0
twenties=0
thirties=0
forties=0
fifties=0
sixties=0
seventy_plus=0

for row in spreadsheet:
    if row[4]=='MN':
        if row[10]=='0-19 Years':
            if row [11]=='':
                youth+=5
            elif row[11]!='':
                youth+=int(row[11])
        if row[10]=='20-24 Years' or row[10]=='25-29 Years':
            if row [11]=='':
                twenties+=5
            elif row[11]!='':
                twenties+=int(row[11])
        if row[10]=='30-34 Years' or row[10]=='35-39 Years':
            if row [11]=='':
                thirties+=5
            elif row[11]!='':
                thirties+=int(row[11])
        if row[10]=='40-44 Years' or row[10]=='45-49 Years':
            if row [11]=='':
                forties+=5
            elif row[11]!='':
                forties+=int(row[11])
        if row[10]=='50-54 Years' or row[10]=='55-59 Years':
            if row [11]=='':
                fifties+=5
            elif row[11]!='':
                fifties+=int(row[11])
        if row[10]=='60-64 Years' or row[10]=='65-69 Years':
            if row [11]=='':
                sixties+=5
            elif row[11]!='':
                sixties+=int(row[11])
        if row[10]=='70-74 Years' or row[10]=='75 Years and Over':
            if row [11]=='':
                seventy_plus+=5
            elif row[11]!='':
                seventy_plus+=int(row[11])

terms=['0-19 Years','20-29 Years','30-39 Years','40-49 Years','50-59 Years','60-69 Years','70+ Years']
counts=[youth,twenties,thirties,forties,fifties,sixties,seventy_plus]

fig, ax = plt.subplots()
ax.bar(terms, counts)
plt.title('Approximate Number of COVID-19 Deaths in Minnesota in 2020 by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Approximate Number of COVID-19 Deaths in Minnesota in 2020')
plt.show()
    






"""
with open('/Users/hankilong/Documents/Henry Long Claremont McKenna College/CMC Sophomore/FA 2022/CSCI/project_02/School_Learning_Modalities.csv') as f:
    spreadsheet=list(csv.reader(f))

ca_2021=0
ca_in_person_2021=0
tx_2021=0
tx_in_person_2021=0

ca_2022=0
ca_in_person_2022=0
tx_2022=0
tx_in_person_2022=0

for row in spreadsheet:
    if row[2][:10]=='08/01/2021':
        if row[7]=='CA':
            ca_2021+=1
            if row[3]=='Remote':
                ca_in_person_2021+=1
        if row[7]=='TX':
            tx_2021+=1
            if row[3]=='In Person':
                tx_in_person_2021+=1
    if row[2][:10]=='07/31/2022':
        if row[7]=='CA':
            ca_2022+=1
            if row[3]=='Remote':
                ca_in_person_2022+=1
        if row[7]=='TX':
            tx_2022+=1
            if row[3]=='In Person':
                tx_in_person_2022+=1

ca_percent_in_person_2021=100*ca_in_person_2021/ca_2021
tx_percent_in_person_2021=100*tx_in_person_2021/tx_2021

ca_percent_in_person_2022=100*ca_in_person_2022/ca_2022
ca_percent_in_person_2022=100*tx_in_person_2022/tx_2022

print(ca_percent_in_person_2021)

terms=['California Percent in Person 2021', 'Texas Percent in Person 2021', 'California Percent in Person 2022', 'Texas Percent in Person 2022']
counts=[ca_percent_in_person_2021,tx_percent_in_person_2021,ca_percent_in_person_2022,ca_percent_in_person_2022]

fig, ax = plt.subplots()
ax.bar(terms, counts)
plt.show()
"""
