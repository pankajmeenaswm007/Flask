import mysql.connector

class myclass:

    def __init__(self):
##       object 
        self.mydb=mysql.connector.connect(host="localhost",user="root",password="",database="login")
        

    def fire(self,qry):
        self.mycur=self.mydb.cursor()   ## object cursor set
        self.mycur.execute(qry)         ## cursor execute user query
        #return self.mycur

    def getdata(self,tab,name=""):   ##table show items
        if(len(name)>=1):
            qry="select * from "+tab+" where name='"+name+"'"
        else:
            qry="select * from "+tab+""
            
        self.fire(qry)
        mydata=self.mycur.fetchall()
        return mydata
        # rc=self.mycur.rowcount  ## table row count
        # if(rc>=1):
        #     for i in mydata:
        #         print(i)
        # else:
        #     print(name,"this data is not found")  



    def insert(self,tab,data=[]):
##        table insert data
        qry="insert into "+tab+" set Name='"+data[0]+"', Mobile='"+data[1]+"', Password='"+data[2]+"' ,image='"+data[3]+"'"
        print(qry)
        self.fire(qry)
        self.mydb.commit()


    def delete(self,tab,id1):
##       table me row delete 
        qry="delete from "+tab+" where id="+str(id1)+""
        self.fire(qry)
        self.mydb.commit()
        # self.getdata(tab)

    def update(self,tab,d=[]):
##      update table items  
        qry="update "+tab+" set Password='"+d[1]+"' where Mobile='"+d[0]+"'"
        print(qry)
        self.fire(qry)
        self.mydb.commit()
        # self.getdata(tab)

    def drop(self,tab):
##        qry="drop table "+tab+""  ## delete table
        qry="TRUNCATE table tab"    ## delete table all data and not delete structure
        print(qry)
        self.fire(qry)
        self.mydb.commit()

    def createTable(self,tab):
##     new table create   
        qry="create table "+tab+" (id int(10) primary key auto_increment,name varchar(255),city varchar(250),mobile int(10))"
        print(qry)
        self.fire(qry)
        self.mydb.commit()
        

        
    
#ob=myclass()  ## object class
# tab=input("enter table name=")
##name=input("enter a search user name=")
##id=int(input("enter id no="))
##ob.getdata(tab,name)
# id1=int(input("enter user id="))
# n=input("enter user name=")
# c=input("enter city=")
# s=int(input("enter sallary="))
# d=[id1,n,c,s]
# ob.insert(tab,d)

##ob.getdata(tab)
    
##ob.delete(tab,9)

##ob.update(tab,d)

##ob.drop(tab)

##ob.createTable(tab)
