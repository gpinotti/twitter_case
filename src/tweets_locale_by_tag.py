import logging
import configs
import pymongo


# PARAMS HASHTAGS_LIST
HASHTAGS_LIST = configs.HASHTAGS_LIST

MONGO_COL_TWEETS = configs.MONGO_COL_TWEETS
MONGO_COL_LOCALE = configs.MONGO_COL_LOCALE



# FUNCTION DEFINITIONS


def locale_by_tag(db_connection, mongo_col_tweets, mongo_col_locale):
    tweet_col = db_connection[mongo_col_tweets]
    locale_col = db_connection[mongo_col_locale]

    count_documents = locale_col.count()

    if not count_documents == 0:
        logging.info("Collection \"{0}\" is not empty. Performing cleanup".format(mongo_col_locale))
        clean_collection = configs.cleanup_collection(db_connection, mongo_col_locale)
        logging.info("Collection cleanup: {0} documents were deleted from the collection.".format(clean_collection))

    locale_by_tag = tweet_col.aggregate([{"$group":{"_id":{"lang":"$lang", "hashtag":"$hashtag"}, "count":{"$sum":1}}},{"$sort":{"count":1}}])
    x = locale_col.insert_many(locale_by_tag)

    return (len(x.inserted_ids))



# RUN APPLICATION


def main():
    mongodb_connection = configs.mongodb_connect()
    tweets_locale_by_tag = locale_by_tag(mongodb_connection, MONGO_COL_TWEETS, MONGO_COL_LOCALE)

if __name__ == "__main__":
#    configs.logging_basic_config()
    main()
