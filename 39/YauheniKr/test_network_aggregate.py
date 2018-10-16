import network_aggregate
import openpyxl, netaddr, sys, os
import pytest



def test_open_excel_routers(tmpdir_factory):
    address = ["192.168.100.0/24", '192.168.1.0/24']
    filename = tmpdir_factory.mktemp('./sub').join("netaddr.xlsx")
    wb = openpyxl.Workbook()
    sheet = wb.active
    for cell_row in range(1,len(address)+1):
        sheet.cell(row = cell_row, column = 1).value = address[cell_row-1]
    wb.save(filename)
    print(address)
    assert address == network_aggregate.open_excel_routers(filename)
