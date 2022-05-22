def where_is_my_char(str, char):
    positions = []
    for x in range(0, len(str) ):
        if str[x] == char:
            positions.append(x)

    return positions


[input_string, input_char] = input("input a string and a char operated with a space and hit enter: ").split()

print(where_is_my_char(input_string, input_char))
