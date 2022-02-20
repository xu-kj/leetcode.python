# 1353. Maximum Number of Events That Can Be Attended

leetcode [link][problem]

You are given an array of `events` where `events[i] = [startDayi, endDayi]`. Every event `i` starts at `startDay_i` and ends at `endDay_i`.

You can attend an event `i` at any day `d` where `startTime_i <= d <= endTime_i`. You can only attend one event at any time `d`.

Return the maximum number of events you can attend.

Example 1:

![e1](./assets/e1.png "example 1")

```
Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.
```

Example 2:

```
Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4
```

Constraints:

* `1 <= events.length <= 1e5`
* `events[i].length == 2`
* `1 <= startDay_i <= endDay_i <= 1e5`

[problem]: https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/
