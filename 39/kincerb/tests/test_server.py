import checkin
import pytest

from psutil._common import sdiskpart

PARTITIONS = [
    sdiskpart(device='rootfs', mountpoint='/', fstype='rootfs', opts='rw'),
    sdiskpart(device='/dev/mapper/rootvg-rootlv', mountpoint='/', fstype='ext4', opts='rw,relatime,data=ordered'),
    sdiskpart(device='proc', mountpoint='/proc', fstype='proc', opts='rw,nosuid,nodev,noexec,relatime'),
    sdiskpart(device='tmpfs', mountpoint='/dev/shm', fstype='tmpfs', opts='rw,nosuid,nodev,noexec'),
    sdiskpart(device='cgroup', mountpoint='/sys/fs/cgroup/blkio', fstype='cgroup', opts='rw,nosuid,nodev,noexec,relatime,blkio'),
    sdiskpart(device='devpts', mountpoint='/dev/pts', fstype='devpts', opts='rw,nosuid,noexec,relatime,gid=5,mode=620,ptmxmode=000'),
    sdiskpart(device='devtmpfs', mountpoint='/dev', fstype='devtmpfs', opts='rw,nosuid,size=1945760k,nr_inodes=486440,mode=755'),
    sdiskpart(device='sysfs', mountpoint='/sys', fstype='sysfs', opts='rw,nosuid,nodev,noexec,relatime'),
    sdiskpart(device='pstore', mountpoint='/sys/fs/pstore', fstype='pstore', opts='rw,nosuid,nodev,noexec,relatime'),
    sdiskpart(device='configfs', mountpoint='/sys/kernel/config', fstype='configfs', opts='rw,relatime'),
    sdiskpart(device='systemd-1', mountpoint='/proc/sys/fs/binfmt_misc', fstype='autofs', opts='rw,relatime,fd=35,pgrp=1,timeout=0,minproto=5,maxproto=5,direct,pipe_ino=13097'),
    sdiskpart(device='hugetlbfs', mountpoint='/dev/hugepages', fstype='hugetlbfs', opts='rw,relatime'),
    sdiskpart(device='debugfs', mountpoint='/sys/kernel/debug', fstype='debugfs', opts='rw,relatime'),
    sdiskpart(device='mqueue', mountpoint='/dev/mqueue', fstype='mqueue', opts='rw,relatime'),
    sdiskpart(device='binfmt_misc', mountpoint='/proc/sys/fs/binfmt_misc', fstype='binfmt_misc', opts='rw,relatime'),
    sdiskpart(device='sunrpc', mountpoint='/var/lib/nfs/rpc_pipefs', fstype='rpc_pipefs', opts='rw,relatime'),
    sdiskpart(device='ohlewnas300d.nwie.net:/linux_mig_scripts', mountpoint='/linux_mig_scripts', fstype='nfs',
              opts='rw,relatime,vers=3,rsize=131072,wsize=524288,namlen=255,hard,proto=tcp,timeo=600,retrans=2,sec=sys,mountaddr=10.86.146.172,mountvers=3,mountport=300,mountproto=udp,local_lock=none,addr=10.86.146.172'),
]


class TestServerInfo(object):

    def mock_disks(self, all):
        return PARTITIONS

    @pytest.mark.parametrize('fs_type',
                              ['ext4',
                               'rootfs',
                               'proc',
                               'tmpfs',
                               'cgroup',
                               'devpts',
                               'devtmpfs',
                               'sysfs',
                               'pstore',
                               'configfs',
                               'autofs',
                               'hugetlbfs',
                               'debugfs',
                               'mqueue',
                               'binfmt_misc',
                               'nfs'])
    def test_single_filter(self, monkeypatch, fs_type):
        monkeypatch.setattr(checkin.server.info.psutil,
                            'disk_partitions',
                            self.mock_disks)
        assert {fs_type, } == set([disk.fstype for disk in checkin.server.info.mounted_disks(fs_filter=fs_type)])

    @pytest.mark.parametrize('fs_type',
                             [['ext4', 'rootfs'],
                              ['ext4', 'nfs'],
                              ['ext4', 'tmpfs'],
                              ['nfs', 'tmpfs'],
                              ['nfs', 'devtmpfs']])
    def test_multiple_filters(self, monkeypatch, fs_type):
        monkeypatch.setattr(checkin.server.info.psutil,
                            'disk_partitions',
                            self.mock_disks)
        assert set(fs_type) == set([disk.fstype for disk in checkin.server.info.mounted_disks(fs_filter=fs_type)])

