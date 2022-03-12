class Student:
    def __init__(self, name): #initialize
        self.name = name
        print(f"{name} 학생이 물을 마십니다.")
        
    def __repr__(self): #represent
        return repr(self.name) 
    
    def do_introduction(self):
        print(f"안녕하세요, 제 이름은 {self.name}입니다.")
        
    def study(self, subject):
        print(f"{self.name} 학생은 {subject}을/를 공부 중입니다.")
        
class HighSchoolStudent(Student):
    def work(self):
        print(f"{self.name}은 고등학교에 갑니다.")
        
class AdultStudent(Student):
    def work(self):
        print(f"{self.name}은 회사에 갑니다.")
        
####
def work(student_type):
    if student_type == "고등학생":
        print("고등학교에 갑니다.")
    if student_type == "성인":
        print("회사에 갑니다.")
####        
        
student_one = Student("심재훈")
student_one.name
student_two = Student("한성용")
student_two.do_introduction()
student_two.study("파이썬")
        
    
student_three = HighSchoolStudent("임민석")
student_three.do_introduction()
student_three.work()

student_four = AdultStudent("박희찬")
student_four.do_introduction()
student_four.work()


####
class PublicTransportation:
    def __init__(self, type_, price):
        self.type_ = type_
        self.price = price
    
    def __repr__(self):
        return repr(self.type_)
    
    def move(self):
        print(f"{self.type_}을/를 타고 이동 중입니다.")
        
    def discount(self, age):
        if age < 20 or age > 65:
            self.price = int(self.price * 0.7)
            print(self.price)
            
class Subway(PublicTransportation):
    def is_in_traffic_jam(self, time):
        print("지금은 정체가 없습니다.")
        
class Automobile(PublicTransportation):
    def is_in_traffic_jam(self, time):
        if 18 <= time < 19:
            print("지금은 정체가 있습니다.")
        else:
            print("지금은 정체가 없습니다.")

class Taxi(Automobile):
    def discount(self, age):
        pass

        
transportation_one = Subway("지하철", 2000)
transportation_one.move()
transportation_one.discount(13)
transportation_two = Automobile("버스", 2500)
transportation_two.move()
transportation_three = Automobile("택시", 3000)
transportation_one.is_in_traffic_jam(18)
transportation_two.is_in_traffic_jam(18)