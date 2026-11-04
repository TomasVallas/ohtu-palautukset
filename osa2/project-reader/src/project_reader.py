import re
from urllib import request
import toml
from project import Project


def riippuvuuden_nimi(riippuvuus):
    # "flask>=3.1.3" -> "flask"
    return re.split(r"[<>=!~;\[ ]", riippuvuus, maxsplit=1)[0]


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # deserialisoidaan TOML-merkkijono Pythonin sanakirjaksi
        data = toml.loads(content)
        tiedot = data["project"]

        tekijat = [tekija["name"] for tekija in tiedot.get("authors", [])]
        riippuvuudet = [
            riippuvuuden_nimi(r) for r in tiedot.get("dependencies", [])
        ]
        dev_riippuvuudet = [
            riippuvuuden_nimi(r)
            for r in data.get("dependency-groups", {}).get("dev", [])
        ]

        return Project(
            tiedot.get("name"),
            tiedot.get("description"),
            tiedot.get("license"),
            tekijat,
            riippuvuudet,
            dev_riippuvuudet,
        )
