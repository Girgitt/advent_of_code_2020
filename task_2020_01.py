input_data = """
1864
1192
1802
1850
1986
1514
1620
1910
1557
1529
1081
1227
1869
1545
1064
1509
1060
1590
1146
1855
667
1441
1241
1473
1321
1429
1534
1959
1188
1597
1256
1673
1879
1821
1423
1838
1392
1941
1124
1629
1780
1271
1190
1680
1379
1601
1670
1916
1787
1844
2000
1672
1276
1896
1746
1369
1687
1263
1948
1159
1710
1304
1806
1709
1286
1635
1075
1125
1607
1408
1903
1143
1736
1266
1645
1571
1488
1200
211
1148
1585
2005
1724
1071
1690
1189
1101
1315
1452
1622
1074
1486
1209
1253
1422
1235
1354
1399
1675
241
1229
1136
1901
1453
1344
1685
1985
1455
1764
1634
1935
1386
1772
1174
1743
1818
1156
1221
167
1398
1552
1816
1197
1829
1930
1812
1983
1185
1579
1928
1892
1978
1720
1584
1506
1245
1539
1653
1876
1883
1982
1114
1406
2002
1765
1175
1947
1519
1943
1566
1361
1830
1679
999
1366
1575
1556
1555
1065
1606
1508
1548
1162
1664
1525
1925
1975
1384
1076
1790
1656
1578
1671
1424
757
1485
1677
1583
1395
1793
1111
1522
1195
1128
1123
1151
1568
1559
1331
1191
1753
1630
1979
953
1480
1655
1100
1419
1560
1667
"""


def get_input():
    return [int(item) for item in input_data.splitlines() if item != '']


def get_solution_1():
    report_vals = get_input()
    argument_for_product = dict()
    for input_val in report_vals:
        product_result = input_val * (2020-input_val)
        try:
            argument_for_product[product_result]
            print(product_result)
        except KeyError:
            argument_for_product[product_result] = input_val


def get_solution_2():
    report_vals = get_input()
    # a + b + c = 2020

    # b + c = 2020 - a
    # a + c = 2020 - b
    # a + b = 2020 - c

    # 1. sumy dopelnien do 2020 dla kazdego [wejscia]
    # 2. dla kazdego dopelnienia roznica z innego wejscia do przetestowania czy znajdzie sie w zbiorze pozostalych wejsc
    for input_val_1 in report_vals:
        dopelnienie_1 = 2020 - input_val_1
        for input_val_2 in report_vals:
            if input_val_1 == input_val_2:
                continue
            dopelnienie_2 = dopelnienie_1 - input_val_2
            if dopelnienie_2 in report_vals:
                prod_res = (input_val_1 * input_val_2 * dopelnienie_2)
                print("%s  %s  %s = %s" % (input_val_1, input_val_2, dopelnienie_2, prod_res))
