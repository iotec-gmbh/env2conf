import unittest
import unittest.mock

from env2conf import env2dict, utils


class TestDict2Conf(unittest.TestCase):
    def setUp(self):
        env2dict.readEnv = unittest.mock.Mock(return_value={})

    def test_env2dict(self):
        test_data = [
            # simple
            {
                "after": {"variable": "value"},
                "env": {"VARIABLE": "value"},
            },
            # override
            {
                "before": {"variable": "value1"},
                "after": {"variable": "value2"},
                "env": {"VARIABLE": "value2"},
            },
            # prefix
            {
                "after": {"variable": "value"},
                "env": {"PREFIX_VARIABLE": "value"},
                "prefix": "PREFIX",
            },
            # no real prefix
            {
                "env": {"PREFIXVARIABLE": "value"},
                "prefix": "PREFIX",
            },
            # list
            {
                "before": {
                    "variable": []
                },
                "after": {
                    "variable": ["value1", "value2"]
                },
                "env": {"VARIABLE": "value1,value2"},
            },
            {
                "before": {
                    "variable": []
                },
                "after": {
                    "variable": ["value1", "value2"]
                },
                "env": {"VARIABLE": "value1:value2"},
                "delimiter": ":"
            },
            # no real list
            {
                "before": {
                    "variable": ""
                },
                "after": {
                    "variable": "value1,value2",
                },
                "env": {"VARIABLE": "value1,value2"},
            },
        ]

        for i, test in enumerate(test_data):
            env = test.get("env", {})
            prefix = test.get("prefix", "")
            delimiter = test.get("delimiter", ",")
            before = test.get("before", {})
            after = test.get("after", {})
            utils.readEnv.return_value = env
            env2dict.env2dict(
                before,
                prefix=prefix,
                delimiter=delimiter,
            )
            self.assertEqual(before, after, "Test {} failed".format(i))
