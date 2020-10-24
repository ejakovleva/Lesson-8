class TypeListError(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []

while True:
    x = input("Enter any number (if you want to quit enter 'stop'): ")
    if 'stop' in x:
        break
    try:
        x
        for i in x:
            if ord(i) not in range(ord('0'), ord('9') + 1) and ord(i) != ord('.'):
                raise TypeListError("Enter only integers!")
    except TypeListError as err:
        print(err)
    else:
        my_list.append(float(x))

print(my_list)
