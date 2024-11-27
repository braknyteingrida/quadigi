from pprint import pprint as print
#list
# dim = 10
# my_2d_list = [["*"] * dim] * dim
# print (my_2d_list)

#tuple
# tuple_ = (1, "2", (1,2), None) # non mutible
# tuple_single_elem = (1,)
# print(tuple_)

# idx = tuple_.index("2")
# print(idx)

# first, second, third, forth = tuple_
# print(third)

# first, *_ = tuple_
# print(first)

# first, *remaining = tuple_
# print(remaining)

# tuple_[1]


#set
my_set = {1,"2",3,4,5,6,7} # neturi indeku
my_set.add(True)
my_set.remove("2")
print(my_set)

#dict
empty_dict = {}
my_dict = {"key1":1, "key2": "Value2"}
my_dict_2 = dict(key1=1,key2="Some Value")


if "key2" in my_dict:
    print(my_dict["key2"])
    
    
value = my_dict.get("key", 123) # jei randi "key" grazina "key, jei ne 123"
print(value)

my_dict["new_elem"] = None #add new
my_dict["new_elem"] = 98 # change
print(my_dict)