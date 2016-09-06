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

We can count the number of divisors of a number `n` by checking from two to the square root of `n`
(this is thanks to the useful property of the symmetric divisor).

## Sieve

The sieve of Eratosthenes is a simple and popular technique for finding all the prime numbers from
2 to a given number `n`. The algorithm takes is name from the process of sieving.

The process works as follows. We start with the set of number from 2 to `n`. At each step we choose
the smallest number in the set and remove all its multiples. We only have to do this up to the
square root of `n`. This runs in `O(n log log n)` time (the proof here is interesting).

Using the sieve of Eratosthenes, we can quickly factor numbers. If we know that one of the prime
factors of `x` is `p`, then all the prime factors of `x` are `p` plus the decomposition of `x/p`.
This runs in `O(log x)` time, when we are given the pre-computed sieve.

##  GCD

The Euclidean algorithm solves the problem of calculating the greatest common divisor (gcd) between
two positive integers. There are many implementations of the Euclidean algorithm, varying in
complexity and efficiency.

Knowing the GCD, we can also quickly compute the LCM (lowest common multiple).

## Fibonacci

The Fibonacci sequence is defined recursively by summing the last two elements of the sequence and
starting with 0 and 1.

There are advanced ways to compute Fibonacci numbers very quickly.

## Binary search

Binary search is the search of a sorted array. It runs in `O(log n)` time.

## Greedy algorithm

Greedy programming is a method by which a solution is determined based on making the locally optimal
choice at any given moment. Depending on the problem, a greedy solution may or may not be the best
approach.

## Dynamic programming

Dynamic programming is a method by which a solution is determined based on solving successively
similar but smaller problems.