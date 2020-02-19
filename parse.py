import xml.etree.ElementTree as eT
from splitObj import Splits


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
