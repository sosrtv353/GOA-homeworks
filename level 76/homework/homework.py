def row_sum_odd_numbers(n):
    return n**3

def printer_error(s):
    valid = "abcdefghijklm"
    res = 0

    for i in s:
        if i not in valid: res += 1

    return f"{res}/{len(s)}"

def reverse_words(text):
    str_list=text.split(" ")
    result = []
    for i in str_list:
        result.append(i[::-1])
    return " ".join(result)

def binary_array_to_number(arr):
    res = ""
    for bit in arr:
        res += str(bit)
    return int(res, 2)