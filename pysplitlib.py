#!/usr/bin/env python3
"""
Creates a Splits object for use by livesplit software. Can also be used to view
splits xml formats with pysplit.py splitsfile.xml
"""
import sys
from datetime import datetime
import xml.etree.ElementTree as eT


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


def parse_xml(xml_file):
    tree = eT.parse(xml_file)
    root = tree.getroot()

    # Get Game Name
    try:
        game_name = root.find('GameName').text
    except AttributeError:
        game_name = ''

    # Get Game Icon
    try:
        game_icon = root.find('GameIcon')
    except AttributeError:
        game_icon = None

    # Get Category Name
    try:
        category = root.find('CategoryName').text
    except AttributeError:
        category = ''

    # Get Segment Data
    try:
        segments = root.find('Segments')
        segment_list = []
        # TODO Add Split times in
        for segment in segments:
            seg_dict = {}
            seg_dict.update({'name': segment.find('Name').text})
            seg_dict.update({'icon': segment.find('Icon').text})
            seg_dict.update({'best': segment.find('BestSegmentTime').find('RealTime').text})
            # for hist in segment.find('SegmentHistory'):
            #    print(hist.attrib['id'])

            segment_list.append(seg_dict)
    except AttributeError:
        segment_list = []

    # Get Attempt Count
    try:
        attempt_count = root.find('AttemptCount').text
    except AttributeError:
        segment_list = []

    return game_name, game_icon, category, attempt_count, segment_list


def parse_file(xmlfile):
    """Parses XML file and returns Split object"""
    game_name, game_icon, category, attempt_count, segments = parse_xml(xmlfile)
    return Splits(game_name, game_icon, category, attempt_count, segments)


def timesplit(start, end):
    """
    Returns difference in seconds of start and end

    start (datetime): Start time
    end (datetime): End time
    """
    return (end - start).total_seconds()


def start_split():
    """returns datetime object"""
    return datetime.now()


def end_split(start):
    """Returns a timesplit in seconds"""
    return timesplit(start, datetime.now())


if __name__ == "__main__":
    FILE = sys.argv[1]
    print(parse_file(FILE))
