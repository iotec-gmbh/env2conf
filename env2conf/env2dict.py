import os


def __recursive_add__(key, remaining_parts, confDict, value, delimiter):
    old_config = confDict.get(key)

    if old_config is not None:
        old_config_type = type(old_config)
        if old_config_type is list:
            confDict[key] = value.split(delimiter)
            return
        if old_config_type is dict:
            __recursive_add__(
                remaining_parts[0], remaining_parts[1:],
                old_config, value, delimiter)
            return

    if remaining_parts:
        __recursive_add__(
            "{}_{}".format(key, remaining_parts[0]),
            remaining_parts[1:],
            confDict, value, delimiter
        )
        return

    confDict[key] = value


def env2dict(confDict, prefix='', delimiter=',', env=None):
    if env is None:
        env = os.environ

    if prefix:
        prefix = prefix + "_"

    for key, value in env.items():
        if not key.startswith(prefix):
            continue

        key = key[len(prefix):].lower()
        key_parts = key.split("_")
        __recursive_add__(
            key_parts[0], key_parts[1:], confDict, value, delimiter)
