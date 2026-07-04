# adapted from USACO


def solve():
  n, k = (int(x) for x in input().split())
  patches = ['.'] * n
  g_cover = -1
  h_cover = -1
  s = input()
  for idx, ch in enumerate(s):
    if ch == 'G' and g_cover < idx:
      if idx + k >= len(patches):
        if patches[idx] != '.':
          patches[idx - 1] = 'G'
        else:
          patches[idx] = 'G'
        g_cover = n
      else:
        patches[idx + k] = 'G'
        g_cover = idx + 2 * k
    elif ch == 'H' and h_cover < idx:
      if idx + k >= len(patches):
        if patches[idx] != '.':
          patches[idx - 1] = 'H'
        else:
          patches[idx] = 'H'
        h_cover = idx + k
      else:
        patches[idx + k] = 'H'
        h_cover = idx + 2 * k
  print(n - patches.count('.'))
  print("".join(patches))


t = int(input())
for _ in range(t):
  solve()
