# Print the following dictionary using the format method and ** unpacking.

country = {
 	"name": "Germany",
 	"population": "83 million",
 	"capital": "Berlin",
 	"currency": "Euro"
 }


# def showme(countries):
#     for entry in countries:
#         print("{name}is a country with population: {population}.\nCapital for {name} is in {capital} and offcial currency - {currency}".format(**entry))

print("{name} is a country with population: {population}.\nCapital for {name} is in {capital} and offcial currency '{currency}'".format(**country))
