import os


def readEnv():
    return os.environ


def env2dict(confDict, prefix='', delimiter=','):
    if prefix:
        prefix = prefix + "_"

    for key, value in readEnv().items():
        if not key.startswith(prefix):
            continue

        key = key[len(prefix):].lower()

        old_config = confDict.get(key)
        old_config_type = type(old_config)
        if old_config_type is list:
            confDict[key] = value.split(delimiter)
            continue

        confDict[key] = value
