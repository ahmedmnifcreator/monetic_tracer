# utils/xml_utils.py

import xmltodict


def xml_to_dict(xml_text):

    if xml_text is None:
        return None

    return xmltodict.parse(xml_text)


def dict_to_xml(data):

    return xmltodict.unparse(
        data,
        pretty=True
    )


def extract_tag(data, *keys):

    current = data

    for key in keys:

        if not isinstance(current, dict):
            return None

        current = current.get(key)

        if current is None:
            return None

    return current