import peewee
import peewee_async
import datetime
import time

#Creating database connection using SQLite
db = peewee.SqliteDatabase("assignment1.db")

#Creating base class to be inherited by agent and handler classes
class BaseModel(peewee.Model):
    class Meta:
        database = db

#Creating Agent class with attributes as required in the table
class Agent(BaseModel):
    agent_id = peewee.CharField(unique=True)
    created_date = peewee.DateField(default= '22-3-2019')

#Creating Handler class with attributes as required in the table
class Handler(BaseModel):
    handler_uuid = peewee.CharField(unique=True)
    agent_id = peewee.ForeignKeyField(Agent)
    system_id = peewee.CharField()
    version = peewee.CharField(default='3.7')
    registered_time = peewee.DateField(default=datetime.datetime.now())

#Creating tables for agent and handler if it doesnt exist and making entries in the tables
#for us to fetch on querying
if not Agent.table_exists():
    db.create_table(Agent)
    agent_details =[{'agent_id':1}, {'agent_id': 2}, {'agent_id':3}, {'agent_id':4}]
    Agent.insert_many(agent_details).execute()

if not Handler.table_exists():
    db.create_table(Handler)
    handler_details = [{'handler_uuid':"Alpha", 'agent_id':1, 'system_id':'abc'},
                       {'handler_uuid': "Bravo", 'agent_id': 2,'system_id': 'def'},
                       {'handler_uuid': "Charlie", 'agent_id': 3, 'system_id': 'ghi'},
                       {'handler_uuid': "Delta",'agent_id': 4,'system_id': 'jkl'},
                       {'handler_uuid': "Epsilon", 'agent_id': 5, 'system_id': 'mno'}]
    Handler.insert_many(handler_details).execute()
