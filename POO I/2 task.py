# ---------------------------------------------------------------
#           Inheritance, Polimorfism, Incapsulation
# ---------------------------------------------------------------

class Rifle:
    def __init__(self):
        self.ammo = 0
        self.range = 0
        self.cartrige = ""
        self.mass = 0

    def shoot(self):
        print("Rifle is shooting")

    def reload(self):
        print("Rifle is reloading")


class AWP(Rifle):
    def __init__(self):
        Rifle.__init__(self)
        self.ammo = 5
        self.range = 3943
        self.cartrige = ".338 LMB-action"
        self.mass = 6.5

    def show_info(self):
        print("Ammo: ", self.ammo)
        print("Range: ", self.range)
        print("Cartrige: ", self.cartrige)
        print("Mass: ", self.mass)

    def reload(self):
        print("Rifle is reloading, takes a 3 seconds")

    def shoot(self):
        print("Rifle is shooting, armour was pearsed through")


class Railgun(Rifle):
    def __init__(self):
        Rifle.__init__(self)
        self.ammo = 200
        self.range = 120
        self.cartrige = "feromagnetic pins"
        self.mass = 3

    def show_info(self):
        print("Ammo: ", self.ammo)
        print("Range: ", self.range)
        print("Cartrige: ", self.cartrige)
        print("Mass: ", self.mass)

    def reload(self):
        print("Rifle is reloading, takes a 1 seconds")

    def shoot(self):
        print("Rifle is shooting, armour was scratched")

# ---------------------------------------------
#           Main Program
# ---------------------------------------------


print("AWP")
rifle1 = AWP()
rifle1.show_info()
rifle1.shoot()
rifle1.reload()

print("Railgun")
rifle2 = Railgun()
rifle2.show_info()
rifle2.shoot()
rifle2.reload()
