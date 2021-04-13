# -*- coding: iso-8859-15 -*-

import os.path as osp
import tornado.web
import tornado.escape
import logging

logger = logging.getLogger(__name__)

HERE = osp.dirname(osp.dirname(osp.abspath(__file__)))
static = osp.join(HERE, 'static')


class ImageHandler(tornado.web.RequestHandler):
    def initialize(self, db=None):
        self.db = db

    # @tornado.gen.coroutine
    async def get(self, id):
        with open(osp.join(static, 'prueba.png'), 'rb') as f:
            image_bytes = f.read()
        self.set_header('Content-Type', 'image/png')
        self.write(image_bytes)
        # self.write(tornado.escape.json_encode(responses))
        # self.render('../static/index.html')

    # @tornado.gen.coroutine
    async def post(self, _slash, _email):
        self.set_status(403)

    async def put(self):
        self.set_status(403)
