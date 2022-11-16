import pymongo


class mongo:

    def __init__(self):
        # ts.set_token('18d06f6b9689112d57777972863107f8f53ffde39f7e7d21089cfbd7')

        self.client = pymongo.MongoClient("localhost", 27017)

    def get_all_data(self):
        return self.client.list_database_names()

    def get_client(self):
        return self.client
