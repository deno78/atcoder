t=int(input())
for _ in range(t):
    px, py, qx, qy, rx, ry, sx, sy = map(int, input().split())

    # |X-P|^2 = |X-Q|^2 から垂直二等分線を Ax + By + C = 0 で表す。
    a1 = 2 * (qx - px)
    b1 = 2 * (qy - py)
    c1 = px * px + py * py - qx * qx - qy * qy

    a2 = 2 * (sx - rx)
    b2 = 2 * (sy - ry)
    c2 = rx * rx + ry * ry - sx * sx - sy * sy

    det = a1 * b2 - a2 * b1
    if det != 0:
        print("Yes")
        continue

    # 平行な場合は同一直線かを判定。同一直線なら交点は無限個あるので Yes。
    same_line = (a1 * c2 - a2 * c1 == 0) and (b1 * c2 - b2 * c1 == 0)
    print("Yes" if same_line else "No")
    