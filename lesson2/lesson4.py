
from random import *
class Student:

    def __init__(self,name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
    def to_study(self):
        print("time to study")
        self.gladness -= 5
        self.progress += 0.12
    def to_sleep(self):
        print("time to sleep")
        self.gladness += 3

    def to_chill(self):
        print("reeest!")
        self.gladness += 5
        self.progress -= 0.1
    def punishment(self):
        print("inconect input")
        self.progress -= 0.1
        self.gladness -= 5
    def end_of_day(self):
        print("=== Congratulate , day is done! === \n")
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {self.progress}")
    def is_alive(self):

      if self.progress < -0.5:

          print("Cast out... ;(")
          self.alive = False

      elif self.gladness < 0:
                print("Depression ;(")
                self.alive = False

      elif self.progress > 5:
                print("YOU WIN!!")
                self.alive = False


    def live(self, day):
        print()
        print("==" * 20)
        print("Day number is: ", day)

        life_choice = input("What will you do today")
                            "\n1) Study"
                            "\n2) Chill"
                            "\n3) Sleep"
        if live_choice == "1" or

        live_random = randint(1, 3)

        if live_random == 1:
         self.to_study()

        elif live_random == 2:
         self.to_chill()

        elif live_random == 3:
         self.to_sleep()

        self.end_of_day()
        self.is_alive()


student_Nazar = Student("Nazar")
for day in range(365):
    if student_Nazar.alive == False:
        break
    student_Nazar.live(day)

print("game over")


