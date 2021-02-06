class Animals ():
  def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

  def print_name(self):
    print(self.name + " is " + self.age + " years old" + " and, its breed is a " + self.breed)

class Dogs (Animals):
  pass
  

class Cats (Animals):
  pass
  

cat = Cats ("tom" , "5", "scottish fold")
cat.print_name()

dog = Dogs("Snoopy" , "9", "beagle")
dog.print_name()
        
