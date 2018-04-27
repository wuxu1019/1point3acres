class Person(object):

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def __str__(self):
        return self.firstname + " " + self.lastname

class Employee(Person):
    '''here is the doc'''
    data = "okok"

    def __init__(self, first, last, staffnum):
        super(Employee, self).__init__(first, last)
        self.staffnumber = staffnum


x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "1007")

print x
print y
if not hasattr(x, 'age'):
    setattr(x, 'age', 4)
if not hasattr(y, 'age'):
    setattr(y, 'age', 10)

print getattr(x, 'age')
print getattr(y, 'age')

print Employee.__doc__
print Employee.__bases__