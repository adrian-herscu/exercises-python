def leaders(arr):
    leaders = []

    for i in range(len(arr)):
        potential_leader = arr[i]
        if i == len(arr) - 1:
            leaders.append(arr[i])
        else:
            max_follower = max(arr[i+1:])
            if potential_leader >= max_follower:
                leaders.append(potential_leader)

    return leaders
