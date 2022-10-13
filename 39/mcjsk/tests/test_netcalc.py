import netcalc
import pytest
import pytest_cov
import re

from unittest.mock import patch
from netcalc import (
    mask_to_int,
    iplst_to_int,
    ipint_to_lst,
    iplst_to_ipaddr,
    parse_commands,
    main,
)


def test_main_valid(capfd):
    with patch("sys.argv", ["netcalc", "10.0.0.1/24"]):
        main()
        out = capfd.readouterr()[0]
        assert (
            out
            == f"""\n[+] {'CIDR Range':<16}:  10.0.0.1/24\n[+] {'Subnet ID':<16}:  10.0.0.0/24\n[+] {'Subnet Mask':<16}:  255.255.255.0\n[+] {'Address range':<16}:  10.0.0.0 —— 10.0.0.255\n[+] {'Address block':<16}:  256 total (254 usable) contiguous hosts\n\n"""
        )


@pytest.fixture
def usage():
    return "usage: netcalc [-h] ipaddr/prefix\n  e.g. netcalc 10.0.0.1/24\n"


no_arg = "netcalc: error: the following arguments are required: ipaddr/prefix"
notation = "Error: incorrect notation ['10.0.0.1']"
prefix = "Error: CIDR prefix must be integer ['A1']"
iplong = "Error: abnormal length IP address ['10.0.0.1.2']"
ipshort = "Error: abnormal length IP address ['10.0.1']"
ipchar = "Error: illegal characters in IP address ['10.0.0.F']"


@pytest.mark.parametrize(
    "cmd, error",
    [
        ("10.0.0.1", notation),
        ("10.0.0.1/A1", prefix),
        ("10.0.0.1.2/21", iplong),
        ("10.0.1/21", ipshort),
        ("10.0.0.F/21", ipchar),
    ],
)
def test_main_invalid(cmd, error, usage, capsys):
    with patch("sys.argv", ["netcalc", cmd]):
        with pytest.raises(SystemExit, match=re.escape(usage)):
            main()
        out = capsys.readouterr()[0]
        assert out.strip() == error
    with patch("sys.argv", ["netcalc"]):
        with pytest.raises(SystemExit, match="2"):
            main()
        err = capsys.readouterr()[1]
        assert err.strip() == usage + no_arg


@pytest.mark.parametrize(
    "bitmask, submask",
    [
        (0, 0),
        (4, 4026531840),
        (8, 4278190080),
        (11, 4292870144),
        (15, 4294836224),
        (18, 4294950912),
        (21, 4294965248),
        (22, 4294966272),
        (26, 4294967232),
        (29, 4294967288),
        (32, 4294967295),
    ],
)
def test_mask_to_int(bitmask, submask):
    assert mask_to_int(bitmask) == submask


@pytest.fixture
def get_ip_test_data():
    return [
        ([192, 168, 0, 1], 3232235521),
        ([119, 18, 3, 36], 1997669156),
        ([10, 0, 0, 115], 167772275),
        ([220, 11, 130, 1], 3691741697),
        ([110, 40, 240, 16], 1848176656),
        ([14, 12, 72, 8], 235685896),
        ([255, 255, 252, 0], 4294966272),
        ([255, 255, 255, 255], 4294967295),
        ([10, 0, 10, 0], 167774720),
    ]


def test_iplst_to_int(get_ip_test_data):
    for data in get_ip_test_data:
        iplst, integer = data[0], data[1]
        assert iplst_to_int(iplst) == integer


def test_ipint_to_lst(get_ip_test_data):
    for data in get_ip_test_data:
        iplst, integer = data[0], data[1]
        assert ipint_to_lst(integer) == iplst


@pytest.mark.parametrize(
    "iplst, ipstring",
    [
        ([192, 168, 0, 1], "192.168.0.1"),
        ([119, 18, 3, 36], "119.18.3.36"),
        ([10, 0, 0, 115], "10.0.0.115"),
        ([220, 11, 130, 1], "220.11.130.1"),
        ([110, 40, 240, 16], "110.40.240.16"),
        ([14, 12, 72, 8], "14.12.72.8"),
        ([255, 255, 252, 0], "255.255.252.0"),
        ([255, 255, 255, 255], "255.255.255.255"),
        ([10, 0, 10, 0], "10.0.10.0"),
    ],
)
def test_iplst_to_ipaddr(iplst, ipstring):
    assert iplst_to_ipaddr(iplst) == ipstring
