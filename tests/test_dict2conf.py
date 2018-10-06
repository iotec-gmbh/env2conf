import unittest
import unittest.mock

from env2conf import env2dict


class TestDict2Conf(unittest.TestCase):
    def setUp(self):
        env2dict.readEnv = unittest.mock.Mock(return_value={})

    def test_env2(self):
        test_data = [
            # simple
            {
                "before": {},
                "after": {"variable": "value"},
                "env": {"VARIABLE": "value"},
                "prefix": "",
            },
            # override
            {
                "before": {"variable": "value1"},
                "after": {"variable": "value2"},
                "env": {"VARIABLE": "value2"},
                "prefix": "",
            },
            # prefix
            {
                "before": {},
                "after": {"variable": "value"},
                "env": {"PREFIX_VARIABLE": "value"},
                "prefix": "PREFIX",
            },
            # no real prefix
            {
                "before": {},
                "after": {},
                "env": {"PREFIXVARIABLE": "value"},
                "prefix": "PREFIX",
            },
        ]

        for test in test_data:
            env2dict.readEnv.return_value = test["env"]
            env2dict.env2dict(test["before"], test["prefix"])
            self.assertEqual(test["before"], test["after"])
