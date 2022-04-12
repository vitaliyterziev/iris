class Cube:
    '''
    A class to represent Cube objects

    ...

    Attributes
    ----------
    _side_length -> private, side length of cube

    Methods
    ----------
    __init__(self, side_length) -> sets _side_length property
    volme() -> returns Cube's volume (_side_length ** 3)
    side_length() -> returns _side_length property value
    '''

    def __init__(self, side_length):
        self._side_length = side_length

    def volume(self):
        return self._side_length ** 3

    def side_length(self):
        return self._side_length
