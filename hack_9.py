"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(param):
    param.pop("bar")
    key = param.keys()
    value=param.get(list(key)[0])
    return {list(key)[0].capitalize() : value.replace('k','').capitalize()}

    return result