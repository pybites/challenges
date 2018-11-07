import psutil


def mounted_disks(fs_filter=None):
    """
    Returns a list of mounted disks, each item being a named tuple.

    :param fs_filter: list of filesystem types to return
    :type fs_filter: list
    :returns: list of mounted disks
    :rtype: list
    """
    return [disk for disk in _get_mounted_disks(fs_filter=fs_filter)]


def _get_mounted_disks(fs_filter=None):
    """
    Find mounted disks on the system, returning a generator producing
    a result upon each `next()` call

    :param fs_filter: list of filesystem types to return
    :type fs_filter: list
    :returns: next matching disk
    :rtype: generator
    """
    if fs_filter:
        if not type(fs_filter) is list:
            fs_filter = [fs_filter]

    for disk in psutil.disk_partitions(all=True):
        if fs_filter:
            if disk.fstype in fs_filter:
                yield disk
            continue
        yield disk
