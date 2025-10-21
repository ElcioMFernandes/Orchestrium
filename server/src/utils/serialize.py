import datetime

def serialize(object):
    serialized = {}
    for attr in dir(object):
        if attr.startswith("_"):
            continue

        try:
            value = getattr(object, attr)
            
            if callable(value):
                continue

            if isinstance(value, (str, int, float, bool, type(None))):
                serialized[attr] = value

            elif isinstance(value, datetime):
                serialized[attr] = value.isoformat()

            elif hasattr(value, "__str__"):
                serialized[attr] = str(value)

        except (AttributeError, TypeError):
            continue
    return serialized