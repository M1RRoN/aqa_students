from dataclasses import dataclass


@dataclass
class GroupStatistics:
    avgMark: float
    minMark: float
    maxMark: float

marks = [3.0, 4.0, 5.0, 2.5, 4.5, 3.5]

avg_mark = sum(marks) / len(marks)
max_mark = max(marks)
min_mark = min(marks)

statistics = GroupStatistics(avgMark=avg_mark, maxMark=max_mark, minMark=min_mark)

print(statistics)