# 🎓 Student Management System (Python OOP)

A simple Python project demonstrating Object-Oriented Programming (OOP) concepts by managing student details, calculating percentage, and displaying results.

---

This project demonstrates **Object-Oriented Programming (OOP)** concepts in Python by building a simple Student Management System.

It allows you to:
- Store student details  
- Calculate total marks  
- Compute percentage  
- Display Pass/Fail result  

---

## 📂 Project Structure
student.py # Contains Student class

student_client.py # Runs the program (client code)


---

## 🧠 Code Explanation

### 🔹 student.py

This file defines the **Student class** which contains all the logic.

#### ✅ Constructor (`__init__`)
```python
def __init__(self, name, age, marks, no_of_sub):
    self.name = name
    self.age = age
    self.no_of_sub = no_of_sub
    self.__marks = marks

Initializes student details
Uses data hiding (__marks) to protect marks
##
def _total_marks(self):
    return sum(self.__marks)
->Calculates total marks using Python’s built-in sum() function
##
def _total_percentage(self):
    return (self._total_marks() / (self.no_of_sub * 100)) * 100
->Computes percentage based on total marks and number of subjects
##
def display(self):
    print(self.name, self.age)
->Displays basic student details
##
def result(self):
    self.display()
    percentage = self._total_percentage()
    print(f'Percentage : {percentage:.1f}')
    print('Pass' if percentage > 40 else 'Fail')

->Calls display method
->Calculates percentage
->Prints final result (Pass/Fail)


```
output:


<img width="181" height="71" alt="Screenshot 2026-04-09 010027" src="https://github.com/user-attachments/assets/e3e2cd01-bf7b-4f34-aa1b-9c6246347b5b" />








