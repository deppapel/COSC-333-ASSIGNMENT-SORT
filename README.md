Name: Maxwel Ong'udi
Adm_no: EB3/67319/23
GNOME SORT(DESC)

How it works
gnome sort works by repeatedly stepping through the list/array index, comparing each element with the previous. If they are in correct order like for mine it checks the firsst two check if first is larger than the next, it moves foward. If not, it swaps them and takes one step back to check the new order. This continues until the list is done.

Step-by-step example list

sort [3,5,2,4,1] in descending order to get [5,4,3,2,1].
[i] is the current n.o in the array index, so while i < n which is the size of the array we continue to loop.
if i == 0 then move to the next index and continue, we dont compare here because its the first index and nothing to compare it with. after that we start comparing now.
if arr[i] <= arr[i-1] this checks if the value at current index is less than or equal to the previous one, if so then it moves to the next index (i += 1), otherwise swap the two values (arr[i], arr[i-1] = arr[i-1], arr[i]) then record the swap (swaps += 1). this goes on and on until everything is sorted in descending order. 
So from our example we start 1. i==0 -> move to i=1, array is [3,5,2,4,1]
2. compare index 1 and 0 (3,5) swap to (5,3). new array is [5,3,2,4,1] move to next index
3. compare index 2 and 1(3,2), correct order move to next index. Array remain same
4. compare index 3 and 2 (2,4), swap, now we have [5,3,4,2,1], one step back i.e index 2 and 1, compare, not in order, swap . New array [5,4,3,2,1], one step back to index 1 and 0, compare, correct. move to next until last comparison of index 4 and 3.

Time complexity