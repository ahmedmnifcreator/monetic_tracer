# extractors/xml_extractors.py

import xml.etree.ElementTree as ET


class XmlExtractor:
    """
    Classe permettant de parser un message XML.
    """

    @staticmethod
    def parse(xml_string):
        """
        Convertit une chaîne XML en ElementTree.

        Parameters
        ----------
        xml_string : str

        Returns
        -------
        Element ou None
        """

        if not xml_string:
            return None

        try:
            return ET.fromstring(xml_string)

        except ET.ParseError as e:
            print("Erreur XML :", e)
            return None

    ########################################################

    @staticmethod
    def get(root, path, default=None):
        """
        Récupère la valeur d'une balise.

        Exemple :
            Transaction/RequestedAmount/Amount
        """

        if root is None:
            return default

        element = root.find(path)

        if element is None:
            return default

        return element.text

    ########################################################

    @staticmethod
    def exists(root, path):

        if root is None:
            return False

        return root.find(path) is not None

    ########################################################

    @staticmethod
    def get_attributes(root, path):
        """
        Retourne les attributs d'une balise.
        """

        if root is None:
            return {}

        element = root.find(path)

        if element is None:
            return {}

        return element.attrib

    ########################################################

    @staticmethod
    def get_children(root, path):
        """
        Retourne tous les enfants d'une balise.
        """

        if root is None:
            return []

        element = root.find(path)

        if element is None:
            return []

        return list(element)

    ########################################################

    @staticmethod
    def xml_to_dict(element):
        """
        Convertit récursivement un XML en dictionnaire.
        """

        if element is None:
            return None

        result = {}

        children = list(element)

        if not children:
            return element.text

        for child in children:

            value = XmlExtractor.xml_to_dict(child)

            if child.tag in result:

                if not isinstance(result[child.tag], list):

                    result[child.tag] = [
                        result[child.tag]
                    ]

                result[child.tag].append(value)

            else:

                result[child.tag] = value

        return result