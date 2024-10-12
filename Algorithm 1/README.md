
The whole point of my algorithm is to find a couple. A couple can be a [0,1,2,3] as long as the 0 and 1 is side by side that makes it a couple. This is another form of a coupe [1,0] or [3,2]. 

The algorithm essentially has to essentially see if there is a possibility of a couple. If there is and it’s incomplete. Let’s say [0,2,1,3], we would need one swap such as index 1 and index 2 would need to swap in order to complete a couple. 

We have a function named find and this function finds the parent or leader recursively. 

We have a union function that finds the root of a and b and essentially turns them into pairs. We do this in the fashion of making the parent[rootA] = rootB. This means the rootB will have the children as rootA. 

We then set n which is going to be the n = len(row) which is to find how many couples are going to be in the row. So if row is 6 there will be 3 couples. 

We then have a parent list which stores the root of each people

We then have a for loop which iterates over the couples in a 2step manner. Which then unions the couple by having a row[i] // 2, row[i+1] // 2. Let’s say row = [0,1,3,2,4,6]
What this means is we have a row[i] // 2. Which is 0 // 2 = 0 which then we do union which then finds the leader of 0. for the next one. Row[3+1] // 2 which is 4/2 is 2. So then we do union of that and we find the leader of 2. 

Lastly,

We have the count which counts all the non-coupled people. This is to later determine the swap that we “need” in order to make a couple. 

Then we return the n - count which will return the swaps needed. 
