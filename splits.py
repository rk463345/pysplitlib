from datetime import datetime


def time_split(start, end):
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
    """Returns a time_split in seconds"""
    return time_split(start, datetime.now())