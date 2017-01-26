# Find the expected dollar value of each possible label value.

import collections
import itertools

from box_generator import LABELS, BOXES

# No builtin for this in Py2? Really? :(
def mean(arr):
    return sum(arr) / float(len(arr))

def compute_ev_table(k):
    outcomes = collections.defaultdict(list)
    for boxes in itertools.product(BOXES, repeat=k):
        selected_box = max(boxes, key=lambda box: box[0])
        label,actual = selected_box
        outcomes[label].append(actual)

    ev = {}
    for label in outcomes:
        ev[label] = mean(outcomes[label])
    return ev

print len(BOXES), 'boxes'
results_table = {}
ks = range(1, 3+1)
for k in ks:
    print 'COMPUTING', k
    results_table[k] = compute_ev_table(k)

print '==== RESULTS ===='
def print_row(label, values):
    print ' '.join('{:<10}'.format(v) for v in ([label] + values))
print_row('label', ['k={}'.format(k) for k in ks])
for label in LABELS:
    print_row(label, [results_table[k][label] for k in ks])
