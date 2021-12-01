# THE HOTEL REVIEW ANALYSIS

## Objective: Is to analyse the reviews from customer from different hotels to predict which hotel is best and gives full satisfaction to the customers.

## Procedure:
- Web Scraping the data from Hotel's in Goa and then Cleaning the data to use further process.
- Doing NLP pre-process to clean the data further and extracting the 'Common Nouns Tags'.
- Converting the Nouns in the form of Binary's.
- Implemnting the Binaries in 'Association Rule' to find the frequent itemset.
- After that deleting the duplicate values in that frequent itemset based on its support value (like resort | room , room | resort)
- Then, we creatively made two new approach such as 'Compactness Pruning' and 'Redundancy Pruning'.
- Compactness pruning helps us to find the strength of the feature,if the feature hotel and room between words contain less than 4 words then, we say it is 'compact'. if not we say 'not compact' and we won't consider the non caompact feature. Eg. (like We reached 'hotel' at midnight nice 'room' but bad smell inside the room).
- Redundancy pruning helps us to find the p-support of every single word ( we have single feature and two word feature for fututre process. For that we need to find this single word feature, how many times it reapeated alone and how many it reapeated along with other feature. Finally we subract the seperately repeated word with grouply repeated word and if the sperately repeated word has more count we consider that or otherwise we won't.
- Finally we check this with the 'Polarity' get the percentage of each word ( taken from the above all process and stored seperately and compare those words with two hotels ) in that which hotels has lot of word's with high precentage repeated. Then, we suggest the customer that hotel is best to Choose.
- We deployed the above work using steamlit and down below i provided the link and you can experience 'The Hotel Review Analysis'

## Link : https://hotelcompapp.herokuapp.com/
