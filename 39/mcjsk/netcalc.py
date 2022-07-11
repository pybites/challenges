#!/usr/bin/env python3

"""
netcalc IPv4 subnet calculator

Return range of contiguous block of addresses determined by the
CIDR notation specified on the command line. See --help for usage.

Logic:
  1. Split command line specified CIDR into list of IPv4 address and prefix
  2. Type cast prefix and octets in list to integer for arithmetic operation
  3. Compute subnet block length from host bits (i.e., the remainder after
  subtracting mask bits (prefix) from the 32-bit address space
  4. Compute prefix as a 32-bit integer representation of the subnet mask
  5. Convert list of octets to 32-bit integer representation of IP address,
  then logical AND with subnet mask to compute start IP address of subnet
  6. Compute 32-bit integer representation of end IP address of subnet by
  adding subnet block length to start IP address integer
  7. Convert start, end, and bitmask IP integers to string representation
  of IPv4 address in dot notation
"""
__author__ = "Mark Jamsek"
__version__ = "0.3"
__date__ = "18 July 2019"
__email__ = "mark@jamsek.com"

import argparse


def main():
    """
    Verify command line arguments are valid:
      - correct CIDR (i.e., dash "/") notation
      - CIDR prefix is an integer
      - IPv4 address is correct length
      - IPv4 address is numeric
    If invalid, print reason for error and usage example upon exit.
    If valid, proceed with program logic.
    """
    args, parser = parse_commands()
    cidr = args.cidr[0].split("/")
    if len(cidr) != 2:
        print(f"\nError: incorrect notation {args.cidr}")
        exit(f"{parser.format_usage()}")
    ipstring = cidr[0]
    try:
        prefix = int(cidr[1])
        blocklen = 2 ** (32 - prefix)
    except:
        print(f"\nError: CIDR prefix must be integer ['{cidr[1]}']")
        exit(f"{parser.format_usage()}")
    iplist = ipstring.split(".")
    if len(iplist) != 4:
        print(f"\nError: abnormal length IP address ['{ipstring}']")
        exit(f"{parser.format_usage()}")
    try:
        iplist = [int(x) for x in iplist]
    except:
        print(f"\nError: illegal characters in IP address ['{ipstring}']")
        exit(f"{parser.format_usage()}")

    bitmask_int = mask_to_int(prefix)
    start_ipint = iplst_to_int(iplist) & bitmask_int
    end_ipint = start_ipint + blocklen - 1
    start_ipaddr = iplst_to_ipaddr(ipint_to_lst(start_ipint))
    end_ipaddr = iplst_to_ipaddr(ipint_to_lst(end_ipint))
    netmask = iplst_to_ipaddr(ipint_to_lst(bitmask_int))
    print(f"\n[+] {'CIDR Range':<15} :  {args.cidr[0]}")
    print(f"[+] {'Subnet ID':<15} :  {start_ipaddr}/{cidr[1]}")
    print(f"[+] {'Subnet Mask':<15} :  {netmask}")
    print(f"[+] {'Address range':<15} :  {start_ipaddr} —— {end_ipaddr}")
    print(
        f"[+] {'Address block':<15} :  {blocklen:,d} total ({blocklen - 2 if int(cidr[1]) <= 30 else blocklen:,d} usable) contiguous hosts\n"
    )


def mask_to_int(prefix):
    """
    Convert CIDR prefix to integer: initialise 32-bit address with each bit
    set, then bitwise left shift for the number of host bits (i.e., the
    remaining bits after subtracting the mask bits specified by the prefix)
    to set the host bits to zero. Then logical AND with 32-bit address space
    to pad with leading zeros to get 32-bit subnet mask
    
    :param prefix: integer of mask bits

    :return: integer representation of subnet mask
    """
    return 0xFFFFFFFF << (32 - prefix) & 0xFFFFFFFF


def iplst_to_int(iplst):
    """
    Convert IP octet list to integer: perform bitwise left shift of each octet
    in multiples of eight corresponding to its position (i.e., MSByte left
    shift 24 bits; Byte 2, 16 bits; Byte 1, 8 bits; LSByte stays put) to
    convert to 32-bit integer
    
    :param iplst: list of octets that comprise specified IPv4 address
    
    :return: integer representation of 32-bit IPv4 address
    """
    return sum(map(lambda x, y: x << y, iplst, [24, 16, 8, 0]))


def ipint_to_lst(ipint):
    """
    Convert IP address integer to list of octets: perform bitwise arithmetic
    right shift of the 32-bit integer in four iterations of decreasing
    multiples of eight from 24 to 8, to move corresponding byte (i.e., bit
    24–31; 16–23; 8–15; and 0–7) to first eight bits, then logical AND with
    255 to produce each 1-byte length octet of the IPv4 address.
    
    :param ipint: IPv4 address as decimal integer
    
    :return: list of four octets representing IPv4 address (e.g., [10, 0, 0, 1])
    """
    return [(ipint >> b) & 0xFF for b in (24, 16, 8, 0)]


def iplst_to_ipaddr(iplst):
    """
    Convert list of octets to IPv4 address string in dot notation
    
    :param iplst: list of four octets
    
    :return: string of IPv4 address (e.g. '192.168.0.1')
    """
    return ".".join([str(o) for o in iplst])


def parse_commands():
    parser = argparse.ArgumentParser(
        prog="netcalc",
        description="%(prog)s: IPv4 subnet calculator",
        epilog=f"%(prog)s {__version__} released {__date__}",
        usage=f"netcalc [-h] ipaddr/prefix\n  e.g. netcalc 10.0.0.1/24",
    )
    parser.add_argument(
        "cidr", metavar="ipaddr/prefix", help="CIDR notation to find subnet", nargs=1
    )
    args = parser.parse_args()
    return args, parser


if __name__ == "__main__":
    main()
