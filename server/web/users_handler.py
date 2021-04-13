# -*- coding: iso-8859-15 -*-

import tornado.web
import tornado.escape
import logging

logger = logging.getLogger(__name__)


class UsersHandler(tornado.web.RequestHandler):
    def initialize(self, db=None):
        self.db = db

    # @tornado.gen.coroutine
    async def get(self, _slash, email):
        mongo = self.application.mongo
        db = mongo.prueba

        query = {}
        if email is not None:
            query = {
                'email': email
            }

        responses = []
        async for user in db.users.find(query):
            user['_id'] = str(user['_id'])
            responses.append(user)

        self.set_header('Content-Type', 'text/javascript')
        self.write(tornado.escape.json_encode(responses))
        # self.render('../static/index.html')

    # @tornado.gen.coroutine
    async def post(self, _slash, _email):
        if _email is not None:
            self.set_status(403)
        else:
            data = tornado.escape.json_decode(self.request.body)
            db = self.application.mongo.prueba

            logger.info(f'Body keys: {list(data.keys())}')
            logger.info(f"data[key2] = {data['key2']}")

            insert_id = await db.users.insert_one(data)
            self.set_header('Content-Type', 'text/javascript')
            self.write(tornado.escape.json_encode(
                {"_id": str(insert_id.inserted_id)}))

    async def put(self):
        self.set_status(403)
