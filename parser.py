
def parser(query):
    
    query = " " + query
    #print "I am the length of query:", len(query)

    tokens = []
    index = 0

#######################################################################
    while index <= len(query):
        print "index in while loop", index, len(query)
        if query[index] == " " and query[index + 1] != chr(39):
            start = index + 1

            j = start
            while query[j] != " " and j < len(query):
                print query[j]
                #print " I am j2 in the space loop:", j
                j += 1
                #print "i am new j", j

            tokens.append(query[start:j])
            print tokens

            index = j
            print "i am index in j2 at loop-end", index

        elif query[index + 1] == chr(39):
            start = index + 2

            j = start
            #print "start:", j
            
            while query[j] != chr(39) and j < len(query):
                print " I am j1 in the quote loop:", j
                j+=1
                
            tokens.append(query[start:j])
            print tokens

            index = j + 1
########################################################################
    return tokens


print parser("John said 'Howdy Doogie' on a house")