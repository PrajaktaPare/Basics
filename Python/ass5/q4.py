people = {
	'John': {'age': 45, 'city': 'New York'},
	'Mike': {'age': 22, 'city': 'Los Angeles'},
	'Sarah': {'age': 32, 'city': 'New York'},
	'Anna': {'age': 28, 'city': 'Chicago'}
}

for name, details in people.items():
    if details['city'] == 'New York' and details['age'] > 30:
        print(name)