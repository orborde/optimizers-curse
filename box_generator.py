# Boxes have labels from 0 to 20. We want the label to accurately
# report the expected value of the box.
#
# Turns out, this is actually kinda tricky.

LABELS = range(0, 20+1)
ERROR_MAX = 5

# For each label, generate boxes of the same error size in pairs (one
# high, and one low) to keep the EV for that label symmetric.
BOXES = []
for l in LABELS:
    # Generate a zero-error box.
    BOXES.append( (l, l) )

    # Generate error-offset pairs.
    for e in xrange(1, ERROR_MAX + 1):
        # You can't put negative dollars in the box, though.
        if e > l:
            continue

        BOXES.append( (l, l - e) )
        BOXES.append( (l, l + e) )

def mean(arr):
    return sum(arr) / float(len(arr))

if __name__ == '__main__':
    # Make sure that the EV actually matches the label for all boxes.
    import collections
    outcomes = collections.defaultdict(list)
    for label, actual in BOXES:
        outcomes[label].append(actual)

    for label in sorted(outcomes.keys()):
        values = outcomes[label]
        assert label == mean(values)

