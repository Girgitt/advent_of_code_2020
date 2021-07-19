from collections import OrderedDict
input_data = """FBFBFFFLLL
FFBBBBFLRR
BFBFBBBLLL
FFBBBBBLLL
BFFBBBBRLL
BBBFFBFRLL
FFBBFFFRRR
FFBFFBBLRL
FBFFBFBRRR
FBFFBFBRLL
BFFBFFFRLR
FFFBBFFRRR
BFBFBBFLLL
FBFBBFFRRL
BFFBFBFLRL
FBFFFBFRRL
FBFBFFBRRR
FBFBFFBRLL
BFBFFFBLLL
BFBFFBBLRL
FBFFFFBRRL
BFFFBFFRRL
FBFBFFFRLR
BFFFFBBLLR
FFBFFFFRLR
BBFBBFFLLL
FFBFFBFRRR
FBFBFBBRRR
BBBFFFFLRR
FFFBFFBRRR
BFFBFBFLRR
BFFFBBBRLL
FFBFBBBRLR
FBFFFFBLLR
FBBFBFFLRL
FBFFFFFRLL
FBBBBFBRLL
BFBBBBFLLL
FBBBFBBRRR
BFFFBFBLLL
FBBBBBFLRL
BFBBBFFLRR
BFBBFBBLRR
FFBBBFFLRR
FFBBBBFRLR
BFFFBFFLLR
FBBFFFBRRL
FBBBFBBLRR
FFBBFBFRRL
FFFBFBBLRR
FBFBBBBRLR
FBFFBFBLLL
FBBFFFFRLL
BBBFFFBLRL
FBBFBBBLLL
FFBBFBBLLR
FBFFFBBRLR
BBFBBFFRRL
FFFBBFFRLL
FBFFBBBLRL
BFFBFFFLRL
FFFFBBFRRR
FBBFBBFLLR
BFBFBFBRRL
BBFBFBBRRR
BBBFFFBLLL
BFBFFBFRLL
FFBBFFBRRR
BFBBFFFRRL
BFBBBFBRRL
BFBBBBBRRR
BBFBFBFRLL
BBFFBFFLRL
BFFBBFFLLL
BFBFBFFLLL
FBBBFFFRLR
BFFFBBBLRL
FBFBFFFLRR
FBBBFBBLRL
FFBBFBBRLR
FBBFFFFLRL
FFFBFBBLLL
FBFBFFBRRL
BBFFBBFRRR
BFFFFBFRLR
FBFBFFBLRL
FFBFFBBLLL
FBFBBFBRLR
BFFBBFBRLR
FFBFBFBLLL
FFBBFFBRLR
FBBBBBBLLL
FFFBBBBRRL
BFBBFBBRLL
BBFFFBFLLR
FFBBBBFRRR
BFBFFFBRLL
BFBFFBFLRR
FFFFBBBLLR
FBFFBBFRLL
FFFFBBBRRL
FFBFFBBLLR
FBFFFBBLLL
FFBBBBFRLL
BBFFBFFLLL
BFBBBBBRRL
BFFBFBFLLL
FFBFBBFLLR
FFBFBBBLRL
BFFBFFBLRL
FBBBFFFRRR
FBBFFBBRRL
FBBFFBBLLR
BBFBBBFLRR
BBFFFBFRRL
FBFBFBFRRL
FFBFBBFRRR
FBFFBBBLLR
BBFBFFBRLL
BFBBBFBLRL
FFBBFFFLRR
BFFFBFFLRL
BFFBBBFLLL
FBBFFFBLRL
BBBFFBFLLL
BFBBFBBRLR
FBBBBBFRLL
FBBBBFBLRR
FFBFBBFRLR
BBFFFFBLLL
FBFBBBFRLR
FBBFBBBLRL
BBFFBBBRLL
FFBFBFFLLR
FFFBBFBRLL
FFBBBFFRLL
BFBBFFFLRR
FBBBFBFRLL
BBFBFBFLRR
BFBBBFFRLL
FFBFFFFRRR
BFBBBBBLLR
FBBBBBBRRR
BBFBBFFLRR
BFBFFBBLRR
BFFBFBBLRR
BFFBBFFRLR
FBBBFFBRRR
FFFFBBBRLR
FBFFFFFLLL
BBFFFBFLRR
BFFFFBFLRL
BFFBFFBLLL
BFFBBFBRRL
FFFBBFFLLR
FBFFFFBLRL
FBFFFBFLLR
FFBBFBBRLL
FFBFFBBRLR
FFBFFFBRRL
FFFBFBFLRR
BBFFBFFRRR
BBFFFFFLLL
FBBFBFBRLR
BBFBBFBLLR
BBFBBBFRRL
BFBFFBBLLR
FBBFFFFLLR
FFBFBFFRRL
FFFBFFBRRL
FBFBFFBRLR
BFBBFBFRLL
BBFBBBBLLR
BFBBBFFLLL
BBFBBBBRRL
BFBFBFBRLR
BFFFBFBRRL
BFFBBBFRRL
BFFFBFBRLL
FBFBFBFLRR
FFBFFBFLRR
BBFBBBBRLL
BFBBBFFLRL
FBBBBFBLLL
BBFBBBFLRL
BFBBFBFLLL
FBBBBBBLRL
FFBFFFBLLL
FFBBBBBRRL
FBBFFFBLLL
FBBBFFBLRR
BBBFFBFLLR
FFFFBBBLLL
FBBBBBBRLR
FFBFFBBRRR
BFFFBFFRLL
BBBFFFBRRR
FBBFBFFLLL
FBFBFBBRLR
FBFFFFFLRL
FFBBBBBRLR
FBBBFFBRRL
BFBBBBFRRL
FBFBBFBLLR
BBFFBBBLLL
BBBFFBFRLR
FFBBFFFLLL
FFBFFBBRRL
FBBBBFFLLL
FBBBBBFRRR
FBFFBBFLLR
FFFBFFFLRL
FFFBFBBRRL
BFFFBFFLLL
FBBBFBBLLL
FFBFBBBLLL
BFFFFFBLRL
FBBBFBFLRR
BBFFBBFLLR
FBFFBBBRLR
BFBFFFFLLR
BFBBBFBLLL
BBFBFBBRLR
FFFBBFBLLR
BFFBFBBRRL
BBFFBBFLRR
BFFBBBFLRR
FBFBBBBRRL
BFBFBFFRRL
BBFBBFFRLR
BBFBBBBRLR
FFBBFFFLLR
BBFBFBBLRR
FBFBFBFLLL
BFFFFBBRRR
BFBBBBFRRR
BFFFFFFLRL
BBBFFBFLRR
FFFBBBBRLR
FBBFFFBRLL
BBFFBBFLRL
FFBBBBBRRR
BBFFBFFRLL
BFFFFFBRRR
FBBFBFBRRR
BFFFFBFRRR
FBBFBBBRLL
FFFBFBBRLR
FBBBBFFRLR
FBBFFFBLLR
FFBBFFBLLR
BFBFFFBLRR
FFBFBBBRRR
BFBFBFBLRR
BFFBBFBLRR
FBFFBFFRLL
BFFBBBFRLR
FBFFFBFRLR
FFFBFBFRLL
FBBFBBFLLL
BFBBFFFLRL
FBBFBFFLRR
BBFFFBFRRR
FBBFBFBLRL
FBBBFBFLLR
FBFBBBBLLR
BBBFFFFLLR
BFBBFBFRRR
FFBFBFFRLR
FFBBFBBLLL
BFFFFFBLLR
FBBBFBFLLL
FBBFBBFRLR
BBFFFFFRLL
BFBFBFFLRR
FBFBBFFLRR
BBFBBFBRLR
BFFFBBFRLR
FBFFBBFRRR
FBFFFBFLLL
FBBFBBBRRR
BBFFFBBLRL
FFBFFBFLLR
BBFFBFFLLR
BBBFFBFRRL
FBFBBFBRRR
FBBBBBBRLL
FBFFFBBLRR
FFFBFFFLLL
BBFBBFFRLL
BBFFFBFRLL
BBFFFBFLLL
FFBBFBBRRL
FFFFBBFLRL
BFBBBBFLRL
BBFBBFFLLR
BBFFBFBRRR
FBFBBFFRLL
FBFBBFBLLL
BFBBBFFRRR
FFBBBFBRLL
FFBFBBBRRL
BFBBFBFRLR
BBFBFBFRLR
FBFBBBFLLR
FBFBBBFLRL
BBFFBBFRLR
FFBBFFFLRL
FFFFBBFLRR
FFFBBFFLRL
FFFBFBFRRR
FBBFFBBLRR
BBFBBFBLRR
BFFBBBFLRL
FBFFBFFRLR
FBFFFBFRRR
BFFBBFFRRL
BFFFBBFRLL
BFBFBBBLRR
FFBFFFBLRL
FBFBBFBRLL
FBBBBFBLLR
FFBFBFBLRL
FBFBBBFLRR
FFBBBBBLRR
FFBFFFBLLR
BBFFFBBRLL
BBFFBBFLLL
FFFBBFBLRL
FBBBFBFRRR
BBFBBBBRRR
FBBBFFBLLR
FBBBBFBLRL
FBFBFFFRRL
FBBFFFFLRR
BFFFBFBLRL
BFFBFFBRLL
BFBFFFBLRL
FBFBFBFRLL
BBFBFBFLLL
FBBBBBFRRL
BFFBFFFRLL
FBBBFBBRRL
BFBBFFBRLR
FFBFBFFLLL
FFBBBBBLLR
FFBFBFBRRL
FFFBFFBLRL
BBFFFBFLRL
FBFBFBBRRL
BFFBFFBRRL
BBFBFBBLRL
BBFBFBFRRR
FBFFBBFRLR
FBFBBFBLRR
FBBFFFFLLL
FFFBFFFLRR
FFFBBBBRRR
BBFFFBBRLR
FFBFFFFRLL
FBFFBFBRLR
FBFBFBBRLL
FBBBBFFLRR
FBBFBFBRLL
FBBBFBFLRL
BBFBBBFLLR
FFBFBBBLLR
BFFBBBFRRR
FFBBFBFLLL
BFBBBFBRLR
FFBFBBBRLL
FFBFBFFLRR
FBFBFBBLLL
BFBBBBFLLR
FFBBFBFRRR
FBFBFBBLRR
BFFFBFBLLR
BFFBFBFRRL
FFFBBBFRLR
FFFBBFFRRL
FFFBBBFLRL
FFFFBBFLLL
BBBFFFBLRR
FBFFFFBRRR
FFFFBBFRRL
FBFBBFFRLR
BFFBBBBLRL
FBFFFFBLRR
FFFBBFBLRR
FFFFBBFRLL
FFFBBFBRRR
FBFFBBBRRL
BBFFFFFLRL
BBFFBBFRRL
BFFFBBBLLL
FBBBBBBLRR
FBBBFFFRLL
FBFFBFFLRR
FFBFBBFLLL
FFBBBFBRRR
BFFFBFBRRR
BBFFBFBRRL
BFFFBBBRLR
FBFFFBBRRR
BBFBBFBRLL
BBFFBBBRRR
FBFFBFBLLR
FFBFFBBLRR
FBBFBBFLRL
FFBFFBFLLL
FFFBFFFRRL
BBBFFFBRLL
BFBFBBBRRL
FFBFBFBLLR
FFFBBBFRLL
BFFFBBFRRR
BFBBFFFRLR
FBBFFBBRLL
BFBBBBBLRL
BBFBFBFLRL
BFBBBFBLLR
FBBFFBBRRR
BFFFFBBLRR
FBBFBBBLLR
BFBFBFBRLL
BFBFBFBRRR
BFFFFBFRRL
FBFBBFFLLR
FBBFBBFRRL
BBFBFBBLLL
BFFBFFBRRR
FBBFBFBLRR
BFFBBFBLLR
BFBFBBBRLL
FBFFBBBLRR
BBFFBFBLRR
BBFFFFFRLR
BBBFFBBLLR
BBFBBFFRRR
BBFFFBBLLR
BFFBFFBRLR
FBFFBFFLLL
BFBBFFFRLL
FFFBFBBRLL
FBFBFBBLRL
FFFBBBFRRL
BFBFBBFRLR
BBFFFFFRRL
FBBFBFFLLR
BFFFBBFLRR
BBFBBFBRRR
BBFFBBBLRR
FBFBBFFRRR
BFFFBFFRLR
FFBBFBFLLR
FBFBFFBLRR
FBFFBFBLRL
FFBFBFBRLR
FBBFBBBRRL
FFBBFFFRLR
FFFBFBBRRR
FBBFBFFRLL
FFBFBFFRLL
FFBFBBBLRR
FFBBBFFLLR
BFBFFFFLRR
FFBBBFBLRL
BBFFFBBRRL
FFBFFBFRRL
FFBBBFBRLR
BFBFFBFLLL
BBFBBBFRLR
BFBFFBFRLR
FFBBBBBLRL
FFFBBFFLLL
BBFFBFFRRL
BFBBFBBLRL
BFFBFFFLRR
BBBFFFFLRL
BFBFFBBRLL
FBBBFFBLLL
FBBFFBBLLL
BBFFFFFLLR
FFBBFFBLRR
BFBBFBFLRR
BBFFFFFLRR
BFFBFBFLLR
FBFBBBBLLL
FBBBFFBRLR
FBBBFBBLLR
BFBFBBBLRL
BFFFBFBRLR
FBBFFBFRRR
BFFFBBFLLL
FFBFFFBRLR
FFBFFFBRRR
FFFBFFBRLR
BBFBFFFRLL
BFBFFBFRRL
BFBFBBFRRL
FBBBBBFLRR
BFFBBBBLRR
FFBFFBFLRL
BFBFBBFLRL
BFFFFFFLLR
FBFFBBBRRR
BFBFFBBRLR
FBBFBFFRLR
BFFBBBFLLR
BFBFFFBLLR
FFBFFFFRRL
FFFBBBBLRR
FFFBBFBLLL
BFFBFBBLLR
FBFFBFBLRR
FFFBBBBRLL
BBBFFFBRLR
BFBBFFFLLL
BFBBBFFLLR
BFBFBFFRRR
BFFFFBFLLR
FBBBBFBRLR
BFFBBBBRRL
FBFBFBFRLR
FFBFBBFRRL
BFFFBBFLLR
FFBBBFBLLL
FFBFBBFLRR
BFFFFBFLLL
FBBBBBFRLR
BBFBBBFLLL
FBFBBFBRRL
FFBBFBFRLL
BFBFFFFRRR
FBFFFFFRLR
FFBBFFBLRL
BBFBBBBLRL
FBBFFBFLRL
BFFFBFBLRR
FBFFFBBRRL
BBFBFFBRLR
FFBBFBBLRL
FBBBBFFLRL
BFFFFBBRLR
FBFFBBFLRR
FFBFBFFRRR
FFBBFBFLRR
BFFBFFFRRL
FBBFFBFRLR
FBBFBFBLLR
BFBFFBBRRL
FBFFFBFLRR
FBFBBFBLRL
BFFFFBFRLL
BFBFBBBRRR
FFFBFFFLLR
FBBBFFFLRR
FFBFBBFLRL
BFFFFBBLRL
BBFFBFFLRR
FBBFFFFRRR
FFFBFBBLRL
BFFFBFFLRR
BFBBFBFLRL
FBFFBFBRRL
BFBFFFFLRL
FBBFFFBRRR
FFBBFFBRLL
FFBFFBFRLL
BBFBFBBLLR
BFBFBFFLLR
BFFFBBBRRL
BBFBFFFLLR
FBFBFFFLRL
BFFBBFFRRR
BFFBFBBRLR
BBBFFBFLRL
BBFBFFBLRR
BBFBFFFLLL
FFBBBBFLLL
BFBBFBBRRR
BBFFFFBRRL
FFBFFBBRLL
FBBFFFBLRR
FFFFBBBLRL
FFBFBFFLRL
FBBBBFBRRR
BFFBBFBRRR
BFFFBBBLLR
BFFBFBFRLR
BFFBBBFRLL
FFFFBBBLRR
BFBFBBBRLR
BFBFBFFRLL
FFBBFFFRRL
FBBFFBFRRL
BBFFBBFRLL
FBBFFBBRLR
BFBBFFFRRR
BFBBFFBRRL
FBFFFBBRLL
FBBBBBBRRL
FBFFFFBRLR
BFBBFFBLLR
BBFBFFBRRL
BFFBBFFLLR
BFFFFBBRLL
BBFFBFBLLL
FBBFFFFRLR
FBBFFBFLRR
BFFBBFFRLL
BFBBFBBLLL
FBFBFBFLLR
BFFFBBBLRR
BFBFBFBLRL
BBBFFFFRRR
FFBFBFBRLL
FBFFBFFRRR
FFBFFFBRLL
FBBFBBFRRR
FFFBBBFRRR
FBFFBFFRRL
FFBBFFBRRL
FBBBFFFLLR
BBFBBFBRRL
BBFBFFFRRL
FFFBBBBLRL
FBBBFFFRRL
BFBBFFBLRL
FBFFFFFLRR
FBFFBBFLRL
BBFFBBBRRL
BBBFFBBLLL
FBFFBBBRLL
BBBFFFFRLL
FFBBBFFRLR
BBFFFFBRLL
FBFFFBBLLR
BFFBFBFRRR
FBFFBBBLLL
FBFBBBFRLL
BFFFFFBLRR
BFFBBFFLRL
FFBBFBBRRR
FBFFBFFLLR
BFFBBBBLLR
BFFFFFFRRR
BBFBBBFRRR
BBFFFFBLRR
BFFBBFBLLL
FFBBFFBLLL
BBBFFFFRRL
FBBFBBFLRR
FBBFFFBRLR
FBFBBFFLRL
FBFBFFFRLL
FBBFFBBLRL
BFFBBBBRRR
FFFFBBFLLR
BBFFBBBRLR
BFFFFFFRLL
FBBBBBBLLR
BBFFFBBLRR
BFFFFFBLLL
FBBBBFFLLR
BBFBFFFRRR
FBFBFFBLLL
FBFFFFBLLL
FFBFFBFRLR
BFBFFBBLLL
BFFBBFFLRR
FBBBBBFLLL
FFBBBFBLRR
BFFFFFBRLR
BBFBFBBRRL
BBFFFFBRRR
FFFBFBFLRL
FBFBBBBLRR
BFBFFBBRRR
FFBFFFFLLL
BFBFFBFLLR
FBBFBBBRLR
FFFBFFFRLL
FFFBFBFRLR
FFBBBFFLRL
BFFBBBBRLR
FBFFBBFLLL
FFFBBFFLRR
BBFBFBFLLR
FFBBFBFLRL
BBFFBBBLRL
BBFFFFBLLR
FFBFFFBLRR
BFBBFBFLLR
BFBBBBBLLL
BBFBBFBLRL
BBFBFFFRLR
BFFBFFFLLL
BBFBFFBRRR
FBFBBBFRRR
FBBBBFFRLL
BFFBBFBLRL
BBFBFFBLRL
BFBBFFBRRR
BBBFFFFLLL
BFBFFFFRRL
FBFFFFFRRR
BFFFFBBLLL
BFBBFFBRLL
FFBBBBBRLL
BFFBFBBRRR
BFBBFFFLLR
BFBBFBBLLR
FBBBBFBRRL
FBFBFBFLRL
BFBBBBFRLL
FFFBFFBLLL
BFFBFFFLLR
BFBBBFBRLL
FFFBBFBRRL
FFBFBFBRRR
FFFBFBBLLR
BFBBBFBRRR
FBBFBBFRLL
BFBBFBBRRL
BFBBBBFRLR
FFFBBBBLLL
BBFFFBBLLL
FFBBBBFLRL
BFBBBBBRLL
FBBFFBFRLL
FBFFFBBLRL
FBBFBFFRRR
FFFBFBFLLR
FFBBBFFRRL
FBBBFBBRLR
BBFBFFFLRR
FBFBBFFLLL
BBFFBFFRLR
BBFBFFFLRL
FBBBBFFRRR
FFBBBFBLLR
BBBFFFBRRL
FBFBFFFLLR
BBFBFFBLLL
FFFBBFBRLR
FBFFFBFLRL
BFFBFBBLLL
BBFBFBBRLL
FBFFBBFRRL
BFBFFFFRLL
BBBFFBBLRL
FFFBFFBLLR
BFFBFBBRLL
FFBFBFBLRR
BBFBFBFRRL
FBBBFBFRRL
FFFBBBBLLR
FBBBFBBRLL
BFBFBBFLRR
BFFFFFFLLL
FFFBFFFRLR
BFBBBFFRLR
BFFFFFBRLL
FBFFFFFLLR
FBBBFFBRLL
FBBFFBFLLR
BFFBFFBLRR
FBFBBBFLLL
FBFFFFFRRL
BBFFFFBLRL
BFBFFFFRLR
FBBFFFFRRL
BFFBBBBLLL
FFFFBBBRRR
FFBBFBBLRR
FBBFFBFLLL
BFFFFBBRRL
FFBBBBFRRL
BFFFFBFLRR
BFFFBBFRRL
BFBBBFFRRL
BFFFBFFRRR
FBFBBBBRRR
FBFFBFFLRL
FBBBBBFLLR
BFBFBBFLLR
BBBFFBFRRR
BFBBFFBLRR
FBBFBFFRRL
BBFBBFBLLL
BFBBFFBLLL
FFBBBFBRRL
BFBFBFBLLL
BFFBFBFRLL
BBFFBBBLLR
FFFBFBFLLL
FFBBBBFLLR
FFFBFBFRRL
BFBFFFBRRR
FFBFBBFRLL
FFFBBBFLLR
FBBFBFBLLL
BBFFFFFRRR
FFFBFFFRRR
BFFFBBBRRR
FFBFFFFLRL
FFFBFFBLRR
FFBBFBFRLR
FBBFBBBLRR
BFFBBFBRLL
BBFFFBBRRR
FFFFBBFRLR
FBBFBFBRRL
FBFBFFBLLR
FBFBFBBLLR
BFBFBBFRRR
BBFFBFBLLR
FFBBBFFLLL
BBFFBFBRLL
BFFFBBFLRL
BFBFBFFRLR
BFBFFFFLLL
FFBBBFFRRR
BBFBFFBLLR
BFBBBBFLRR
BFFBFBBLRL
FFBBFFFRLL
FFBFFFFLLR
BFBFFFBRRL
BFBFBFFLRL
BFFFFFFLRR
BBFBBFFLRL
FBFFFFBRLL
BBFFBFBRLR
FBBBFFFLLL
FFFBBBFLLL
BFFBFFFRRR
BBFBBBBLLL
BBFFFBFRLR
FBFBFFFRRR
FFFBBFFRLR
BFFBFFBLLR
BBFFBFBLRL
BFBFBFBLLR
FBFFFBFRLL
BBFBBBFRLL
BFBBBBBRLR
BFBFFFBRLR
FFFBBBFLRR
BFBFFBFLRL
BBFBBBBLRR
BFBFBBFRLL
FFFFBBBRLL
BFBBBBBLRR
FBFBBBBRLL
BFBBFBFRRL
BBFFFFBRLR
FBBBFBFRLR
BFBFFBFRRR
FBFBBBBLRL
BFBFBBBLLR
FFBFFFFLRR
FBFBBBFRRL
FBFBFBFRRR
BFFFFFFRLR
FBBBBFFRRL
BFFFFFBRRL
BBBFFFFRLR
FBBBFFBLRL
FBBBFFFLRL
FFFBFFBRLL
BFFFFFFRRL
BBBFFFBLLR"""


def get_input():
    seats_raw_data = [item for item in input_data.splitlines() if item]
    print("len seats_raw_data: %s" % len(seats_raw_data))
    return seats_raw_data


def get_solution_1():
    seats_data = get_input()
    # BFFFBBFRRR: row 70, column    7, seat    ID    567.
    # FFFBBBFRRR: row    14, column    7, seat    ID    119.
    # BBFFBBFRLL: row    102, column    4, seat    ID    820.

    expected = [(70, 7, 567), (14, 7, 119), (102, 4, 820)]
    input = ['BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']
    for test_try in range(3):
        got = get_decoded_seat(input[test_try])
        if not expected[test_try] == got:
            print("wrong result for %s, expected %s gto %s", input, expected, got)
    max_seat_id = 0
    for seat_code in seats_data:
        seat_id = get_decoded_seat(seat_code)[2]
        if seat_id > max_seat_id:
            max_seat_id = seat_id
    print("highest seat id: %s" % max_seat_id)


def get_solution_2():
    seats_data = get_input()

    all_seat_rows = [item for item in range(0, 128)]
    all_seat_cols = [item for item in range(0, 8)]
    all_possible_ids = []
    for row_number in all_seat_rows:
        for col_number in all_seat_cols:
            all_possible_ids.append(row_number * 8 + col_number)

    min_row = 9999999
    max_row = 0
    min_col = 9
    max_col = 0
    for seat_code in seats_data:
        seat_data = get_decoded_seat(seat_code)
        seat_row = seat_data[0]
        seat_col = seat_data[1]
        seat_id = seat_data[2]
        if seat_row < min_row:
            min_row = seat_row
        elif seat_row > max_row:
            max_row = seat_row
        if seat_col < min_col:
            min_col = seat_col
        elif seat_col > max_col:
            max_col = seat_col
        all_possible_ids.remove(seat_id)
        #print("removed ID: %s" % seat_id)

    print("min row: %s" % str(min_row))
    print("max row: %s" % str(max_row))
    print("min col: %s" % str(min_col))
    print("max col: %s" % str(max_col))

    print("free seat IDs: %s" % str([item for item in all_possible_ids if item < (max_row * 8) and item > (min_row * 8)]))


def get_decoded_seat(seat_data):
    row_part = seat_data[:-3]
    col_part = seat_data[-3:]

    if len(row_part) != 7:
        raise Exception("wrong row part len")

    if len(col_part) != 3:
        raise Exception("wrong col part len")

    seat_rows = [item for item in range(0, 128)]

    for idx, row_code in enumerate(row_part):
        #print("in: %s" % seat_rows)
        if row_code == 'F':
            # lower part
            #print("  F - keeping lower half")
            seat_rows = seat_rows[:int(len(seat_rows)/2)]
        elif row_code == 'B':
            # upper part
            #print("  B - keeping upper half")
            seat_rows = seat_rows[int(len(seat_rows)/2):]
        else:
            raise Exception("wrong row code: %s", row_code)
        #print("  out: %s" % seat_rows)
    if len(seat_rows) > 1:
        raise Exception('unexpected row outcome: %s', str(seat_rows))
    row = seat_rows[-1]

    seat_cols = [item for item in range(0, 8)]

    for idx, col_code in enumerate(col_part):
        if col_code == 'L':
            # lower part
            seat_cols = seat_cols[:int(len(seat_cols) / 2)]
        elif col_code == 'R':
            # upper part
            seat_cols = seat_cols[int(len(seat_cols) / 2):]
        else:
            raise Exception("wrong col code: %s", col_code)
    if len(seat_cols) > 1:
        raise Exception('unexpected col outcome: %s', str(seat_cols))
    col = seat_cols[-1]
    seat_id = row * 8 + col

    return (int(row), int(col), int(seat_id))

