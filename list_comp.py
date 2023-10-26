# bits = [False, True, False, False, True, True]

# super_bits = [1 if b == True else 0 for b in bits]
# print(super_bits)


my_string = "MyNameIsShubhadip"
my_string = "".join(
    [
        i if i.islower() else f" {i.lower()}" if i in ["N", "I"] else f" {i}"
        for i in my_string
    ]
)[1:]
print(my_string)
