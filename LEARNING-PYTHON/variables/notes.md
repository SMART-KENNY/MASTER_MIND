## Python Variable Name Rules

- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables

---

Here are some example of valid variable names:

firstname
first_name
capital_city
_if # if we want to use reserved word as a variable
year_2021
current_year_2021
num1

---

invalid variables name

first-name
first@name
first$name
num-1
1num

! the most common way of naming varaible is by using snake case
use underscore '_' character after each word for a variable eg.. (first_name, engine_rotation_speed).

first_name = 'kenny'
is_working = True
skills = ['python', 'bash', 'java', 'spark']
personal_info = {
    'country' : 'Japan',
    'age' : '20',
    'work' : 'Data Engineer'
}



##### Data types
to determine the data types of variable use type() function

print(type(first_name))          # str
print(type(10))                  # int
print(type(3.14))                # float
print(type(1 + 1j))              # complex
print(type(True))                # bool
print(type([1, 2, 3, 4]))        # list
print(type({'name':'kenny'})) # dict
print(type((1,2)))               # tuple
print(type(zip([1,2],[3,4])))    # zip


#### Cast casting variables
# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
num_float = float(num_str)
print('num_float', float(num_str))  # 10.6
num_int = int(num_float)
print('num_int', int(num_int))      # 10

# str to list
first_name = 'kenny'
print(first_name)               # 'kenny'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']