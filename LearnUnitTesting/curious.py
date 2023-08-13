


class FoxError(Exception):
    pass

def c(n):
    if n > 10:
        raise FoxError("It worked")
    pass

i = int(input("Give n: "))

c(i)