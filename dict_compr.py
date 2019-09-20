country_to_capital = {'United Kingdom': 'London', 'France': 'Paris', 'India': 'New Delhi', 'Sri Lanka': 'Colombo'}
captital_to_country = {capital: country for country, capital in country_to_capital.items()}
print(captital_to_country)


# duplicate keys are overwritten
words = ['hi', 'hello', 'welcome', 'hey']
d = {x[0]: x for x in words}
print(d)