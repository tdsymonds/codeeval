for i in xrange(1,13):
    for j in xrange(1,13):
        result = str(i*j)
        print '%s%s' % ((3-len(result))*' ', result), 
    print