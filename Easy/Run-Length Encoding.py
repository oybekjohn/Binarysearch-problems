def lengthEncoding(data):
    return f'{data.count(str(letter for letter in data))}{letter}'

lengthEncoding("your string here")