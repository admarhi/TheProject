from operator import itemgetter
  
# Initialize dictionary
test_dict = {'gfg' : 1, 'is' : 4, 'best' : 6, 'for' : 7, 'geeks' : 3 }
  
# Initialize K 
K = 2
  
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
  
# Smallest K values in Dictionary
# Using sorted() + itemgetter() + items()
res = dict(sorted(test_dict.items(), key = itemgetter(1))[:K])
  
# printing result
print("The minimum K value pairs are " + str(res))