[**challenge**](https://www.codewars.com/kata/5d41d87bb29859002690d4fd) | [**My solution**](/python/6kyu/Counting%20Digits.py)

## Challenge explanation

This kata is inspired by the British gameshow Only Connect, specifically the clue that stumped the contestants seen here

Your goal is to write a function that receives an integer and then repeatedly counts the occurrences of each digit (the number of rounds will be given as a positive integer).

Note
The order is important, the result should list the digits in the order they first appeared (from left to right).

Examples
Simple 1 round example:
```
num = 141, rounds = 1
ROUND 1: 141 --> [21, 14]
```
# Reading left to right, 1 was encountered first (two 1), then 4 (one 4)
So the solution is [21, 14]

Simple 1 round example with a larger number:
```
num = 1221313, rounds = 1
ROUND 1: 1221313 --> [31, 22, 23]
```
# Reading left to right, 1 was encountered first, then 2, then 3
So the solution is [31, 22, 23]

More complex 3 round example:
```
num = 5, rounds = 3
ROUND 1: 5 --> [15]
ROUND 2: 15 --> [11, 15]
ROUND 3: 1115 --> [31, 15]
So the solution is [31, 15]
```




### Explanation of the Solution

The function `count_digits(num, rounds)` repeatedly processes a number by counting how many times each digit appears, for a given number of rounds.

For each round:

1. The current number is converted to a string so its digits can be processed from **left to right**.
2. For every digit encountered, the function:

   * Counts how many times that digit appears in the whole number.
   * Combines the count and the digit into a string (e.g. `"2" + "1" → "21"`).
3. To preserve the required order, each digit is only processed **the first time it appears**, which is ensured by checking whether the generated value is already in the result list.
4. All generated count–digit pairs are concatenated to form the number for the next round.

After completing all rounds, the final result is converted into a list of integers and returned.

This approach guarantees:

* Correct counting of digit occurrences
* Preservation of the original left-to-right digit order
* Proper transformation across multiple rounds

## Enjoyed the Code?

If you found this project helpful or interesting, please consider giving it a 
star on GitHub! ⭐

Your support motivates me to continue working on and improving this project.

[Give a Star](https://github.com/Scigeek-saadati/codewars-problems) 

Thank you!