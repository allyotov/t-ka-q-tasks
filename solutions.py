import logging

logger = logging.getLogger(__name__)


def task_1_1(char_array):
    if '0' in char_array:
        i = char_array.index('0')
        logger.debug(i)
        return i
    return -1


def task_1_2(x1, y1, x2, y2, x3, y3, x4, y4):
    def get_minmax_corners(x1, y1, x2, y2):
        if x1 < x2:
            left_x = x1
            right_x = x2
        else:
            left_x = x2
            right_x = x1

        if y1 < y2:
            low_y = y1
            up_y = y2
        else:
            low_y = y2
            up_y = y1
        return left_x, low_y, right_x, up_y
    x_left_1, y_low_1, x_right_1, y_up_1 = get_minmax_corners(x1, y1, x2, y2)
    x_left_2, y_low_2, x_right_2, y_up_2 = get_minmax_corners(x3, y3, x4, y4)

    x_vertexes = {x_left_1: 1, x_right_1: 1, x_left_2: 2, x_right_2: 2}
    y_vertexes = {y_low_1: 1, y_up_1: 1, y_low_2: 2, y_up_2: 2}

    x_coords = list(x_vertexes.keys())
    x_coords.sort()
    x_verts_colored = [x_vertexes[x] for x in x_coords]

    y_coords = list(y_vertexes.keys())
    y_coords.sort()
    y_verts_colored = [y_vertexes[y] for y in y_coords]

    x_intersection = False
    if x_verts_colored[0] == x_verts_colored[3] or x_verts_colored[0] == x_verts_colored[2]:
        x_intersection = True

    y_intersection = False
    if y_verts_colored[0] == y_verts_colored[3] or y_verts_colored[0] == y_verts_colored[2]:
        y_intersection = True

    s = 0

    if x_intersection and y_intersection:
        width = x_coords[2] - x_coords[1]
        height = y_coords[2] - y_coords[1]
        s = width * height    

    return s

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(filename)s | %(levelname)s: %(message)s',  # noqa: WPS323
    )
    assert task_1_1("111111111110000000000000000") == 11 # индексы начинаются с нулевого, поэтому 12-й элемент имеет 11-й номер
    assert task_1_1("11111111111") == -1 # Если во входящей последовательности нет нулей, возвращаем -1



    assert task_1_2(1, 1, 2, 2, 3, 3, 4, 4) == False
    assert task_1_2(0, 0, 2, 2, 1, 1, 3, 3) == 1
    assert task_1_2(0, 0, 4, 4, 1, 1, 3, 3) == 4

    logger.debug('Все тесты прошли успешно')