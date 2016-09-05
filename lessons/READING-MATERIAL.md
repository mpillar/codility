# Lessons reading material

This doc summarizes the reading material provided in
[Codility's lessons section](https://codility.com/programmers/lessons). The pdfs there are quite
good. I encourage you to give them a read!

## Counting

If we know all elements in an array are in the set `{0, 1, ..., m}` then we can use a counting array
of size `m+1` to count the occurrences of each element in the original array.

This is useful, for example, when trying to solve the multi-array swap problem in `O(n+m)` time.

N.B. we could also use a hash table to solve this problem. This would give us the same runtime but
the overhead would be higher for small values of `m`.

## Prefix sums

Prefix sums allow you to calculate the sum of a given slice of an array.

## Sorting

Sorting algorithms: selection, counting, merge, quick. From `O(n^2)` to `O(n log n)`.

## Stacks and queues

1. Stack: supports insertion and removal at the top only.
2. Queue: Support insertion at the tail and removal at the head only.

## Leader

A leader is an element in an array that occurs more than `n/2` times where `n` is the length of the
array. The leader can be computed using `O(n)` complexity using an algorithm that makes use of a
neat variation on a stack.

## Maximum slice problem

Also known as the maximum continuous sub-sequenece problem. We can solve this problem in `O(n)` time
by noting that as long as the value of the previous slice is greater than zero, we should continue
to add to it.

## Prime numbers
TODO

## Sieve
TODO

##  GCD
TODO

## Fibonacci
TODO

## Binary search
TODO

## Caterpillar method
TODO

## Greedy algorithm
TODO

## Dynamic programming
TODO
