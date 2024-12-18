my_dict = {
    'Name1': 1990,
    'Name2': 2000,
    'Name3': 2010,
}
print(my_dict.get('Name3'))
print(my_dict.get('Name4'))
my_dict.update({
    'Name4': 2020,
    'Name5': 2030,
})
print(my_dict.pop('Name5'))
print(my_dict)
print()
my_set = {1, 2, 3, 1, 2, 3, 'name', 'text', 'name'}
print(my_set)
my_set.update([False, 13])
my_set.remove('name')
print(my_set)