# algo
# use binary search to find the max feasible distance. use the search space   1.....ar[-1]-ar[0]
#
def feasible(ar, N, dis, no_of_cows):
    j = 1
    count_cows = 1
    last_cow_loc = 0  # stores the j of last cow
    while j < N:
        if ar[j] - ar[last_cow_loc] >= dis:
            last_cow_loc = j
            count_cows += 1
        j += 1
    if count_cows >=no_of_cows:
        return True
    else:
        return False


def find_max_distance(ar, N, no_of_cows):
    st = 1
    end = ar[-1] -ar[0]
    ans = 1
    while  st <= end :
        mid = st + (end - st)// 2
        if feasible(ar, N, mid,no_of_cows):
            if mid>ans:
                ans = mid
            st = mid+1
        else:
            end = mid -1
    return ans


