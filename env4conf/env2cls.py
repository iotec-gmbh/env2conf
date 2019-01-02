from .env2dict import env2dict


def env2cls(confcls, **kwargs):
    env2dict(confcls.__dict__, **kwargs)
