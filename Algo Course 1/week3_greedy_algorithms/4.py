# Uses python3
import sys
import math
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    tem = []
    segments.sort(key = lambda x:x.end)
    #print(segments)
    temp=None
    for s in segments:
        if temp is None:
            temp = s.end
        if temp>=s.start and temp<=s.end:
            continue
        else:
            if temp not in tem: tem.append(temp)
            if s.start==s.end:
                temp=s.end
                if temp not in tem:tem.append(temp)
            temp = s.end
    if temp is None: temp = s.end
    if temp not in tem:tem.append(temp)
    tem.sort()
    return tem

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
