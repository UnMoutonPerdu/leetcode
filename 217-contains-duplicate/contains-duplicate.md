# Linear time solution - One Liner

We can simply create a set using the `set` function on `nums` and compare the size of both the set and `nums`. Converting a list to a set and compute their length both take linear time. <u>The worst time complexity is so **O(n)**.</u>

# Linear time solution 

Another similar solution is to create an empty set and iterate through the list. If the element is not in the set, we add it, otherwise the program outputs `True`. If no duplicates have been found the program outputs `False`. The worst time complexity is also **O(n)** but the average time complexity is better.
