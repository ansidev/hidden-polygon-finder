import yaml


class ShapeData:
    """
    A class to convert a nested Dictionary into an object with key-values
    accessibly using attribute notation (AttributeDict.attribute) instead of
    key notation (Dict["key"]). This class recursively sets Dicts to objects,
    allowing you to recurse down nested dicts (like: AttributeDict.attr.attr)
    """

    def __init__(self, path):
        stream = open(path, "r")
        docs = yaml.load_all(stream)
        for doc in docs:
            for key, value in doc.items():
                setattr(self, key, value)

    def get(self, key):
        """
        Provides dict-style access to attributes
        """
        return getattr(self, key)

    def set(self, key, value):
        setattr(self, key, value)
