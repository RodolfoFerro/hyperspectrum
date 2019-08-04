#Ejercicio 1


class student:
  def __init__(self, age, name, topics):
    self.age = age
    self.name = name
    self.topics = topics
    if age < 18:
      self.underage = True
    else:
      self.underage = False
    school.append(self)

class directory:
  def __init__(self, list):
    for x in list:
      print (f"Age: {x.age}")
      print (f"Name: {x.name}")
      for y in x.topics:
        print (f"Topic of interest: {y}")
      if x.underage:
        print("Underage")
      else:
        print("Not underage")
      print ("")

school = []        
jesus = student(19, "Jesús", ["Math", "Coding", "Robotics"])
ramon = student(16, "Ramón", ["Mechanics", "FRC", "Robotics"])

directory(school)