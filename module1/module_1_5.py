immutable_var = (1, 'text', ['a', 'b'], True, {'key': 'value'})
print(immutable_var)
try:
    immutable_var[0] = 11
except Exception as e:
    print(e)
mutable_list = list(immutable_var)
mutable_list[0] = 11
print(mutable_list)
