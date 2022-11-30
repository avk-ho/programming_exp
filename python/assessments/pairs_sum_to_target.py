# https://www.programmingexpert.io/programming-fundamentals/assessment/5

# quick brute force solution, nested for loops
def pairs_sum_to_target(list1, list2, target):
    pairs = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] + list2[j] == target:
                pairs.append([i, j])

    return pairs


# if both lists were sorted, a faster solution is possible
def pairs_sum_to_target(list1, list2, target):
    pairs = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            pair_sum = list1[i] + list2[j]
            if pair_sum == target:
                pairs.append([i, j])
            elif pair_sum > target: # stopping the loop once the target can no longer be created
                break

    return pairs
