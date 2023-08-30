class Bank:
    def _person_3(self):
        print("Name : Sara")
        print("Age : 25")
        print("Type : Savings")
class Xerox(Bank):
    def hell(self):
        super().person_3()
        pass
obj_1=Bank()
#obj_1._person_3()
print(dir(obj_1))
#obj_1._Bank__person_3()

