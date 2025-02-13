

class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name 
        self.lvl = lvl
        self.hp = hp

    def intoduce(self):
        return f"Привет, меня зовут {self.name}, мой lvl {self.lvl}, мое HP {self.hp}"
    
    def is_adult(self):
        if self.lvl >= 10:
            return True
        else:
            return False
    

superman = Hero("Klarkent", 15, 200)
print(superman.intoduce())

ironman = Hero("Tony", 8, 200)
halk = Hero("Gilbert", 12, 200)
print(ironman.is_adult())
print(halk.is_adult())





