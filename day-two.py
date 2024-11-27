from typing import Union

Number = Union[int, float]

def my_new_sum(arg1:Union, arg2:int|float, arg3:int|float = 0) -> Union:
    """_summary_

    Args:
        arg1 (int): _description_
        arg2 (int): _description_
        arg3 (int, optional): _description_. Defaults to 0.

    Returns:
        int: _description_
    """
    new_sum = arg1 + arg2 + arg3
    return new_sum

result = my_new_sum(arg1=1.1, arg2=2, arg3=2)
print(result)

def facelift_sum(*args:Number) -> Number:
    result = 0
    for num in args:
        result += num
    return result

res = facelift_sum(1,2,3,4,5)
print(res)

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} has a value of {value}")
        
display_info(name = "Andrius", role= "teacher")