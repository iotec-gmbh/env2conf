import os


def readEnv():
    return os.environ


def env2dict(confDict, prefix=''):
    if prefix:
        prefix = prefix + "_"
    for key, value in readEnv().items():
        if not key.startswith(prefix):
            continue
        key = key[len(prefix):].lower()
        confDict[key] = value
