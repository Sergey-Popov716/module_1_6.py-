my_dict = {'Ksusha': 1999, 'Dasha': 2000, 'Denis': 2001, 'Sergey': 1995}
print(my_dict)
print('Book:', my_dict)
my_dict.update({'Sasha' : 1997,
                "Tanya" : 1971})
print(my_dict)
my_dict.pop('Dasha')
print(my_dict)
my_set = {1, 2, 3, 4, 1, 2, 6, 8, 1, 'Planet', 'Planet', 'Cat', 'Planet', 'dogs'}
print(set(my_set))
my_set.add('string')
my_set.add('basketball')
print(my_set)
my_set.discard(1)
print(my_set)