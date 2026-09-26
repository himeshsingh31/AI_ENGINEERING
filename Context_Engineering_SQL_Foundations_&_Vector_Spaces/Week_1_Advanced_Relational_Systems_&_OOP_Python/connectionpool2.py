import mysql.connector as mc
import threading as th
import time as t


class connection:
    def __init__(self,status):
        self.conn = mc.connect(
            host ="localhost",
            user ="root",
            password ="Honey3156$@",
            database = "corporate_activity_db"
        )

        self.status = "vacant"


class pool:
    def __init__(self):
        c1 = connection("status")
        c2 = connection("status")
        c3 = connection("status")
        c4 = connection("status")
        c5 = connection("status")
        c6 = connection("status")
        c7 = connection("status")
        c8 = connection("status")
        c9 = connection("status")
        c10 = connection("status")



        self.connections = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]

    def getconnection(self):
        for i in self.connections:
            if i.status == "vacant":
                i.status = "busy"
                return i 

        return None


class result:
    def __init__(self,pool):
        self.pool = pool


    def __enter__(self):
        self.connection = self.pool.getconnection()
        if(self.connection == None):
            raise Exception("SERVER IS BUSY !!")

        self.cursor = self.connection.conn.cursor()
        return self.cursor
    


    def __exit__(self,exc_type,exc_value,traceback):
        self.connection.status = "vacant"
        self.cursor.close()



x =t.time()
poo = pool()
print("the time in making the pool is : ",t.time()-x)

r =[]

def getconn():
    tm = t.time()
    with result(poo) as p:
        p.execute("select log_id ,action,status,created_at from activity_logs where user_id  = 10 limit 1;")
        x = p.fetchall()
    r.append((x,t.time()-tm))


 
         

threads =[]

z = t.time()
for i in range(200):
    thr = th.Thread(target = getconn)
    threads.append(thr)
    thr.start()

print("the timing in execution of all the requests is : ",t.time()-z)

for i in threads:
    i.join()


for i in r:
    print(i[0],i[1])    




        


    
    






