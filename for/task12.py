def define_string(a, b):
    if a != str(a) and b != str(b):
        return 0
    elif type(a) == str and len(a) == len(b):
        return 1
    elif type(a) == str and len(a) > len(b):
        return 2
    elif type(a) == str and len(a) != len(b) and b == 'learn':
        return 3


print(define_string(12, 4566))
print(define_string('cat', 'dog'))
print(define_string('python', 'java'))
