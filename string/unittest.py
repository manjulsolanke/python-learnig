import unittest

class TestS3(unittest.TestCase):

    def test_bucket_name_value(self):
        bucket = 'thisistestbucketname'
        self.assertEqual(bucket, 'thisistestbucketname')

    def test_region_value(self):
        region = 'us-east-1'
        self.assertEqual(region, 'us-east-1')

    def test_bucket_name_is_string(self):
        bucket = 'thisistestbucketname'
        self.assertTrue(type(bucket), str)

    def test_region_is_string(self):
        region = 'us-esat-1'
        self.assetTrue(type(region), str)


if __name__ == '__main__':
    unittest.main()
