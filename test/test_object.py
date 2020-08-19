import posixpath
import unittest

import sbol3


class TestObject(unittest.TestCase):

    def setUp(self) -> None:
        sbol3.set_defaults()

    def test_trailing_slash(self):
        # A trailing slash on an object's identity should automatically be removed
        sbol3.set_homespace('http://example.org/sbol3')
        slash_identity = posixpath.join(sbol3.get_homespace(), 'c1', '')
        self.assertTrue(slash_identity.endswith(posixpath.sep))
        c = sbol3.Component(slash_identity)
        identity = slash_identity.strip(posixpath.sep)
        self.assertEqual(identity, c.identity)


if __name__ == '__main__':
    unittest.main()