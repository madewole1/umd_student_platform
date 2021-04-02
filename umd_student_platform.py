"""A platform for UMD students to look up prerequistes for classes
"""

class Student:
    """This class will take the student't name, as well as their prerequisites.
    
    Attributes:
        name(str): name of student 
        prerequisites(set): prerequisites the student has 
    """
    def __init__(self, name, prerequistes):
       self.name = name
       self.prerequistes = set()

      
