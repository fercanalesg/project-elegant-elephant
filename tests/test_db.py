import unittest
from peewe import *
from app import TimeLinePost

MODELS = [TimeLinePost]

# use an in-memory SQLite for tests.
test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        # Bind model classes to test db. Since we have a complete list of
        # all models, we do not need to recursively bind dependencies.
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)
    def tearDown(self):
        # Not strictly necessary since SQLite in-memory databases only live
        # for the duration fo the connection, and in the next step we close 
        # the connection...but a good practice all the same.
        test_db.drop_tables(MODELS)

        # Close connection to db.
        test_db.close()

    def test_timeline_post(self):
        # CReate 2 timeline posts
        first_post = TimelinePost.create(name='John Doe',
        email = 'john@example,com', content='Hello World, I\'m John!' )
        assert first_post.id == 1
        second_post = TimelinePost.create(name='Jane Doe', 
        email = 'jame@example.com', content = 'Hello worl, I\'m Jane! ')
        assert second_post.id == 2
        
