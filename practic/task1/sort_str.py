def sort_str(input_string):
    letter_list = list(input_string)

    sorted_letters = sorted(letter_list)

    result_string = ''.join(sorted_letters)
    return result_string

inp_str = "привет"
sorted_string = sort_str(inp_str)
print(sorted_string)
