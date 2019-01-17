# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    weight=0
    #print(values,weights)
    #sortedRes = sorted(zip(values,weights), key=lambda tup:tup[0]/tup[1], reverse=True)
    values,weights = (list(t) for t in zip(*sorted(zip(values,weights), key=lambda tup:tup[0]/tup[1], reverse=True)))
    #print(values,weights)
    #for i in range(len(weights)):
    #    print(values[i],weights[i])
    i=0
    for i in range(len(weights)):
        if capacity == 0:
            return value
        a=min(weights[i],capacity)
        value += (a*(values[i]/weights[i]))
        weights[i]=weights[i]-a
        capacity=capacity-a
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    #sys.stdout.write(data)
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    #print(data, n,capacity,values,weights)
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
