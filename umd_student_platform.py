
""" A platform for UMD I-School students to plan their schedules. """

class Student:
    """ An instance of a UMD Information Science student.

    Attributes:
        student_id (int): the unique identifying number of the student
        student_name (str): the name of the student
        grad_year (int): the intended graduation year of the student
    """
    
    def __init__(self, student_id, student_name, grad_year, classes_taken):
        """ Assigns attributes to objects, instantiates a student class

        Args:
            student_id (int): the unique identifying number of the student
            student_name (str): the name of the student
            grad_year (int): the intended graduation year of the student
            classes_taken (list of str) : the list of classes the student has
              taken 
        
        Side effects:
            creates global variables, specifically student_id, student_name, 
              grad_year, and classes_taken
        """
        self.student_name = student_name
        self.student_id = student_id
        self.grad_year = grad_year
        self.classes_taken = classes_taken


    def greet(self):
      """ This method takes a student's name and and student's identification 
      number to create a customized greeting based on the inputs of the student 
      trying to use our program.

      Args:
        self (Student) : an instance of the Student Class

      Returns: 
        welcome (str) : This method returns our welcome statements with the 
          student's name and identification number in the greeting.
      """
      welcome = input(f'Welcome, {self.student_name} (UID: {self.student_id}),'+
                    ' to I-School help! What can we assist you with? ' +
                    'Please choose from the following list of options: \n' +
<<<<<<< HEAD
                    'Benchmark I Courses \nBenchmark II Courses \nCore Courses'+
                    '\nMajor Specializations \nCredit Counter '+
                    '\nUpdate Classes Taken \nChange Name or '+
=======
                    'Benchmark I \nBenchmark II \nCore Courses'+
                    '\nMajor Specializations \nCredit Counter \nAdvising '+
                    'Contacts \nUpdate Classes Taken \nChange Name or '+
>>>>>>> 8dea784822e2fc14be859d1a2a35a632a259c845
                    'Graduation Year\n')
      return welcome
   

    def get_classes(self):
      """ This method uses a loop to allow students to enter the classes that 
      they have taken that are part of the Information Science major, stores 
      them in a list, and then returns the list with the classes in it. 

      Returns: 
        student_classes (list) : the inputted classes that the student has 
        taken in the Information Science major. 
      """
      count = 0
      self.classes_taken = []
      while count == 0:
        classes = input("Please enter all of the INST-related classes that " +
                  "you have taken, one at a time, in the following format:" +
                  "CLAS 100 \n For example, INST 201.\n\n Enter stop when you" +
                  " have finished. Don't forget to include I-School major " +
                  "benchmarks, like math and psychology courses! Thank you! \n")
        if classes.lower() != "stop":
          self.classes_taken.append(classes)
        else:
          count += 1     
      return self.classes_taken


    def benchmark_I(self):
      """ 
      """
      math_flag = True
      psych_flag = True

      if 'MATH 115' not in self.classes_taken:
        math_flag = False
      elif 'PSYC 100' not in self.classes_taken:
        psych_flag = False

      if math_flag and psych_flag:
        print(f'You have completed all of your Benchmark I courses! ' +
              f'Congratulations, {self.student_name}!')
      else:
        print('You have not completed the Benchmark I requirements.')
        if math_flag == False:
          print('You have not taken MATH 115 or higher.')
        if psych_flag == False:
          print('You have not taken PSYC 100.')
  

    def benchmark_II():
      """
      """
      stat_flag = True
      inst126_flag = True
      inst201_flag = True

      if 'STAT 100' not in self.classes_taken:
        stat_flag = False
      elif 'INST 126' not in self.classes_taken:
        inst126_flag = False
      elif 'INST 201' not in self.classes_taken:
        inst201_flag = False
    
    
    def core_courses(self):
      """
      """

      core_courses = {'INST 311': True, 'INST 314': True, 'INST 326': True, 
                      'INST 327': True, 'INST 335': True, 'INST 346': True, 
                      'INST 352': True, 'INST 362': True}
      
      if 'INST 311' not in self.classes_taken:
        core_courses['INST 311'] = False
      if 'INST 314' not in self.classes_taken:
        core_courses['INST 314'] = False
      if 'INST 326' not in self.classes_taken:
        core_courses['INST 326'] = False
      if 'INST 327' not in self.classes_taken:
        core_courses['INST 327'] = False
      if 'INST 335' not in self.classes_taken:
        core_courses['INST 335'] = False
      if 'INST 346' not in self.classes_taken:
        core_courses['INST 346'] = False
      if 'INST 352' not in self.classes_taken:
        core_courses['INST 352'] = False
      if 'INST 362' not in self.classes_taken:
        core_courses['INST 352'] = False
        
      not_taken = []
      for course in core_courses:
        if core_courses[course] == False:
          not_taken.append(course)
          
      if len(not_taken) == 0:
        print("You have completed all core courses!")
      else:
        print("You must still complete the following core courses: ")
        print(*not_taken, sep = '\n')
        
    def specializations(specialization):
      """
      """


    def credit_counter(self):
      """
      """
      credits = len(self.classes_taken) * 3
      return credits
      


    #def update_classes(self):
     # update = input('Thank you for updating your classes taken! This will '+
      #            ' help us help you! \n Like before, please enter all of the '+
       #           'INST-related classes that you have taken, one at a time, ' +
        #          'in the following format: CLAS 100 \n For example, ' +
         #         "INST 201.\n\n Enter stop when you have finished. Don't " +
          #        'forget to include I-School major benchmarks, like math and' +
           #       " psychology courses! Thank you! \n")
     # if .lower() != "stop":
      #    self.classes_taken.append(classes)
      #else:
      #  count += 1
      #self.write_to_file()

    def change_name_gradyear():
      options = input('Here, you can change your name and your expected ' +
                'graduation year. \nTo update your name, type name. To update' +
                ' your graduation year, type grad year. To update both, ' +
                'type both. Thank you!')
      if options.lower() == 'name':
        self.student_name = input("Please enter your full name: ")
      
      grad_year = input('Please enter your expected graduation year: ')
      self.write_to_file()



    def write_to_file(self):
      """
      """
      with open('Students/'+ self.student_id, 'w+', encoding = 'utf-8') as f:
        class_list = ','.join(self.classes_taken)
        new_file = self.student_name + ',' + self.grad_year + ',' + class_list
        f.write(new_file)



def load_from_file(student_id):
  """
  """
  with open('Students/'+ student_id, 'r', encoding = 'utf-8') as f:
    for line in f:
      attributes = line.strip().split(',')
      student_name = attributes[0]
      grad_year = attributes[1]
      taken_classes = attributes[2:]
      class_instance = Student(student_id, student_name, grad_year, taken_classes)
      return class_instance
  

def main():
  """
  """
  while True:

    been_here = input('Hi! Welcome to the UMD I-School Student Platform!\n' +
                    'Have you been here before? \n')
    if been_here.lower() == 'no':
      student_name = input("Please enter your full name: ")
      student_id = input("Please enter your 9 digit student ID number: ")
      grad_year = input('Please enter your expected graduation year: ')
      classes_taken = []
      class_instance = Student(student_id, student_name, grad_year, classes_taken)
      class_instance.get_classes()
      class_instance.write_to_file() 
      break

    elif been_here.lower() == 'yes':
      student_id = input("Please enter your 9 digit student ID number:  ")
      class_instance = load_from_file(student_id)
      break
    else:
      print('Please enter yes or no')
  
  option = class_instance.greet()
    
  if option == "Benchmark I":
      print(class_instance.benchmark_I())  
  elif option == 'Benchmark II':
      print(class_instance.benchmark_II())
<<<<<<< HEAD
  elif option == 'Update Classes':
    print(class_instance.update_classes())
=======
  elif option == 'Change Name':
      print(class_instance.update_classes())
>>>>>>> 8dea784822e2fc14be859d1a2a35a632a259c845
  elif option == 'Update Name or Grad Year':
      print(class_instance.change_name_gradyear())
  elif option == "Core Courses":
      print(class_instance.core_courses())
  elif option == "Specializations":
      class_instance.get_classes()
      print("S") 
  elif option == "Advising Contacts":
      print("A") 
  elif option == "Credit Counter":
      print('You have completed '+ str(class_instance.credit_counter()) + 
              ' INST credits.')
  else:
      print("I'm sorry, we don't know how to help you with that.")


if __name__ == "__main__":
  main()