print("Hello World")

counties=["Arapahoe","Denver","Jefferson"]
if counties[1]!="Denver":
    print(counties[1])

tempreature=int(input("Wat is the temprature ounside?"))
if tempreature>80:
    print("Turn on the AC.")
else:
    print("Open the windows.")

counties=["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")

counties=["Arapahoe","Denver","Jefferson"]
if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

    x=0
    while x<=5:
        print(x)
        x=x+1

for county in counties:
    print(county)

counties_dict={"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
for county in counties_dict.keys():
    print(county)
for county, voters in counties_dict.items():
    print(f'{county} county has {voters} registered voters.')

    counties_dict={"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
    for county,voters in counties_dict.items():
        print(f'{county} county has {voters} registered voters.')
        
    voting_data=[''{"county":"Arapahoe","registered_voters":422829},{"county":"Denver","registered_voters":463353},{"county":"Jefferson","registered_voters":432438}]
    for county_dict in voting_data:
            print(county_dict)

    for i in range(len(voting_data)):
        print(voting_data[i]['county'])

    for county_dict in voting_data:
        print(county_dict['registered_voters'])

    for county_dict in voting_data:
        print(f"{county_dict['county']} county has {county_dict['registered_voters']} registered voters.")