import random
class Student:
    def __init__(self, name):
         self.name = name
         self.gladness = 50
         self.money = 50
         self.progress = 0
         self.alive = True
    def to_study(self):
         print("Время учится")
         self.progress += 0.12
         self.gladness -= 5
    def to_sleep(self):
         print("Мне пора спать")
         self.gladness += 3
    def to_chill(self):
        print("Время отдыха")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 9
    def to_work(self):
        print("Время работать")
        self.gladness -= 5
        self.money += 10

    def is_alive(self):
        if self.progress < 0:
            print("Пора учится")
            self.to_study()
        if self.money < 0:
            print("Время работать")
            self.to_work()
        if self.gladness < 0:
            print("Время прогулятся")
            self.to_chill()
        if self.progress < -0.5:
            print("Исключен…")
            self.alive = False
        elif self.gladness <= 0:
             print("Дипрессия…")
             self.alive = False
        elif self.progress > 5:
            print("Здал екзамены…")
            self.alive = False
        if self.money < -5:
            print("Бедный…")
            self.alive = False
        elif self.money <= 0:
            print("Дипрессия…")
            self.alive = False
        elif self.money > 100:
            print("Cчастлив…")
            self.alive = False


    def end_of_day(self):
     print(f"Gladness = {self.gladness}")
     print(f"Progress ={round(self.progress, 2)}")
     print(f"Money = {self.money}")

    def live(self, day):
        day = "Day" + str(day) + "of" +self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
         self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
            self.end_of_day()
            self.is_alive ()
        elif live_cube == 4:
            self.to_work()
            self.end_of_day()
            self.is_alive ()
nick = Student(name="Nick")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)