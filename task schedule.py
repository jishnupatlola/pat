class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count=Counter(tasks)
        max_freq=max(task_count.values())
        max_freq_task=sum(1 for i in task_count.values() if i==max_freq)
        res=(max_freq-1)*(n+1)+max_freq_task
        return max(res,len(tasks))
