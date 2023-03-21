# Q25. Define a class, which have a class parameter and have a same instance parameter.

class Myclass:
    name = "Anonymous"
    def __init__(self, name = None):
        self.name = name

name = Myclass("Sushant")
print(f"{name.name}\t{Myclass.name}")

sushant = Myclass()
sushant.name = "Sushant"
print(f"{sushant.name}\t{Myclass.name}")