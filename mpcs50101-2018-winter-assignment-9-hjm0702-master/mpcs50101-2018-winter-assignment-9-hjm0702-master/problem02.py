'''Map Function : O(n) the function executes mathematical operations item by item in the list.
   List Comprehension : O(n) the function executes mathematical operations item by item in the list.

   I conducted several benchmark experiments by generating 1M random integers.
Based on the experiements, Map Funcion is slightly faster than List comprehension.
Please find the attached PNG file for the detailed numbers.  
'''

import random
import time

# cel = [random.randint(1,1000000) for i in range(1000000)]
cel = [random.randint(1,1000000) for i in range(100)]

'''Map Function'''
def temperature1(cel):
    try :
        # cel = (float(fah)-32)/1.8
        fah = float(cel)*1.8+32
        return fah
    except EOFError :
        return "Please input something"
    except ValueError :
        return False

start_map = time.time()
fah = map(temperature1, cel)
end_map = time.time()

'''List comprehension'''

def temperature2(cel):
    try :
        # cel = (float(fah)-32)/1.8
        fah = float(cel)*1.8+32
        return fah
    except EOFError :
        return "Please input something"
    except ValueError :
        return False
start_lc = time.time()
fah1 = [temperature2(i) for i in cel]
end_lc = time.time()

if __name__ == "__main__":

    # print cel
    print "Map Function:", fah, end_map-start_map
    print "---------------------------------------"
    print "List Comprehension:", fah1, end_lc-start_lc
