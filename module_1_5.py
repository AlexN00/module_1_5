immutable_var = 1, 2, True, 'hello'
print(immutable_var)
#immutable_var[0]=3 #не дает изменить элемент кортеджа так как Элементы кортеджа являются неизменяемыми
#print(immutable_var)
mutable_list= [1,2,'hello']
print(mutable_list)
mutable_list[0]=4
print(mutable_list)
