import mysql.connector

class DB:
    def __init__(self):
        #connect to the databse
        try:
            self.conn=mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='indigo1'
            )

            self.mycursor=self.conn.cursor()
            print('Connection established')
        
        except:
            print('Connection error')
    
    def fetch_city_name(self):
        city=[]

        self.mycursor.execute("""
        SELECT DISTINCT(Destination) FROM flights1
        UNION
        SELECT DISTINCT(Source) FROM flights1
        """)

        data=self.mycursor.fetchall()

        for item in data:
            city.append(item[0])
        return city
    
    def fetch_all_flights(self,source,destination):
        self.mycursor.execute("""
        SELECT Airline,Route,Dep_Time,Duration,Price FROM flights1
       WHERE Source='{}' AND Destination='{}'
        """.format(source,destination))

        data=self.mycursor.fetchall()
        return data
    
    def fetch_airline_frequency(self):
        airline=[]
        frequency=[]

        self.mycursor.execute("""
        SELECT Airline,COUNT(*) FROM flights1
        GROUP BY Airline
        """)
        data=self.mycursor.fetchall()
        for item in data:
            airline.append(item[0])
            frequency.append(item[1])

        return airline,frequency
    
    def busy_airport(self):
        city=[]
        frequency1=[]
        self.mycursor.execute("""
        SELECT Source ,COUNT(*) FROM
        ( SELECT Source FROM flights1
        UNION ALL
        SELECT Destination FROM flights1) t
        GROUP BY t.Source
        ORDER BY COUNT(*) DESC
        """)

        data=self.mycursor.fetchall()

        for item in data:
            city.append(item[0])
            frequency1.append(item[1])

        return city,frequency1
    
    def daily_frequency(self):
        date=[]
        frequency2=[]
        self.mycursor.execute("""
        SELECT Date_of_Journey,COUNT(*) FROM flights1
 GROUP BY Date_of_Journey
        """)

        data=self.mycursor.fetchall()

        for item in data:
            date.append(item[0])
            frequency2.append(item[1])

        return date,frequency2



          
    

