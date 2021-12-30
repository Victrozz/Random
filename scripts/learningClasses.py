class Card(object):

    amount_of_cards = 4
    # these are methods, because they are in a class. Otherwise, they'd be functions.
    def __init__(self, name, price, health, attack):
        # these are attributes
        self.name = name
        self.price = price
        self.health = health
        self.attack = attack

    def speak(self):
        print("This card's name is", self.name + ", it costs", self.price, "points" + ", it has a health stat of", self.health, "and an attack stat of", self.attack)

    @classmethod
    def getAmount(cls):
        return cls.amount_of_cards

# outside the class, these are instances

wizard = Card("Wizard", 3, 3, 5)
gnome = Card("Gnome", 1, 2, 1)
giant = Card("Giant", 5, 20, 3)
witch = Card("Witch", 3, 4, 4)

# here, we call the speak method: a function is blah(something), a method is something.blah() and are always from a class.
wizard.speak()
gnome.speak()
giant.speak()
witch.speak()

