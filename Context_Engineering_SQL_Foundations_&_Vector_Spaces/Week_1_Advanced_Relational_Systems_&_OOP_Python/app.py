from models import Users,engine
from sqlalchemy.orm import sessionmaker

Session  = sessionmaker(bind = engine)

session = Session()



#creating of data.. 

user  =  Users(Name = "Himesh singh", Age = 20)
user_1 = Users(Name = "Daulat jadam", Age = 21)
user_2 = Users(Name = "Kapil kumar", Age = 25)
user_3 = Users(Name = "Dishant singh", Age = 20)
user_4 = Users(Name = "Vishal gehlot", Age = 26)

# session.add(user)
session.add_all([user,user_1,user_2,user_3,user_4])
session.commit()



#read of data..
user = session.query(Users).all()
print(user)
print(user[0])

user = user[0]
print(user.id)
print(user.Name)
print(user.Age)


user = session.query(Users).filter_by(Age = 20).all()

for i in user:
    print(i.Name)


# #updation of data
# user = session.query(Users).all()
# user[0].Name = "Rahul yadav"

# print(user[0].Name)



#deletion of data ....

# for i in user:
#  session.delete(i)
# session.commit()


