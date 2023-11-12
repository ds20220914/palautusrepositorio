from urllib import request
from project import Project
from tomli import loads

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)
        toml_data = loads(content)
        name = toml_data.get("tool")
        name1=name.get("poetry")
        name2=name1.get("name")
        dependencies=name1.get("dependencies")
        description=name1.get("description")
        dev=name1.get("group")
        dev1=dev.get("dev")
        dev2=dev1.get("dependencies")
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name2,description,dependencies, dev2)
