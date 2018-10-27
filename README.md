# env2conf

![circleci](https://circleci.com/gh/iotec-gmbh/env2conf.png?style=shield)

Python library to override configuration entries with environment variables

## Installation

To install this module via `pip` use

```
pip install git+https://github.com/iotec-gmbh/env2conf@v0.1
```

or for the latest version

```
pip install git+https://github.com/iotec-gmbh/env2conf
```

## Usage

The simpliest way to use this module is to start with an empty configuration dictionary and fill ist from the environment.

```python
>>> import os
>>> from env2conf import env2dict
>>> conf = {}
>>> os.environ["ENV2CONF_KEY"] = "value"
>>> env2dict(conf, prefix="ENV2CONF")
>>> print(conf)
{'key': 'value'}
```

You can also override variables.

```python
>>> conf = {'key': 'old_value'}
>>> os.environ["ENV2CONF_KEY"] = "new_value"
>>> env2dict(conf, prefix="ENV2CONF")
>>> print(conf)
{'key': 'new_value'}
```

Or create lists in the configuration.
But for that you need to initialize the variable as a list before so that `env2conf` knows how to treat it.

```python
>>> conf = {"list": []}
>>> os.environ["ENV2CONF_LIST"] = "value1,value2,value3"
>>> env2dict(conf, prefix="ENV2CONF")
>>> print(conf)
{'list': ['value1', 'value2', 'value3']}
```

Same applies to nested dictionaries.

```python
>>> conf = {"dict": {}}
>>> os.environ["ENV2CONF_DICT_KEY1"] = "value1"
>>> os.environ["ENV2CONF_DICT_KEY2"] = "value2"
>>> env2dict(conf, prefix="ENV2CONF")
>>> print(conf)
{'dict': {'key1': 'value1', 'key2': 'value2'}}
```

You can also use objects to store your configuration

```python
>>> import os
>>> from env2conf import env2cls
>>> class Conf():
...     pass
... 
>>> conf = Conf()
>>> conf.key = "old_value"
>>> conf.list = []
>>> conf.dict = {}
>>> os.environ["ENV2CONF_KEY"] = "new_value"
>>> os.environ["ENV2CONF_LIST"] = "value1,value2,value3"
>>> os.environ["ENV2CONF_DICT_KEY1"] = "value1"
>>> os.environ["ENV2CONF_DICT_KEY2"] = "value2"
>>> env2cls(conf, prefix="ENV2CONF")
>>> print(conf)
<__main__.Conf object at 0x7f15ce6f92e8>
>>> print(conf.__dict__)
{'key': 'new_value', 'list': ['value1', 'value2', 'value3'], 'dict': {'key1': 'value1', 'key2': 'value2'}}
```
