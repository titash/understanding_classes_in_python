def ordinal(n: int):
    if 11 <= (n % 100) <= 13:
        suffix = "th"
    else:
        suffix = ["th", "st", "nd", "rd", "th"][min(n % 10, 4)]
    return str(n) + suffix


class myClass:
    cvar = 201  # class variable

    # class method:
    # function that works with class attribute but not with instance variables
    @classmethod
    def get_instance_counter(cls):
        return cls.cvar

    # static method:
    #

    def __init__(self, name) -> None:
        self.person_name = name
        myClass.cvar = myClass.cvar + 1
        print(
            f"now constructing {ordinal(myClass.cvar)} MyClass instance for {self.person_name}"
        )

    def greet(self):
        print(f"Hey there {self.person_name}!")


print(myClass.cvar)

x = myClass("David")
y = myClass("Emily")

print(f"{x.cvar=}")
print(f"{y.cvar=}")

print(y.cvar == x.cvar)

print(x.person_name)

x.greet()

print(myClass.get_instance_counter())
print(x.get_instance_counter())


# method: a function that is part of a class and performs type specific operations.
