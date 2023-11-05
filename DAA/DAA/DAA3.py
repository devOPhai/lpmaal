class ItemValue:
    """Item Value DataClass"""

    def __init__(self, wt_, val_, ind_):
        self.wt = wt_
        self.val = val_
        self.ind = ind_
        self.cost = val_ / wt_  # Calculate the cost (value-to-weight ratio)

    def __lt__(self, other):
        return self.cost > other.cost  # Sort items by cost in descending order

def fractionalKnapSack(wt, val, capacity):
    """Function to get the maximum value"""
    iVal = [ItemValue(wt[i], val[i], i) for i in range(len(wt))]

    # Sort items by cost (value-to-weight ratio) in descending order
    iVal.sort()

    totalValue = 0  # Initialize the total value to zero

    for item in iVal:
        curWt = item.wt
        curVal = item.val

        if capacity - curWt >= 0:
            # Take the whole item if there's enough capacity
            capacity -= curWt
            totalValue += curVal
        else:
            # Otherwise, take a fraction of the item
            fraction = capacity / curWt
            totalValue += curVal * fraction
            break

    return totalValue

if __name__ == "__main__":
    wt = [10, 40, 20, 30]
    val = [60, 40, 100, 120]
    capacity = 50

    # Function call
    maxValue = fractionalKnapSack(wt, val, capacity)
    print("Maximum value in Knapsack =", maxValue)
