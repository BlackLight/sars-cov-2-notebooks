from typing import Union, List, Optional


class Genome:
    """
    Genome representation.
    """

    def __init__(self, id: str, name: str, sequence: str = '', args: Optional[List[str]] = None):
        """
        :param id: Genome sequence ID.
        :param name: Genome sequence name/label/description.
        :param sequence: Raw genome sequence.
        :param args: Optional arguments.
        """
        self.id = id
        self.name = name
        self.args = args or []
        self.sequence = sequence

    def append(self, sequence: str):
        self.sequence += sequence.strip()

    def __str__(self):
        import json
        return json.dumps(self.__repr__())

    def __repr__(self):
        return {
            'id': self.id,
            'name': self.name,
            'args': self.args,
            'sequence': ''.join(self.sequence),
        }

    def to_dict(self):
        return self.__repr__()

    @classmethod
    def from_dict(cls, **args):
        return cls(**args)


# vim:sw=4:ts=4:et:
