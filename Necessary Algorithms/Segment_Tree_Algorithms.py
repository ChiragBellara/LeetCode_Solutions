"""
What is a Segment Tree? 
  -> It is a data structure that makes answering range specific questions easier
  -> allows efficient querying/updating of an interval/range

Segment Tree
  => Binary Tree
  => every node has 2 children except the leaf nodes
  => root represents the entire array; leaf represent individual elements; interal nodes represent intervals/segments
  => height = logN
  => Balanced Binary Tree
  => Number of Nodes = ~2*N (will be 2*N - 1 for odd length array and 2*N for even length)
  => best represented as an array where for node I the left child will be 2*I+1 and right child will be 2*I+2
"""

def build_tree(idx, left, right):
    # Base Case
    if left == right:
        segment_tree[idx] = nums[left]
        return

    mid = (left + right) // 2
    build_tree(2*idx + 1, left, mid)
    build_tree(2*idx + 2, mid + 1, right)

    segment_tree[idx] = segment_tree[2 * idx + 1] + segment_tree[2 * idx + 2]
    return

def update_tree(idx_to_update, new_value, idx, left, right):
    # Base Case
    if left == right == idx_to_update:
        segment_tree[idx] = new_value
        return

    mid = (left + right) // 2
    if idx_to_update <= mid:
        update_tree(idx_to_update, new_value, 2*idx + 1, left, mid)
    else:
        update_tree(idx_to_update, new_value, 2*idx + 2, mid + 1, right)
    
    segment_tree[idx] = segment_tree[2 * idx + 1] + segment_tree[2 * idx + 2]
    return

def query(start, end, left, right, idx):
    # If current segment interval is out of bounds of the required
    # [start, end] interval.
    if end < left or start > right:
        return 0
    
    # If current segment interval is a subset of the required
    # [start, end] interval.
    if left >= start and right <= end:
        return segment_tree[idx]
    
    # Break the current segment down to further fine-tune the intervals
    mid = (left + right) // 2
    return query(start, end, left, mid, 2*idx + 1) + query(start, end, mid + 1, right, 2*idx + 2)

nums = [3, 1, 2, 7, 2, 1, 2, 3]
segment_tree = [0] * (2 * len(nums))
build_tree(idx = 0, left = 0, right = len(nums) - 1)
print(segment_tree)    # [14, 6, 8, 4, 2, 7, 1, 3, 1, 0]

# Update the number at index 1 to the value = 2
update_tree(idx_to_update = 1, new_value = 2, idx = 0, left = 0, right = len(nums) - 1)
print(segment_tree)    # [15, 7, 8, 5, 2, 7, 1, 3, 2, 0]

# Query the segment tree to find the sum of all elements in the range [start, end]
outcome = query(start = 2, end = 6, left = 0, right = len(nums) - 1, idx = 0)
print(outcome)  # 15
