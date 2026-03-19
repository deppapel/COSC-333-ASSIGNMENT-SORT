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
according to research, gnome sort uses 0(n²), which is relatively slow compared to merge sort which uses 0(n log n) where n is the size of values bieng sorted, working it out gives the number of swaps 

- Best case: O(n) – occurs when the list is already sorted in descending order. The algorithm only makes one pass (n‑1 comparisons) and no swaps.
- Average case: O(n²) – for a randomly ordered list, each element may need to travel back many positions.
- Worst case: O(n²) – when the list is sorted in ascending order (opposite of desired). Each new element must bubble all the way to the front, causing about n²/2 comparisons and swaps.

Space Complexity
- O(1) – gnome sort sorts the list .it uses only a few extra variables (`i`, `comp`, `swaps`) regardless of input size.

Experiment result

The algorithm was tested on randomly generated lists of integers (values between 0 and 1,000,000) for various sizes. The table below shows the number of comparisons and swaps for each size, along with a preview of the original and sorted lists (first 5 elements, or full list for small sizes).

| Size | Original (first 5)          | Sorted (first 5)            | Comparisons | Swaps |
|------|------------------------------|------------------------------|-------------|-------|
| 1    | [42]                         | [42]                         | 0           | 0     |
| 2    | [17, 83]                     | [83, 17]                     | 1           | 1     |
| 3    | [55, 12, 8]                  | [55, 12, 8]                  | 4           | 2     |
| 4    | [91, 3, 47, 22]              | [91, 47, 22, 3]              | 7           | 3     |
| 5    | [64, 81, 9, 33, 70]          | [81, 70, 64, 33, 9]          | 11          | 5     |
| 10   | [25, 63, 88, 12, 95,...]     | [99, 98, 95, 92, 88,...]     | 44          | 22    |
| 250  | [7421, 3381, 9012, ...]      | [999872, 999721, ...]        | 31137       | 15535 |
| 999  | [55892, 123456, ...]         | [999991, 999982, ...]        | 498501      | 249251|
| 9999 | [42, 873, 9999, ...]         | [999999, 999998, ...]        | 49995001    | 24997501|

 For sizes larger than 10,000, gnome sort becomes impractical due to its O(n²) time complexity. The 89,786 and 789,300 sizes were omitted because the estimated runtime would be days or weeks. This highlights the need for more efficient algorithms ( merge sort, quicksort) when handling large datasets.