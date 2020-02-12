names = ["Sarah", "jorge", "sam", "frank"]
s_names = [name.capitalize() for name in names if name[0].lower() == 's']
print(s_names)

new_dict = {}

food_dict = {
    'apple': 'is a fruit',
    'cucumber': 'is a vegetable'
}

food_dict['cucumber'] = 'is maybe a vegetable'

chosen_fruit = 'apple'
print(food_dict[chosen_fruit])

for key in food_dict:
    print(key)
    print(f' {key} {food_dict[key]}')
