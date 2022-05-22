class Hero():
    def __init__(self, name, hp, armor):
        self.name = name
        self.hp = hp
        self.armor = armor
        
    def print_info(self):
        print("Здоровье:", self.hp)
        print("Колл-во брони:",self.armor)
    
class Warrior(Hero):
    def hello(self):
        print("Верхом на сцыганеном коне из горы появился:", self.name)
        self.print_info()

    def shot(self,enemy):
        print(self.name, "Ударил:", enemy.name, "С мощью:", self.damage)
        enemy.armor -= 10
        if enemy.armor < 0:
            enemy.armor += enemy.hp
        print("Чел:", enemy.name, "Получил в печень остаток хп и брони:", enemy.hp,",",enemy.armor)

Warrior1=Warrior("Вася Пупкин",100,50)
Warrior1.hello()

