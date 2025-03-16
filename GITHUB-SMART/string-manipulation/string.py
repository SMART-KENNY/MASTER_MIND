import datetime



def write_log(date_tirgger=''):
    
    print(f'INFO: INITIALIZE AT {date_tirgger}')
    ...





def toCapitalize(param='') -> str:
    param = param.capitalize()
    print(f'CALLING CAPITALIZING THE FIRST LETTER: {param}')

def toCaseFold(param='') -> str:
    param = param.casefold()
    print(f'REMOVE CASE FROM LETTERS {param}')

def toCenter(param='') -> str:
    param = param.center(50, '.')
    print(f'ADDING SPACE TO CENTER THE STRING {param}')

def toCountLetters(param='') -> str:
    param = param.count('n')
    print(f'COUNTING THE LETTERS FROM THE STRING {param}')



def main ():
    date_trigger = datetime.datetime.now()
    date_trigger = date_trigger.strftime("%Y - %m - %d %H:%M:%S")

    write_log(date_tirgger=date_trigger)
    string_input = str(input('INFO: TYPE ANYTHING: '))
    
    toCapitalize(param=string_input)
    toCaseFold(param=string_input)
    toCenter(param=string_input)
    toCountLetters(param=string_input)
    ...


if __name__ == "__main__":
    main()
    ...