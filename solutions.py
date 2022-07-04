import logging

logger = logging.getLogger(__name__)


def task_1_1(char_array):
    if '0' in char_array:
        i = char_array.index('0')
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

    def get_intersection_edge_len(min_1, max_1, min_2, max_2):
        vertexes = dict() 
        vertexes[min_1] = 1 
        vertexes[max_1] = 1 
        vertexes[min_2] = vertexes.get(min_2, 0) + 2
        vertexes[max_2] = vertexes.get(max_2, 0) + 2
        coords = list(vertexes.keys())
        coords.sort()
        verts_colored = [vertexes[x] for x in coords]
        points_num = len(verts_colored)
        if points_num == 2:
            length = coords[1] - coords[0]
        elif points_num == 3:
            if verts_colored[1] == 3:
                length = 0
            elif verts_colored[0] == 3:
                length = coords[1] - coords[0]
            elif verts_colored[2] == 3:
                length = coords[2] - coords[1]
        else:
            if verts_colored[0] == verts_colored[3] or verts_colored[0] == verts_colored[2]:
                length = coords[2] - coords[1]
            else:
                length = 0

        return length

    x_left_1, y_low_1, x_right_1, y_up_1 = get_minmax_corners(x1, y1, x2, y2)
    x_left_2, y_low_2, x_right_2, y_up_2 = get_minmax_corners(x3, y3, x4, y4)

    w = get_intersection_edge_len(x_left_1, x_right_1, x_left_2, x_right_2)
    h = get_intersection_edge_len(y_low_1, y_up_1, y_low_2, y_up_2)

    return w * h

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(filename)s | %(levelname)s: %(message)s',
    )
    assert task_1_1("111111111110000000000000000") == 11 # индексы начинаются с нулевого, поэтому 12-й элемент имеет 11-й номер
    assert task_1_1("11111111111") == -1 # Если во входящей последовательности нет нулей, возвращаем -1


    assert task_1_2(1, 1, 2, 2, 3, 3, 4, 4) == False
    assert task_1_2(0, 0, 2, 2, 1, 1, 3, 3) == 1
    assert task_1_2(0, 0, 4, 4, 1, 1, 3, 3) == 4
    assert task_1_2(0, 0, 2, 2, 0, 0, 2, 2) == 4
    assert task_1_2(0, 0, 2, 2, 0, 0, 5, 5) == 4
    assert task_1_2(-10, -10, 3, 3, 0, 0, 5, 5) == 9

    logger.debug('Все тесты прошли успешно')