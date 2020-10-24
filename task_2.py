class ZeroError(Exception):
    def __init__(self, error_txt):
        self.error_txt = error_txt


def division(numerator, denominator):
    try:
        numerator, denominator
        if denominator == 0:
            raise ZeroError("You can't delete by zero!")
    except (ValueError, ZeroError) as err:
        print(err)
    else:
        return round(numerator / denominator, 3)


print(division(int(input("Enter a nominator: ")), int(input("Enter a denominator: "))))
