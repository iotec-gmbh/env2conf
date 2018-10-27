import unittest

from env2conf import env2cls


class TestEnv2Conf(unittest.TestCase):

    def test_env2cls(self):
        class Test():
            pass

        test_data = [
            # simple
            {
            },
            {
                "after": {"key": "value"},
                "env": {
                    "key": "value",
                }
            },
        ]

        for test in test_data:
            env = test.get("env", {})
            prefix = test.get("prefix", "")
            delimiter = test.get("delimiter", ",")
            before = test.get("before", Test())
            after = Test()
            for k, v in test.get("after", {}).items():
                setattr(after, k, v)
            env2cls(
                before,
                prefix=prefix,
                delimiter=delimiter,
                env=env,
            )
            self.assertEqual(before.__dict__, after.__dict__)
