# 八数码 https://www.acwing.com/problem/content/181/

from heapq import *


def main():
    st = "".join(input().split())
    seq = st.replace('x', "")
    g = lambda x: int(x) - 1
    # 估价函数，为每个数字当前位置与其终点位置的曼哈顿距离之和
    f = lambda s: sum(abs(i // 3 - g(ch) // 3) + abs(i % 3 - g(ch) % 3) for i, ch in enumerate(s) if ch != 'x')
    dir_x, dir_y = (-1, 1, 0, 0), (0, 0, -1, 1)
    ed, dirs = "12345678x", "udlr"

    # Astar 引入估价函数，借用优先队列完成搜索
    def Astar_bfs(st):
        pq, path, dist = [(f(st), st)], {st: ""}, {st: 0}
        while pq:
            _, cur = heappop(pq)
            # 获取当前状态的路径和步数
            p, d = path[cur], dist[cur]
            if cur == ed:
                return p
            cur = list(cur)
            x, y = divmod(cur.index('x'), 3)
            # 下面的搜索过程与朴素做法几乎一致，区别在于每个点可以搜索多次
            for op, dx, dy in zip(dirs, dir_x, dir_y):
                nx, ny = x + dx, y + dy
                if 0 <= nx < 3 and 0 <= ny < 3:
                    cur[x * 3 + y], cur[nx * 3 + ny] = cur[nx * 3 + ny], cur[x * 3 + y]
                    nxt = "".join(cur)
                    # 从 cur 走到 nxt 的距离比之前更小了，刷新记录！
                    if dist.get(nxt, 1e9) > d + 1:
                        path[nxt] = p + op
                        dist[nxt] = d + 1
                        # 入队 (实际距离 + 估计距离，下个状态)
                        heappush(pq, (dist[nxt] + f(nxt), nxt))
                    cur[x * 3 + y], cur[nx * 3 + ny] = cur[nx * 3 + ny], cur[x * 3 + y]
        return ""

    # 计算初始序列逆序对个数，存在偶数个逆序对时才有解
    cnt = sum(int(seq[i] > seq[j]) for i in range(8) for j in range(i + 1, 8))
    print("unsolvable" if cnt & 1 else Astar_bfs(st))


if __name__ == "__main__":
    main()
