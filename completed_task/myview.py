from aiohttp import web
import asyncio
import peewee
from peewee_database import Agent, Handler
import logging

#index function receives the request at localhost address
#if the request has a valid agent id, the corresponding handler uuid is returned
logging.basicConfig(filename= 'index.log', format = '%(asctime)s - %(message)s', datefmt='%a, %d %b %Y %H:%M:%S', level=10)

async def index(request):

     if request.body_exists:
         d = await request.json()
         logging.info('request arrived with data {}'.format(d))
         agent_id = d['agent_id']
         sys_id = d['system_id']

         try:
             logging.info('looking for handler uuid')
             hand = Handler.get(Handler.agent_id == agent_id and Handler.system_id == sys_id).handler_uuid
             if hand:
                 uuid_dict = dict()
                 uuid_dict['handler_uuid'] = hand
                 return web.json_response(uuid_dict)

         except Exception as e:
             print (e)
             agent_obj = Agent()
             agent_obj.create(agent_id = agent_id)
             txt = "Record created now for agent_id: {0} and created date is {1}. " \
                   "Handler uuid does not exist".format(agent_id, agent_obj.created_date)
             return web.Response(text=txt)

     else:
         return web.Response(text = "No agent id provided.")

#function setroutes adds method of post
def setroutes(app):
    app.router.add_post('/', index)

app = web.Application()
setroutes(app)
web.run_app(app)

