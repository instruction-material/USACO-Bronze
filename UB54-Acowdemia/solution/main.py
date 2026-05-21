def h_index(papers):
  h = len(papers)
  while h > 0 and papers[h - 1] < h:
      h -= 1
  return h

def main():
  n, l = map(int, input().split())
  papers = list(map(int, input().split()))
  papers.sort(reverse=True)
  h = h_index(papers)
  if h != n:
      for j in range(h, max(-1, h - l), -1):
          papers[j] += 1
  papers.sort(reverse=True)
  print(h_index(papers))

if __name__ == "__main__":
  main()
