def add(a, b):
    print "adding %d + %d" % (a,b)
    return a + b

def substract(a,b):
    print "substracting %d - %d" % (a,b)
    return a - b

def multiply(a,b):
    print "multiplying %d * %d" % (a,b)
    return a * b

def divide(a,b):
    print "dividing %d / %d" % (a,b)
    return a / b

print "let's use the functions"

age = add(29,3)
height = substract(200,13)
weight = multiply(24,3)
iq = divide(132,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "now a big puzzle"

what = add(age, substract(height,multiply(weight, divide(iq,2))))

print "that is", what, "do it by hand"
