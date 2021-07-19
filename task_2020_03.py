from collections import OrderedDict
input_data = """
.#.......#...........#.........
..##.......#.#.#.....##...#....
.......#..#.....#...#..........
...#..........###...#........##
#.#..#.#.##.#........#.#.....#.
#..#....#..#....#..............
#..#........#..................
..#.#...#.#...#....#.#.#..#....
..............#..#.............
.##....#...................#...
........#..........#......#...#
.##..#..#...##..........#...#..
.#...#....#.........#...#.....#
.#........##............#.#....
...........#..............##...
.#..#......#..#..............#.
..#.#.#...........#........#...
..###..........#....#.#......#.
.......#...##..........#.......
........#...#..................
....#....#..#.......#........#.
.......##.#......#.....#...##..
..#.#........................#.
.#.....#.##..............#.#...
..#.#...#.#..#....#....#.......
.#....##.....#....#........#...
..#...........#.##....#...#....
..#.##...#....#.#.....##...#...
.......#...####...#...#.......#
.#...#.........................
.......................#.......
.....#.#.........#..........#.#
#.........#............###..#..
.....#.#.............###.......
...#..#........#.#.......#.....
...................#....#......
...#..#...#............#..##...
...#.....#....#.......##......#
.....#....#...##..#..#...#...#.
..........#...........#.#.#....
..#.......#...#.....#......#...
.........#.......##......#..#.#
..#.....#..#.###...#.#......#..
#....#...#..#...#.....#........
..#......#..#.......#.#.....#..
#......#...#......#.....##.#...
........##.......#.......#.....
.#.#...............#...........
..............#...#.#....#.....
....#......#.#..#......#.......
...##....#....#...#............
.#...............#...........#.
.#.#...#.#.....#.....#...#.#...
...##...........#.....#..#...#.
.#.#...##.#.#......#......#....
.##.....#.......##....#.#.#....
.......#...........#....#....#.
....#...........#......#.####..
......#....#...#...##.......#..
......................#.#####..
..#...#.#...#..#..#......#.....
....#........##.......##....#..
#.#......##.........##.#..#...#
.#.#....#...#..#...#...##....#.
.....##...#....#....#.#........
......#..#....#.#...#..........
.........#...................#.
............#.###....#.#.......
...#.#.....#......#....#.#..#..
..............#..#.#.#.#.......
#..##...................##.....
..#.......#..#.........##..#...
.........##...#......#........#
..#.........#........##.###.#..
...........#.#....#.....###....
..#....##.#..#.##....#.....##..
..#.....#.##..................#
#....#.........................
..............#..#...#.#.......
......#..#.#.##....#..........#
..#.........#.####.....#.......
......#..#.#..........#...#....
......#.................#..#.#.
.....#..........#..............
....#.....#............#....##.
.....#.....#........#..........
............#.....#...#........
........#....#.#...............
#.....#.........#......#..#.#..
...#..#......#......#.......#..
.....#......#.#....#..#...#...#
......................#..##....
.............#.........###....#
#..............#.#..........##.
...#.#.................##......
...........#.#.....#...........
.........#.................#.#.
........#........#...#..##...#.
........#......##.......###....
..............#.#.#............
.#.....###...##.#......#.....#.
.............#......#.#.#...#.#
..#.........#.......#.....#....
......#........#...##......#...
.##..........##......#.#.....#.
..#.##....#....#...............
......#...#..#.....#.....#...#.
.......##..##..#............##.
..............#...##........#..
#....#................#..#.....
........#.......#.#.#...#......
......#.......#..............#.
#.#..#...#........#....#..####.
..#........#...........#.....#.
.##...........................#
.............#...........#.....
.#.....#.#...#.........#.......
..........#...#....#....#......
.#..#........##....#...........
.......###......##...#.........
..........#.#.#..#.#....#......
........##..#.........#....#...
........#.#......#.#...#.#..#..
....#....................#.##..
##....#..#...........#.....#.#.
...#..............##...##..#.#.
......#.##.#.......#..#...#....
....#..#..##.....#.....#.#....#
.......#....##.##..............
#..##....#.....#.#.............
..................#......#..#..
..#......#...#..#.......#...#..
...........#....#.#.....#......
#..#...##.........###..#......#
.......#......................#
#.......#....................#.
..#..#..........#..#..#....#...
.##..#..#.....#.#..##..........
#..###.......#..##..#...#..#.#.
.....##......###.....#.#.##...#
..............#...#....#.#.....
#...........#..................
..............#....#..##..#..#.
.........#.............#.......
.#.#....#....#...............##
.##.##.#.....###.....#.........
....#..............##......#...
....#........##................
....#.....#....#....##....##...
.#........#......#......#......
....#..........#...............
##..........#......#.....#.....
........#.#..#.#..#.....##.....
..##......#.#.......#.#..#.....
.#.......#......#...........#..
..#.#..#.#..................#..
...#...#...#...##......#.......
.#...##....#...#...#...#.......
.......#.#.......#.............
.#.##.#.....#...........#.##.#.
.#.##.#........#...##..........
.#.....#.....#....#..#.........
...##.............##...........
.#........##.....#.......#...#.
...........#..#..##........##..
.....#..#......................
..#.......#....................
.....#......#....#....#.......#
........#..#.#.....#......#....
..........#..#.....#......#....
..........#####.....#........#.
........#..#...#.#....#......#.
.........#...#....#.#..........
......#....##..........#...#...
#..............###.#.#.........
.#.#............##......#.#..#.
......#........................
...#..#......#.......#....#...#
.......#....##.....#.#......##.
...........#..........#..#.....
...........#..#.....###......#.
.......#....#..##......#.......
.........#.#.#.......#..#...#..
.......#.......##.....##...#...
..............#....#.....#.....
...#....#.....#.#..........##..
###.........#.............#....
...##......#.#........#....#..#
#....###.......#...#.#......##.
....#...##.......#......#.....#
.....#......#..................
#........##....#....#.#........
........#.......###...#........
........#..#.......###.........
..............#......#..#......
#......#.....#....#.#..........
.#......##.#.#.....#...#.#....#
.##...........#..#.##.....#....
.....#.....................#...
.#..#...#...##.#...#...........
.......#.......##..#.#..#......
.......##.....#.....#..........
.................#.............
#........#..#.......##.........
#...#..###.#..#....#.#.###.....
..#.......#.......#.......#....
..............#............##..
.#...#..#...##.........#....#..
#...........#...#..............
.......#.....#......#..#.....#.
..........#......#.............
##.........###..##.#....#..#.#.
..............###..............
#..##.............##.....#.....
....##...................#..#..
....#.....#..............#..#.#
........#........##...#.....##.
#...........#.##..........##...
#......##.....#...............#
..##..#....#.................#.
#.......##.....................
...............#.##..##......#.
..#.##..#.#....#.......##......
......##....#............##....
.#..#..##.....#.##....#........
#.........#..........#...#....#
...#.......#.............#.#.#.
..##............#...##........#
.......#.#.#........#..........
.....#.............#.....#.....
.........#.........#.........#.
#.....#....#.......#...........
.........#....#.............#.#
.##..#.......#...#......#......
....#....#....#........#....#..
............#.......#..#......#
.#............#.##........##...
..#...##...#....#...#.#...#..#.
#...#..........#..##.........#.
..#.........................#.#
...........#.........#..#.##...
.#..................#..#.......
......#......#...........#..#..
...##.....#.....#..#.......#...
.........#.#.......#......#....
...........#................#..
.....#...#..#............##....
.#.......#..#....#..........#..
#.....#..#.....#..##.......##..
...#.......#...#....#...#.#..##
...#...##......#....#....#.....
.......###.#..#.......#......#.
........#.#...#..#..#...#....#.
....#.........##.#.....#.......
....#.........#..##........#...
..#...........#......#....#.##.
.....................#.........
...................##......#..#
......#.#.....##..##..........#
..#.##........#.#.#..........#.
.#.......#...##.#....#....#....
#.#......#..#..#.......#.......
.............#........#.......#
....#...#.....#........#...#...
..#..............##..#.........
..#.................#..#...##..
....#..#...#...................
......#.........##.#..#..#...##
........#..#....#.......#.#.##.
.#...#...........#..........#..
##.....#...#............##...#.
.##.....#...#..................
.#.......####.#..##.##.#......#
.............#...#..#..#.......
...#.##.........#.#....#.......
...........##...##....#....##..
........#......#...#...........
...........#..#...#....#.##....
..##....#..........#....#...#..
#....#.#.#.......#.#...........
......#............##..........
#.#.###..#....#.......#...#....
.#......##..#..#.#.........#..#
..#.........#........#....#....
......##.#.......##....#..#..##
.............#...#............#
......#......#...#.#.#.##.#....
#.#...#.##.....#..............#
..........#.............##.##..
#......#....#...#.#.#.#..#....#
........#........#...#.#......#
.....#...........#.............
...........#....#..........#...
....####...#..##....#.#........
.#......#...#..#...........#...
#......###..#.##.###...........
..#...........#.........#....#.
................#.#....#..#.##.
...................#......#....
....#.#.....#.......#...###.##.
.#........#.#....#...#..#...#..
....#..###.................#..#
.....#.#..#........#......#..#.
....#.....#...............#...#
............##.#.........#..#..
.......#..#..##.#.#...##.......
..#..........##..#..#........#.
..............#..#...#.........
......#.#....#........##.......
.#.....##....#..#...#.......##.
..............#.##.............
#..#..#...##....##.#.....##.#..
..#...###..#.........##........
........##......#.....#..###...
.....#......##.###.............
....#.....#.#..#.#..#..........
....#..#.......#...........#...
.#.............#..#......##....
..#.#......#.#.................
.......#.#.#............#..#...
......###....##............#..#
.........#....#......#.........
..........#...............#..#.
"""


def get_input():
    parsed_items = [item for item in input_data.splitlines() if item != '']
    return [item * 100 for item in parsed_items]


def get_solution_1():
    forest_data = get_input()
    pos_x = 0
    x_incr = 3
    trees_hit_cnt = 0
    for tree_line in forest_data:
        if tree_line[pos_x] == '#':
            trees_hit_cnt += 1
        pos_x += x_incr

    print("rees_hit_cnt: %s" % trees_hit_cnt)


def get_solution_2():
    forest_data = get_input()
    transform_data = [{"x": 1, "y": 1},
                      {"x": 3, "y": 1},
                      {"x": 5, "y": 1},
                      {"x": 7, "y": 1},
                      {"x": 1, "y": 2}
                      ]

    hit_trace = []
    for move_data in transform_data:
        pos_x = 0
        line_cnt = 0
        trees_hit_cnt = 0
        while line_cnt < len(forest_data):
            tree_line = forest_data[line_cnt]
            if move_data['y'] == 2:
                if (line_cnt + 1) % 2 == 0:
                    line_cnt += 1
                    continue

            if tree_line[pos_x] == '#':
                trees_hit_cnt += 1
            pos_x += move_data['x']
            line_cnt += move_data['y']
        #print("move data %s hit trees: %s" % (str(move_data), trees_hit_cnt))
        hit_trace.append(trees_hit_cnt)

    print("hit_trace: %s" % hit_trace)
    result = hit_trace[0]
    for hit_val in hit_trace[1:]:
        result *= hit_val
    print("result: %s" % result)


