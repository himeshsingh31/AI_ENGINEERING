import mysql.connector
import time as t
import threading



# =============================================================================
# Basic Database Connection Pool Demonstration
# Demonstrates connection pre-allocation, status tracking ('vacant' vs 'busy'),
# custom context manager for automatic checkout/checkin, and thread simulation.
# =============================================================================

# Represents a single database connection along with its availability state
class mydbconnection:

    def __init__(self,status):
      self.connection = mysql.connector.connect(

      host = "localhost",
      user = "root",
      password = "Honey3156$@",
      database = "corporate_activity_db"
      )
      self.status = status

    



# Connection Pool Manager: holds and allocates pre-established database connections
class pool:

# this section is proudly made by AI.. due to repition task and i am also feeling sleepy currently....
   def __init__(self):
       # Pre-initialize a fixed pool of 10 database connections
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



   # Search for and check out the first available ('vacant') connection
   def getconnection(self):
        for i in self.connections:
           if i.status =="vacant":
              i.status = "busy" 
              return i
        return None    
            


timing =[]

# Context Manager: Handles borrowing a connection from the pool and returning it safely
class request:
   def __init__(self,pool):
      self.pool = pool
      self.connection = None

   # Acquire a connection from the pool and create an active cursor
   def __enter__(self):
        self.starting_time = t.time()  
        self.connection = self.pool.getconnection()
        if self.connection == None:
           raise Exception("Server is busy!!")

        self.cursor = self.connection.connection.cursor() 
        return self.cursor


   # Close the cursor and release the connection back to the pool ('vacant')
   def __exit__(self,exc_type, exc, tb):
      self.cursor.close()
      self.connection.status = "vacant"
              
# Benchmark: Measure the time required to initialize and establish the pool
x = t.time()
hook = pool()
print("Time taken for making a pool  is ", t.time()-x)


result =[]

# Worker task: Simulates an incoming client request executing a database query
x =0
def makerequest():
 time = t.time()
 with request(hook) as connection:
   connection.execute("select *  from users where user_id = 10")
   x = connection.fetchall()
   
   result.append((x,t.time()-time))
   




# Simulate 50 concurrent incoming requests using worker threads
threads = []

for i in range(200):
   th = threading.Thread(target = makerequest)
   threads.append(th)
   th.start()

for x in threads:
   x.join()



# Print query results and round-trip execution timing for completed requests
for i in result:
   print("result :",i[0])
   print("timing :",i[1])

# =============================================================================
# End of connection pool demonstration
# =============================================================================


print(t.time())