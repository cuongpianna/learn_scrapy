import pymongo


class MongoPipeline(object):

    collection_name = 'tc_posts'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'tc_scraper')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    # def process_item(self, item, spider):
    #     self.db[self.collection_name].insert_one(dict(item))
    #     return item

    def process_item(self, item, spider):
        self.db[self.collection_name].find_one_and_update(
            {"url": item["url"]},
            {"$set": dict(item)},
            upsert=True
        )
        return item