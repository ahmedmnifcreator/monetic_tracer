# utils/helpers.py

def get_value(data, path, default=None):

    current = data

    for key in path:

        if not isinstance(current, dict):
            return default

        current = current.get(key)

        if current is None:
            return default

    return current


def clean(value):

    if value is None:
        return None

    if isinstance(value, str):
        return value.strip()

    return value


def to_list(value):

    if value is None:
        return []

    if isinstance(value, list):
        return value

    return [value]


def safe_bool(value):

    if isinstance(value, bool):
        return value

    if value is None:
        return False

    return str(value).lower() == "true"