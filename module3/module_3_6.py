def calculate_structure_sum(data):
    result = 0
    for structure in data:
        if isinstance(structure, (str, int, float)):
            try:
                result += structure
            except TypeError:
                result += len(structure)
        elif isinstance(structure, (dict,)):
            for dict_result in [calculate_structure_sum(dict_item) for dict_item in structure.items()]:
                result += dict_result
        else:
            result += calculate_structure_sum(structure)
    return result


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


result = calculate_structure_sum(data_structure)
print(result)
