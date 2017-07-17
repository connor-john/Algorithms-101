# Quick Sort

Quick sort is an algorithm that uses the divide and conquer principle. </br>
#### The Pivot
 - We start quick sort by choosing a pivot, there are many ways to decide a pivot in quick sort, in the code provided I have simply  chosen the pivot at random. </br> 
- The role of the pivot is to split the list, meaning by the end of the algorithm everything smaller 
than the pivot value will be on its left, before it, and everything greater than the pivots value will be on its right, after it. </br>
</br>
We then use what is known as partitioning.</br>
</br>


#### Partitioning


1. Initialising:
   1. start with pointers, which we wil call, L and R at the head and at the end of the list, respectively. </br>
   2. We then swap the pivot with the head of the list.
2. Iteration: while L < R, do:
   1. Decrement R, until it meets an element less than or equal to the value of the pivot.
   2. Increment L, until it meets an element greater than or equal to the value of the pivot.
   3. Swap the elements pointed by L and R.
3. Once L = R swap the pivot with the elemnt pointed by L.
</br>
After partitioning is complete the list is now sorted.
</br>
</br>

### Time complexity

#### The Worst Case

//working on
//finding suitable math packages


