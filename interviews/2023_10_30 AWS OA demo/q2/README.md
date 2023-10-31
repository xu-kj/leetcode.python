# 2. Gifting Groups (example question)

At Audible, a subscriber can gift an audiobook from his/her library to any other non-subscriber to kick start their audiobook journey.
The first time subscriber can receive up to a maximum of N audiobooks from their friends/relatives.
When a non-subscriber receives an audiobook, we can infer that the two may be related.
Similarly, if the non-subscriber receives gifted books from two other subscribers, we can infer that all of them are related and the three of them form a **group**.
More formally, a **group** is composed of all of the people who know one another, whether directly or transitively.
Audible would like your help finding out the number of such distinct groups from the input data.

## Example

Consider the following input matrix `M`:

```
110
110
001
```

![example](./connected_groups_example.svg)

Every row corresponds to a subscriber and the value `M[i][j]` determines if `j` was gifted a book by `i`.
In the above example, user `0` has gifted a book to user `1` and so they are connected `[0][1]`, while person `2` has not received a book from anyone or gifted book to anyone.
Therefore, there are 2 **groups**.
`M[i][j] = 1` if `i == j`
(Each of the people is known to self)

Determine the number of groups represented in a matrix.

Note:
The method signatures may vary slightly depending on the requirements of the chosen language.
For example, C language will have an argument that represents the number of rows and columns in the matrix.
Also, Java will receive a list rather than an array.

## Function Description

Complete the function `countGroups` in the editor.

`countGroups` has the following parameter(s):

- `int related[n]`:
an array of strings of binary digits `related[i]` that represent connections of people

Returns:

- `int`:
an integer that represents the number of groups of people

## Constraints

- `1 <= n <= 300`
- `0 <= i < n`
- `|related| = n`
- Each `related[i]` contains a binary string of `n` zeros and ones.
`related` is a square matrix.
