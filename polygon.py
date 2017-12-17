class Polygon:
    """
    A class to convert a nested Dictionary into an object with key-values
    accessibly using attribute notation (AttributeDict.attribute) instead of
    key notation (Dict["key"]). This class recursively sets Dicts to objects,
    allowing you to recurse down nested dicts (like: AttributeDict.attr.attr)
    """

    def __init__(self, point):
        self.points = list()
        self.max_point = point

    def add(self, point):
        """
        Add new point to polygon
        """
        if len(self.points) < self.max_point:
            self.points.append(point)

    def to_string(self):
        return ''.join(self.points)
