





def main():
    animals: list(str) = ['CAT', 'dog', 'FIsh', 'Elephant', 'lion']
    letter_len_for_each_animals = map(lambda a: a.capitalize(), animals)
    print(f'Length of each letters of animals {list(letter_len_for_each_animals)}')
    


if __name__ == "__main__":
    main()