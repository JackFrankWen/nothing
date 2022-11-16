from GR86.chassis.database.mongdb  import mongo
from GR86.chassis.spider.tushare import Tushare


class Task:
    def __init__(self):
        self.m = mongo()
        self.t = Tushare()
        pass

