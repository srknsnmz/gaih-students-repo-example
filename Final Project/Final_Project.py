class Employee():
    
    def __init__(self,name, age): 
        self.name = name
        self.age = age
        self.language = []

    def addLanguage(self,new_lang):
        self.language.append(new_lang)
    

    def showInfo(self):
        print(self.name + " is " + self.age + " years old")
        for i in self.language: 
          print("language spoken: " + i)

class manager(Employee):

   
    def __init__(self,name, age):
        super().__init__(name, age)
       
       
    def showInfo(self):
        super().showInfo()
        
    
ahmet = Employee("ahmet","23")
mehmet = Employee("mehmet","29")
ayse = Employee("Ayse","35")
zeynep = manager("Zeynep","35")
ahmet.addLanguage("Turkish"),ahmet.addLanguage("English"),
mehmet.addLanguage("English"),mehmet.addLanguage("Turkish")
ayse.addLanguage("English"),ayse.addLanguage("Turkish")
zeynep.addLanguage("Turkish"),zeynep.addLanguage("English"),zeynep.addLanguage("French"),zeynep.addLanguage("Spanish")


ahmet.showInfo()
mehmet.showInfo()
ayse.showInfo()
zeynep.showInfo()
