# adapted from USACO


def solve():
  n, k = (int(x) for x in input().split())
  patches = ['.'] * n
  gCover = -1
  hCover = -1
  s = input()
  for idx, ch in enumerate(s):
    if ch == 'G' and gCover < idx:
      if idx + k >= len(patches):
        if patches[idx] != '.':
          patches[idx - 1] = 'G'
        else:
          patches[idx] = 'G'
        gCover = n
      else:
        patches[idx + k] = 'G'
        gCover = idx + 2 * k
    elif ch == 'H' and hCover < idx:
      if idx + k >= len(patches):
        if patches[idx] != '.':
          patches[idx - 1] = 'H'
        else:
          patches[idx] = 'H'
        hCover = idx + k
      else:
        patches[idx + k] = 'H'
        hCover = idx + 2 * k
  print(n - patches.count('.'))
  print("".join(patches))


t = int(input())
for _ in range(t):
  solve()
