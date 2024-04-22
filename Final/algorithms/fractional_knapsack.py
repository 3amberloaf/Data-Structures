class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight
        
def fractionalKnapsack(total_weight, knapsack):
    
    knapsack.sort(key = lambda x: (x.profit/x.weight), reverse =True)
    
    total_profit = 0.0
    
    for item in knapsack:
        
        if item.weight <= total_weight:
            total_weight -= item.weight
            total_profit += item.profit
            
        else:
            total_profit += item.profit * total_weight / item.weight
            break
    
    return total_profit

if __name__ == "__main__":
    W = 20
    arr = [Item(92, 10), Item(100, 20), Item(120, 30)]
 
    # Function call
    max_val = fractionalKnapsack(W, arr)
    print(max_val)