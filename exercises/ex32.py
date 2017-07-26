hairs = [ 'brown', 'blond', 'red' ]
eyes = ['brown', 'blue', 'green']
theCount = [1, 2, 3, 4, 5]

for number in theCount:
    print "this is the count %d" % number

for hair in hairs:
    print "hair colors %s" % hair

elements = []

for i in range(0,6):
    print "adding %r" % i
    elements.append(i)

for element in elements:
    print "the element is %r" % element
