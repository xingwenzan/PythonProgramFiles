# 最小步数模型 魔板 https://www.acwing.com/problem/content/1109/

from collections import deque

st, ed = "12345678", "".join(input().split())
# A 操作等价于是翻转原字符串，B、C 操作可以在草稿纸上同理推出
# 无需转数组，可减少代码量
C = lambda s: s[0] + s[6] + s[1] + s[3:5] + s[2] + s[5] + s[7]
B = lambda s: s[3] + s[:3] + s[5:] + s[4]
A = lambda s: s[::-1]
pre = {}


def bfs():
    q = deque([st])
    pre[st] = ("", "")
    while q:
        cur = q.popleft()
        if cur == ed:
            s = pre[ed][1]
            return str(len(s)), s
        # 「操作名」 与 「操作后得到的字符串」 对应
        for op, nxt in zip("ABC", (A(cur), B(cur), C(cur))):
            if nxt not in pre:
                pre[nxt] = (cur, pre[cur][1] + op)  # cur 可不记录，但要注意把前面的都改了
                q.append(nxt)


# 获得到达终点状态的操作次数以及路径，有空字符串的用例，不加 strip 会格式错误
print("\n".join(bfs()).strip())
