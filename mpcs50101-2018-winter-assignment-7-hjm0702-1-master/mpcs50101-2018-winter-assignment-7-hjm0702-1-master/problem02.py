'''
Q : Selecting the next best move in a game of tic tac toe.
A : O(n) or O(n^2)
Mathematically, if the game progresses, the possible spots we can choose decrease one by one.
So, the time will decrease in an exponential rate.
In reality, however, if an opponent selects a spot, I should choose one or two possible spots to win or not to lose the game.
In this sense, as the game progresses, the time to select will decrease in an exponential rate.


Q: Reading a book, where n is the number of pages.
A : O(n)
Given each page has similar numbers of words, the time to read a book will increase in a linear rate.


Q: Compiling a telephone or address book from a list of names/numbers.
A :O(n^2)
Since we have to find and match a name with a right phone number, the time to compile will increase in an exponential rate.


Q: Determining if a number is odd or even.
A : O(n)
Since we can judge it number by number, the time to determine will increase in a linear rate.


Q: Finding a word in the dictionary.
A : O(log n)
Even though we have many a dictionary with many pages,
we usually find a word by finding the first few letters referring to an index and a trial-and-error approach.
In that sense, I think, even if the number of pages increases,
the time to find a word will grow in a logarithmic rate.


Q: Checking if you have put all the items on your packing list in your suitcase.
A : O(n^2)
I think it depends on whether you put all the items in your bag or not.
Assuming I already put all items inside the bag,
it needs more time exponentially if you have more items since you have to get items outside the bag and check one by one.

'''
