from sample_file import feasible, find_max_distance

if __name__=='__main__':
  test_cases=int(input())
  for i in range(test_cases):
    ar = list()
    str_n_cows = input()
    N=int(str_n_cows.split(" ")[0])
    cows = int(str_n_cows.split(" ")[1])
    for j in range(N):
      x = int(input())
      ar.append(x)
    ar.sort()
    print(find_max_distance(ar, N, cows))