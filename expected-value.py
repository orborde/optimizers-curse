# Find the expected dollar value of each possible label value.

import collections
import itertools

# Maps "number on the box" to "actual dollars in the box"
outcomes = collections.defaultdict(list)

for dollars,fiction in itertools.product(range(1,10+1), range(-4, 5, 1)):
    label = dollars + fiction
    outcomes[label].append(dollars)

def mean(arr):
    return sum(arr) / float(len(arr))

for label in sorted(outcomes.keys()):
    values = outcomes[label]
    print label, mean(values)

