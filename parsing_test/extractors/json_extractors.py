# extractors/json_extractors.py

import json


class JsonExtractor:

    """
    Extraction des objets JSON présents dans les logs.
    """

    @staticmethod
    def parse(json_string):

        """
        Convertit une chaîne JSON en dictionnaire Python.

        Parameters
        ----------
        json_string : str

        Returns
        -------
        dict
        """

        if json_string is None:
            return None

        try:

            return json.loads(json_string)

        except json.JSONDecodeError as e:

            print("Erreur JSON :", e)

            return None

    ############################################################

    @staticmethod
    def get(data, path, default=None):

        """
        Accès sécurisé aux champs imbriqués.

        Exemple

        JsonExtractor.get(
            data,
            ["Card","Pan"]
        )

        """

        current = data

        for key in path:

            if isinstance(current, dict):

                current = current.get(key)

            else:

                return default

            if current is None:

                return default

        return current

    ############################################################

    @staticmethod
    def exists(data, path):

        """
        Vérifie si un champ existe.
        """

        return JsonExtractor.get(
            data,
            path
        ) is not None

    ############################################################

    @staticmethod
    def extract_list(data, path):

        """
        Retourne une liste.

        Si le champ n'est pas une liste,
        retourne [].
        """

        value = JsonExtractor.get(
            data,
            path,
            []
        )

        if isinstance(value, list):

            return value

        return []

    ############################################################

    @staticmethod
    def extract_dict(data, path):

        """
        Retourne un dictionnaire.

        Si absent -> {}
        """

        value = JsonExtractor.get(
            data,
            path,
            {}
        )

        if isinstance(value, dict):

            return value

        return {}