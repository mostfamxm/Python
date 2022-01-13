
class Person :
    def __init__(self,name,Id,gender,age) :
        self.name=name
        if(age>0 and age <=120):
            self.__age=age
        flag=False
        if len(Id)==9:
          for x in Id:
            if(x.isdigit()):
                flag=True
            else :
                flag=False    
        if(flag==True):
            self.__Id=Id    
        if(gender==True):
           gender=True
           self.__ismale=gender
        else :
             gender=False      
             self.__ismale=gender
    @property
    def Age(self):
        return self.__age
    @Age.setter 
    def Age(self,age):
           if(age>0 and age <=120): 
               self.__age=age
    @property
    def ID(self):
        return self.__Id
   
    @ID.setter 
    def ID(self,ID):
      flag=False
      if len.ID==9:
        for x in ID:
            if(type(x)==int):
                flag=True
            else :
                flag=False    
        if(flag==True):
            self.__Id=ID

    @property
    def IsMale(self):
        return self.__ismale
   
    @IsMale.setter 
    def isMale(self,Gender):
       if(Gender==True):
        Gender=True
        self.__ismale=Gender
       else : Gender=False                       

    def print(self):
         print("name :",self.name,"age :",self.Age,"id :",self.ID,"is male: ",self.IsMale,)
class Worker(Person):

    def __init__(self, salary):
        self.__salary=salary

    def __init__(self, name, Id, gender, age):
        super().__init__(name, Id, gender, age)
    @property
    def Salary(self):
        return self.__salary
    @Salary.setter
    def Salary(self,salary):
        if(salary>=0):
            self.__salary=salary    
    def print(self):
        print(super().print(),"the salry of the worker is: ",self.Salary())
class Student(Person):
    def __init__(self,college,subject):
          self.__college=college
          self.__subject=subject    
    def __init__(self, name, Id, gender, age):
        super().__init__(name, Id, gender, age)
    @property
    def College(self):
        return self.__college
    @College.setter
    def College(self,co):
        self.__college=co    
    @property
    def Subject(self):
        return self.__subject
    @Subject.setter
    def Subject(self,su):
        self.__subject=su     
    def print(self):
        print(super().print(),"college name : ",self.College(),"subject: ",self.Subject())         
class Teacher(Person):
    def __init__(self,course,years):
        self.__course=course
        self.__years=years
    def __init__(self, name, Id, gender, age):
        super().__init__(name, Id, gender, age)        
    @property
    def Course(self):
        return self.__course 
    @Course.setter
    def Course(self,cu):
        self.__course=cu
    @property
    def Years(self):
        return self.__years
    @Years.setter
    def Years(self,y):
        if(type(y)==int):
            self.__years=y    
class Cinema:
    def __init__ (self,movieName,price):
        self.movieName=movieName
        if(price>=30 and price<=200):
           self.__price=price
        if(isinstance(self,Student)):
           self.__studentDiscount=20
        if(isinstance(self,Teacher)):   
           self.__teacherDiscount=10
    @property
    def Price(self):
        return self.__price 
    @Price.setter
    def Price(self,p):
        int(p)
        if(p>=30 and p<=200):
           self.__price=p
    @property
    def SD(self):
        return self.__studentDiscount 
    @SD.setter
    def SD(self,SD):
        if(isinstance(self,Student)):
            self.__studentDiscount=SD
    @property
    def TD(self):
        return self.__teacherDiscount 
    @TD.setter
    def TD(self,TD):
        if(isinstance(self,Teacher)):
            self.__teacherDiscount=TD        
if __name__  == '__main__':
    c=Cinema("die hard",50)
    S=Student("john","123654987",True,19)
    T=Teacher("anaa","987564231",False,28)
    W=Worker("mark","546987123",True,32)

    p=[]
    def insertToArray(arr):
        arr=[]
        arr.insert(0,S)
        arr.insert(1,T)
        arr.insert(2,W)

    insertToArray(p)

    def total(cinema,arr):
        
        count=0
        total=0
        st=0
        te=0
        wo=0
        for i in arr:
            if(isinstance (arr[i],Student)):
                total+= (cinema.Price()-cinema.SD())
                count+=1 
                st+=1
            elif(isinstance(arr[i],Teacher)):
                total+=(cinema.Price()-cinema.TD())
                count+=1
                te+=1
            else :
                total+=cinema.Price()
                count+=1
                wo+=1

        return"total income :{total}movie price : {cinema.Price()}the number of people that watched the movie :{count}students that whatched the movie: {st}teachers that watched the movie :{te}workers that watched the movie : {wo}"

print(total(c,p))

            

         
    


