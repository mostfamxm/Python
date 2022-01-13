class Person:
    def __init__(self,name,age,id,gender):
        self.name=name
        if(age>0 and age<=120):
            self.__age=age
        if(len(id)==9):
            flag=False
            for c in id:
                if(isinstance(c,int)):
                    flag=True
                else :
                    flag=False
                if(flag ==True):
                    self.__id=id
        if(isinstance(gender,bool)):
            self.__isMale=gender
    @property
    def Age(self):
        return self.__age
    @Age.setter
    def Age(self,age):
        if(age>0 and age<=120):
            self.__age=age
    @property
    def ID(self):
        return self.__id
    @ID.setter
    def ID(self,id):
        if len(id)==9:
            flag=True
            for x in id:
                if(isinstance(x,int)):
                    flag=True
                else:
                    flag=False
                if(flag==True):
                    self.__id=id
    @property
    def IsMale(self):
        return self.__isMale
    @IsMale.setter
    def IsMale(self,b):
        if(isinstance(b,bool)):
            self.__isMale=b
    
    def print(self):
        print("name :",self.name,"age :",self.Age(),"id :",self.ID(),"is male: ",self.IsMale())                                                
class Worker(Person):
    def __init__(self,salary):
        if(isinstance(salary,int)):
            self.__salary=salary
    def __init__(self, name, age, id, gender):
        super().__init__(name, age, id, gender)        
    @property
    def Salary(self):
        return self.__salary
    @Salary.setter
    def Salary(self,s):
        if(isinstance(s,int)):
            self.__salary=s
    def print(self):
        print(super().print(),"the salry of the worker is: ",self.Salary())
class Student(Person):    
    def __init__(self,college,subject):
        if(isinstance(college,str)):
            self.__college=college
        if(isinstance(subject,str)):    
            self.__subject=subject

    def __init__(self, name, age, id, gender):
        super().__init__(name, age, id, gender)
    @property
    def College(self):
        return self.__college
    @College.setter
    def College(self,co):
        if(isinstance(co,str)):
            self.__college=co
    @property
    def Subject(self):
        return self.__subject
    @Subject.setter
    def Subject (self,Su):
        if(isinstance(Su,str)):
            self.__subject=Su
    def print(self):
        print(super().print(),"college name : ",self.College(),"subject: ",self.Subject())    
class Teacher(Person):
   
    def __init__(self,subject,years):
        if(isinstance(subject,str)):
            self.__subject=subject
        if(isinstance(years,int)):
            self.__years=years
    def __init__(self, name, age, id, gender):
        super().__init__(name, age, id, gender)        
    @property
    def Subject(self):
        return self.__subject
    @Subject.setter
    def Subject(self,s):
         if(isinstance(s,str)):
            self.__subject=s
    @property
    def Years(self):
        return self.__years
    @Years.setter
    def Years(self,y):
         if(isinstance(y,int)):
            self.__years=y

    def print(self):
        print(super().print(),"course name : ",self.Subject(),"years of experint: ",self.Years())
class Cinema:
    def __init__ (self,movieName,price):
        if(isinstance(movieName,str)):
           self.__movieName=movieName
        if(isinstance(price,int)):  
           if(price>=30 and price<=200):
                self.__price=price
        if(isinstance(self,Student)):
           self.studentDiscount=20
        if(isinstance(self,Teacher)):   
           self.teacherDiscount=10  
    @property
    def Price(self):
        return self.__price
    @Price.setter
    def Price(self,p): 
         if(isinstance(p,int)):  
           if(p>=30 and p<=200):
                self.__price=p
    @property
    def MovieName(self):
        return self.__movieName
    @MovieName.setter
    def MovieName(self,mn):
        if(isinstance(mn,str)):
            self.__movieName=mn
if __name__ =='__main__':
    c=Cinema("die hard",50)
    S=Student("john",19,"123564789",True)
    T=Teacher("anaa",28,"546789123",False)
    W=Worker("mark",32,"369852147",True) 
    p=[]
    def insertToArray(*arr):
        arr=[]
        arr.insert(0,S)
        arr.insert(1,T)
        arr.insert(2,W)
    insertToArray(p)
    def total(*cinema,**arr):
        count=0
        total=0
        st=0
        te=0
        wo=0
        for i in arr:
            if(isinstance (i,Student)):
                total+= (cinema.Price()-cinema.studentDiscount)
                count+=1 
                st+=1
            elif(isinstance(i,Teacher)):
                total+=(cinema.Price()-cinema.teacherDiscount)
                count+=1
                te+=1
            else :
                total+=cinema.Price()
                count+=1
                wo+=1
        return" total income :{total}movie price : {cinema.Price()}the number of people that watched the movie :{count}students that whatched the movie: {st}teachers that watched the movie :{te}workers that watched the movie : {wo}"
print(total(c,p))            


            
                   
                    
        