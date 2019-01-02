import unittest

from env4conf import env2dict


class TestDict2Conf(unittest.TestCase):

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
            {
                "before": {
                    "dict": {},
                },
                "after": {
                    "dict": {
                        "key_1": "value1",
                        "key_2": "value2",
                    }
                },
                "env": {
                    "DICT_KEY_1": "value1",
                    "DICT_KEY_2": "value2",
                }
            }
        ]

        for i, test in enumerate(test_data):
            env = test.get("env", {})
            prefix = test.get("prefix", "")
            delimiter = test.get("delimiter", ",")
            before = test.get("before", {})
            after = test.get("after", {})
            env2dict(
                before,
                prefix=prefix,
                delimiter=delimiter,
                env=env,
            )
            self.assertEqual(before, after, "Test {} failed".format(i))
