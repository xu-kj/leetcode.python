# Q1

Given an array of integers representing the object moving in a row.

For each object,
the absolute value represents its size,
and the sign represents its direction
(positive meaning right, negative meaning left).
Each object moves at the same speed.
Find out the state of the objects after all collisions.
If two objects meet,
the smaller one will explode.
If both are the same size,
both will explode.
Two objects moving in the same direction will never meet.

## Examples

### 1

```
Input: objects = [5,10,-5]
Output: [5,10]
```

Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

### 2

```
Input: objects = [8,-8]
Output: []
```

Explanation: The 8 and -8 collide exploding each other.

### 2.1

```
Input: objects = [-8,8]
Output: [-8,8]
```

Explanation: The -8 and 8 never collide since they move in opposite directions.

### 3

```
Input: objects = [10,2,-5]
Output: [10]
```

Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
