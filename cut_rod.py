def cutRod(price, n):
    val = [0 for x in range(n+1)]
    val[0] = 0
 
    # Build the table val[] in bottom up manner and return
    # the last entry from the table
    for i in range(1, n+1):
        max_val = -99;
        for j in range(i):
             max_val = max(max_val, price[j] + val[i-j-1])
	     print "j" ,j, val
        val[i] = max_val
	print "i", i,val
 
    return val[n]

arr = [3,5]
size = len(arr)
print("Maximum Obtainable Value is " + str(cutRod(arr, size)))
