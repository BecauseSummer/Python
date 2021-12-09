# -*- coding: utf-8 -*-
from . import db
from pymongo.collection import Collection


class ImageCollection(object):
    COL_NAME = 'ImageCollection'
    col = Collection(db, COL_NAME)
    class Field(object):
        _id = '_id'
        url = 'url'
        update = 'update'
        imagesList = 'imagesList'
        zhihu_type = 'zhihu_type'
        origin = 'origin'
    class ZhihuTypeField(object):
        collection  = 0
        question  = 1
    class OriginField:
        zhihu = 0
        douban = 1
        other = 2