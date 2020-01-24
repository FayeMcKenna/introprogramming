
#Question1
#Read the tsv file
#save the contents in a nested list of rows (each row is itself a list).
#use map function to create a dictionary of each row iteration
#dictionary entries should be {‘date’: date_from_row, ‘taxon’: taxon_from_row, ‘mcp’: most_common_protein
#create list of dictionaries
#Filter the list of  dictionaries so that any rows with TRYP or BOVIN in the most common protein string are removed.
#Use a ‘reduce’ function to reduce the filtered list of dictionaries down to a single dictionary containing counts
# for each taxon grouped by year. Finally print the most common taxon for each year and how many times it appeared that year.

fh = open('/Users/fayemckenna/Desktop/Sackler/Introduction to Programming/test.tsv' , 'r')
text = fh.readlines() # open text file

data = [] #create data nested list
for row in text:
    items = row.rstrip('\r\n').split('\t')   # strip new-line characters and split on column delimiter
    items = [item.strip() for item in items]  # strip extra whitespace off data items
    data.append(items)
del data[0]
#Data =[[‘file_name’,’fjdkasjfdl’,’ahfjhds’][‘date’,’00400’,’20492’]]
from datetime import datetime
def lister(l): #create a function to make a dict of each row
    dict1 = {} #dictionary
    dict1['date']= (l[1][0:4])
    dict1['mcp'] = l[6]
    dict1['taxon'] = l[22].split(',')
    return dict1

list(map(lister,data))
changed=list(map(lister,data))


#filter list of  dictionaries so that any rows with TRYP or BOVIN in the most common protein string are removed.
#filtered_list = [x for x in dictionary_list if x.attribute != 'TRYP' or 'BOVIN']
filtered_list= list(filter(lambda x: 'TRYP' not in x['mcp'] and 'BOVIN' not in x['mcp'], changed))


#Use a ‘reduce’ function to reduce the filtered list of dictionaries down to a single dictionary containing counts for each taxon grouped by year. Finally print the most common taxon for each year and how many times it appeared that year.
#step1: need to regroup based on date
#step 2: add up taxon in that date
#need to do this for each dictionary in list maybe larger loop?


from functools import reduce


text = filtered_list
words = []
def reduce_to_counts(counts_of_taxon, line):
    year=line['date']
    counts_of_taxon[year] = counts_of_taxon.get(year,{})
    for t in line['taxon']:
        counts_of_taxon[year][t]=counts_of_taxon[year].get(t,0) +1
    return counts_of_taxon
counts_taxon = reduce(reduce_to_counts, filtered_list, {})


for year in counts_taxon.keys():
    print(max(counts_taxon[year], key=lambda key:counts_taxon[year][key])+ ' '+ year + ' ' + str(max(counts_taxon[year].values())))
#print(max(counts_taxon.items(), key=lambda x: x[1]))



#Question2
#Write a function to reverse (transform) the user-item-rating dictionary to an item-user-rating dictionary, i.e. a dictionary where the top-level keys are individual items, and the value for each item is the corresponding user-rating dictionary
#Write a function that can take as input two ratings’ dictionaries, and compute/return some measure of their dis-similarity
#compute the dis-similarity as: Average of Absolute Difference of ratings for common keys.
#Use the above function to compute the dis-similarity of each pair of users in the user-item-rating dictionary, using their item-ratings. Likewise, compute the dis-similarity of each pair of items in the item-user-rating dictionary, using their user-ratings. Print the most similar (least dissimilar) user-pair(s) and the most similar (least dissimilar) item-pair(s) in the data provided.

user_item_rating = {
    'user1': {'item1': 2.5, 'item2': 3.5, 'item3': 3.0,
              'item4': 3.5, 'item5': 2.5, 'item6': 3.0},
    'user2': {'item1': 3.0, 'item2': 3.5, 'item3': 1.5,
              'item4': 5.0, 'item5': 3.5, 'item6': 3.0},
    'user3': {'item1': 2.5, 'item2': 3.0, 'item4': 3.5,
              'item6': 4.0},
    'user4': {'item2': 3.5, 'item3': 3.0, 'item4': 4.0,
              'item5': 2.5, 'item6': 4.5},
    'user5': {'item1': 3.0, 'item2': 4.0, 'item3': 2.0,
              'item4': 3.0, 'item5': 2.0, 'item6': 3.0},
    'user6': {'item1': 3.0, 'item2': 4.0, 'item4': 5.0,
              'item5': 3.5, 'item6': 3.0},
    'user7': {'item2': 4.5, 'item4': 4.0, 'item5': 1.0}
}
#Write a function to reverse (transform) the user-item-rating dictionary to an item-user-rating dictionary, i.e. a dictionary where the top-level keys are individual items, and the value for each item is the corresponding user-rating dictionary

from collections import defaultdict
import pprint

def switch(user_item_rating):
    flipped = defaultdict(dict)
    for key, val in user_item_rating.items():
        for subkey, subval in val.items():
            flipped[subkey][key] = subval
    return flipped
switchlist=(switch(user_item_rating))
pprint.pprint(dict(switch(user_item_rating)))


# Write a function that compares user1 and user2 each common item by subtracting taking the asbolute value and dividing by 2

def compare(dict1, dict2):
    newlist = []  # create list to save rating
    for k in dict1:  # iterate over keys in dict1 #how to make it an integer?
        if k in dict2:  # if that key is also in dict2
            newlist.append((abs((dict1[k]) - (dict2[k])))) # # then subtract and absolute value and divide by number
    return sum(newlist)/len(newlist)  # return value

compare(user_item_rating['user1'], user_item_rating['user2'])  # call function

# Use the above function to compute the dis-similarity of each pair of users in the user-item-rating
less_count = None
less_word = None
more_compare=[]
listuser= user_item_rating.keys()
for o in listuser:
    for p in listuser:
        if p!=o:
           diff=compare(user_item_rating[p], user_item_rating[o])
           if less_count is None or diff < less_count:
                less_count=diff
                less_word= [p,o]
print('most similar user-pairs: ', less_count, less_word)

# Use the above function to compute the dis-similarity of each pair of users in the user-item-rating
less_count = None
less_word = None
more_compare=[]
listuser= switchlist.keys()
for o in listuser:
    for p in listuser:
        if p!=o:
           diff=compare(switchlist[p], switchlist[o])
           if less_count is None or diff < less_count:
                less_count=diff
                less_word= [p,o]
print('most similar item-pairs: ',less_count, less_word)