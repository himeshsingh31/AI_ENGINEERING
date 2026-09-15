import mysql.connector
import time as t
import threading



class mydbconnection:

    def __init__(self,status):
      self.connection = mysql.connector.connect(

      host = "localhost",
      user = "root",
      password = "******",
      database = "*****"
      )
      self.status = status

    



class pool:

# this section is proudly made by AI.. due to repition task and i am also feeling sleepy currently....
   def __init__(self):
    pool1 = mydbconnection("vacant")
    pool2 = mydbconnection("vacant")
    pool3 = mydbconnection("vacant")
    pool4 = mydbconnection("vacant")
    pool5 = mydbconnection("vacant")
    pool6 = mydbconnection("vacant")
    pool7 = mydbconnection("vacant")
    pool8 = mydbconnection("vacant")
    pool9 = mydbconnection("vacant")
    pool10 = mydbconnection("vacant")


    self.connections = [
        pool1, pool2, pool3, pool4, pool5,
        pool6, pool7, pool8, pool9, pool10
    ]
#////////////////////////////////////////////////////// 


   def getconnection(self):
        for i in self.connections:
           if i.status =="vacant":
              i.status = "busy" 
              return i
        return None    
            


timing =[]
class request:
   def __init__(self,pool):
      self.pool = pool
      self.connection = None

   def __enter__(self):
        self.starting_time = t.time()
        self.connection = self.pool.getconnection()
        if self.connection == None:
           raise Exception("Server is busy!!")

        self.cursor = self.connection.connection.cursor() 
        return self.cursor


   def __exit__(self,exc_type, exc, tb):
      self.cursor.close()
      self.connection.status = "vacant"
              
x = t.time()
hook = pool()
print("Time taken for making a pool  is ", t.time()-x)


result =[]
#  making a replica of the fake connections requets ...
def makerequest():
 time = t.time()
 with request(hook) as connection:
   connection.execute("select *  from employees")
   x = connection.fetchall()
   
   result.append((x,t.time()-time))
   



threads = []

for i in range(50):
   th = threading.Thread(target = makerequest)
   threads.append(th)
   th.start()

for x in threads:
   x.join()



for i in result:
   print("result :",i[0])
   print("timing :",i[1])

# //////////////////  
