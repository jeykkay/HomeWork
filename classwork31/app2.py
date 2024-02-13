def get_number(digits):
    if not digits:
        return []

    number = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def search_combination(combination, next_number):
        list_combination = []
        search_combination('', digits)

        if not next_number:
            list_combination.append(combination)






