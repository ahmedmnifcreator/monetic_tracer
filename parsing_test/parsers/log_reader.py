# parsers/log_reader.py

from pathlib import Path


class LogReader:
    """
    Classe responsable de la lecture des fichiers de log.
    """

    def __init__(self, file_path: str):
        """
        Initialise le lecteur avec le chemin du fichier.

        Parameters
        ----------
        file_path : str
            Chemin du fichier log.
        """
        self.file_path = Path(file_path)

    def exists(self) -> bool:
        """
        Vérifie que le fichier existe.
        """
        return self.file_path.exists()

    def read(self) -> str:
        """
        Lit tout le contenu du fichier.

        Returns
        -------
        str
            Contenu complet du log.
        """

        if not self.exists():
            raise FileNotFoundError(
                f"Le fichier '{self.file_path}' est introuvable."
            )

        with open(
            self.file_path,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as file:

            return file.read()

    def read_lines(self):
        """
        Retourne une liste contenant toutes les lignes du log.

        Returns
        -------
        list
        """

        if not self.exists():
            raise FileNotFoundError(
                f"Le fichier '{self.file_path}' est introuvable."
            )

        with open(
            self.file_path,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as file:

            return file.readlines()