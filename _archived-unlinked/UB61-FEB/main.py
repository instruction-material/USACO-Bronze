#adapted from USACO
N = int(input())
S = list(input())
if S.count("F") == N:
  S[0] = "E"
positions = [i for i in range(N) if S[i] != "F"]
ones = positions[0] + N - 1 - positions[-1]
mn, mx = 0, 0
for a, b in zip(positions, positions[1:]):
  mn += ((b - a) & 1) ^ (S[a] != S[b])
  mx += b - a - (S[a] != S[b])
ans = range(mn, ones + mx + 1, 1 + (ones == 0))
print(len(ans))
for level in ans:
  print(level)
