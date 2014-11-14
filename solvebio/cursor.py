class Cursor(object):
    """
    Stateful cursor object that tracks of the range and offset of a Query.
    """

    @property
    def offset_absolute(self):
        return self.start + self.offset

    @classmethod
    def from_slice(klass, _slice, offset=0):
        return \
            Cursor(_slice.start, _slice.stop, offset=offset)

    def __init__(self, start, stop, offset=0):
        """
        Creates a new cursor object.
        """
        self.reset(start, stop, offset)

    def advance(self, incr=1):
        self.offset += incr

    def reset(self, start, stop, offset):
        """
        Reset.

        :Parameters:
          - `start`: Absolute start position
          - `stop`: Absolute stop position
          - `offset` (optional): Cursor offset relative to `start`
        """
        self.start = start
        self.stop = stop
        self.offset = 0

    def reset_absolute(self, offset_absolute):
        """
        Reset the internal offset from an absolute position.

        :Parameters:
          - `offset_absolute`: Absolute cursor offset
        """
        self.offset = offset_absolute - self.start

    def has_next(self):
        return self.offset >= 0 and self.offset < (self.stop - self.start)

    def __repr__(self):
        return 'range: %s, offset: %s' % \
            (slice(self.start, self.stop), self.offset)
