# print("Hello World")

counties = ["Arapahoe", "Denver", "Jefferson"]

if counties[1] == 'Denver':

    print(counties[1])
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")
    
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

for county in counties:
    print(county)
    
numbers = [0, 1, 2, 3, 4]
# for num in numbers:
#     print(num)
for num in range(5):
    print(num) 


for i in range(len(counties)):
    print(counties[i])
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# print keys in dict
for county in counties_dict:
    print(county)
# for county in counties_dict.keys():
#   print(county)

for voters in counties_dict.values():
    print(voters)
# for i in counties_dict.values():
#   print(i)

for county in counties_dict:
    print(counties_dict[county])
for county in counties_dict:
    print(counties_dict.get(county))  

for county, voters in counties_dict.items():
    print(county, voters) 
# Print each county and registered voter form the counties dictionary so
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

    
# list of dictionaries in a list
voting_data = [{"county": "Arapahoe", "registered_voters": 422829},
               {"county": "Denver", "registered_voters": 463353},
               {"county": "Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict) 

# for i in range(len(counties_dict)):
# print(counties_dict[i])
for i in range(len(voting_data)):
    print(voting_data[i]["county"])

# to get values from list of dictionaries in a list
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
# f strings
# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# print(f"I received {my_votes / total_votes * 100}% of the total votes.") 

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes} number of votes. "
#     f"The total number of votes in the election was {total_votes}. "
#     f"You received {candidate_votes / total_votes * 100}% of the total votes.")

# print Floating point decimal
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")    
print(message_to_candidate)

# skill drill Print each county and registered voter from the dictionary.
# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters:,} registered voters.")

# Print each county and registered voter from the dictionary
voting_data = [{"county": "Arapahoe", "registered_voters": 422829},
               {"county": "Denver", "registered_voters": 463353}, {"county": "Jefferson", "registered_voters": 432438}]
for counties_dict in voting_data:
    print(f"{counties_dict['county']} county has {counties_dict['registered_voters']:,} registered voters.")
