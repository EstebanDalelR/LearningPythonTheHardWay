def cheese_and_crackers (cheese_count, boxes_of_crackers):
    print "you have %d cheeses" % cheese_count
    print "and %d boxes of crackers" % boxes_of_crackers

print "give them parameters"
cheese_and_crackers(23,21)

print "or use variables"
cheese_amount = 44
cracker_boxes = 19

cheese_and_crackers(cheese_amount,cracker_boxes)

print "or do math"
cheese_and_crackers(1+2,2*3)

print "or both"
cheese_and_crackers(cheese_amount*3,cracker_boxes+5052302302)

print "or get input"
cheese_amount = int(raw_input())
cracker_boxes = int(raw_input())

cheese_and_crackers(cheese_amount,cracker_boxes)
