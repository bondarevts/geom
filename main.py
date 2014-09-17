#!/usr/bin/env python3
# -*- coding: utf8 -*-

from sys import stdin


class Point:
    def __init__(self, x, y, w=1):
        self.x = x
        self.y = y
        self.w = w

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ',' + str(self.w) + ')'


def parse_coords(line):
    return Point(*map(int, line.strip()[1:-1].split(',')))


def point_det(p1, p2, p3):
    return determinant([
        [p1.x, p1.y, p1.w],
        [p2.x, p2.y, p2.w],
        [p3.x, p3.y, p3.w]
    ])


def determinant(m3x3):
    return (
        m3x3[0][0] * m3x3[1][1] * m3x3[2][2] +
        m3x3[0][1] * m3x3[1][2] * m3x3[2][0] +
        m3x3[0][2] * m3x3[1][0] * m3x3[2][1]
    ) - (
        m3x3[0][2] * m3x3[1][1] * m3x3[2][0] +
        m3x3[0][1] * m3x3[1][0] * m3x3[2][2] +
        m3x3[0][0] * m3x3[1][2] * m3x3[2][1]
    )


def crossed(s1, s2, p1, p2):
    return point_det(p1, p2, s1) * point_det(p1, p2, s2) < 0 and \
        point_det(s1, s2, p1) * point_det(s1, s2, p2) < 0


def on_line(p1, p2, s):
    # horizontal ray to left
    return not point_det(p1, p2, s) and s.x <= p1.x


def is_inner_point(poly, point):
    counter = 0
    left = Point(-1, 0, 0)
    i = 0
    poly_length = len(poly)
    while i < poly_length:
        start, end = poly[i], poly[i + 1 - poly_length]
        if on_line(point, left, end):
            side = point_det(point, left, start)
            i += 1
            while on_line(point, left, poly[i + 1 - poly_length]):
                i += 1
            if side * point_det(point, left, poly[i + 1 - poly_length]) < 0:
                counter += 1
        elif crossed(start, end, point, left):
            counter += 1
        i += 1
    return counter % 2


def main():
    poly_length = int(stdin.readline())
    poly = []
    for i in range(poly_length):
        poly.append(parse_coords(stdin.readline()))
    points_count = int(stdin.readline())
    for i in range(points_count):
        point = parse_coords(stdin.readline())
        print("yes" if is_inner_point(poly, point) else "no")


if __name__ == '__main__':
    main()
