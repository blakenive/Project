from time import*
class president():
    def __init__(self,name,health,money,damage,nalog):
        self.name = name
        self.health = health
        self.money = money
        self.damage = damage
        self.nalog = nalog

    def print_info(self):
        print("Поприветствуйте президента:", self.name)
        print("Хелтх:", self.health)
        print("Бабло:", self.money)
        print("Мощность леща:", self.damage)
        print("Удар по насалению налогом:", self.nalog)

    def strike(self,enemy):
        print(self.name,"дал леща с силой:", self.damage,"Врагу:", enemy.name)
        enemy.health -= self.damage
        if enemy.health <0:
            enemy.money += enemy.health
            enemy.helth = 0
        print("Враг", enemy.name, "получил удар лещом остаток хп:", enemy.health, "остаток моней:", enemy.money)
    def fight(self,enemy):
        while self.money and enemy.money >0:
            print("")
            self.strike(enemy)
            if enemy.money <0:
                print("")
                print("Президент:",enemy.name, "Попущен и отпущен до народа")
                break
            sleep(1.5)
            enemy.strike(self)
            if self.money <0:
                print("")
                print(self.name, "Попущен и отпущен до народа")
                break
            sleep(1.5)
Putin = president("Путин",100,1000,15,"Налог на шаги")
Putin.print_info()
print("")
Zelenka = president("Зеленский",70,10,6,"Налог на сало")
Zelenka.print_info()
print("")
Bidon = president("Байдон",85,1200,10,"Налог на налог")
Bidon.print_info()
print("")
Putin.fight(Zelenka)
if Putin.money >0:
    print("Хп увеличены на 150")
    Putin.health += 150
Putin.fight(Bidon)

