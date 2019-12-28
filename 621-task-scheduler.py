"""
Problem Link: https://leetcode.com/problems/task-scheduler/

Given a char array representing tasks CPU need to do. It contains capital letters A to Z where 
different letters represent different tasks. Tasks could be done without original order. 
Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.
However, there is a non-negative cooling interval n that means between two same tasks, 
there must be at least n intervals that CPU are doing different tasks or just be idle.
You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
 
Note:
The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
      d = {}
      max_val = 0
      for task in tasks:
        d[task] = d.get(task,0) + 1
        if d[task] > max_val:
          max_val = d[task]
      max_val -= 1
      idle_slots = max_val * (n+1)
      for k,v in d.items():
        idle_slots -= min(max_val, v)
      print(max_val, idle_slots)
      return idle_slots + len(tasks) if idle_slots > 0 else len(tasks)
        
from collections import Counter
class Solution1:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks).values()
        M = max(task_counts)
        m_count = 0
        for i in task_counts:
          if i == M:
            m_count += 1
        return max(len(tasks), (M - 1) * (n + 1) + m_count)
