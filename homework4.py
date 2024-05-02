immutable_var = (1, 2, "a", "b", [1, 2] + ["a", "b"], 36.6, 'Normal', None, False)
print(immutable_var)

immutable_var_2 = (4, 5, 6)
#[0] = 404           #Используем когда хотим сохранить список значений, которые мы не будем редактировать


mutable_list = [1, 2, 3, 4, 5, 6]
print(mutable_list)
mutable_list [2] = 404
print(mutable_list)