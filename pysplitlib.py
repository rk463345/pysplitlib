#!/usr/bin/env python3
"""
Creates a Splits object for use by livesplit software. Can also be used to view
splits xml formats with pysplit.py splitsfile.xml
"""
from sys import argv
from pysplitlib.parse import parse_file


class Splits:
    """Creates splits object to be used for livesplit software"""

    #pylint: disable=R0913
    def __init__(self, game_name='', game_icon=None, category='', attempt_count=0, segments=[]):
        self.game_name = game_name
        self.game_icon = game_icon
        self.category = category
        self.attempt_count = attempt_count
        self.segments = segments

    def __repr__(self):
        return 'Splits({})'.format(self._to_dict())

    def _to_dict(self):
        return {
            'game': self.game_name,
            'icon': self.game_icon,
            'category': self.category,
            'attempt_count': self.attempt_count,
            'segments': self.list_to_dict()
        }

    def list_to_dict(self):
        """Convert segment list to dict"""
        return {i: self.segments[i] for i in range(0, len(self.segments))}


if __name__ == "__main__":
    FILE = argv[1]
    print(parse_file(FILE))
