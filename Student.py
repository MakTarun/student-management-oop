```
#data hiding

class Student:
    def __init__(self,name,age,marks,no_of_sub):
        self.name=name
        self.age=age
        self.no_of_sub=no_of_sub
        self._marks=marks

    def _total_marks(self):
        return sum(self._marks)
    def _total_percentage(self):
        return (self._total_marks()/(self.no_of_sub*100))*100
    def display(self):
        print(self.name,self.age)
    def result(self):
        self.display()
        percentage=self._total_percentage()
        print(f'Percentage : {percentage: .1f}')
        print('Pass' if percentage>40 else 'Fail')

```
