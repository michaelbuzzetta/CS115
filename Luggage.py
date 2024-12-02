def subset(capacity, items):
    if capacity <= 0 or items ==[]:
        return 0
    elif items[0]>capacity:
        return subset(capacity, items[1:])
    else:
        use_it=items[0]+subset(capacity-items[0],items[1:])
        lose_it=subset(capacity,items[1:])
        return max(use_it,lose_it)
