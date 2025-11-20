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

nums = [3, 1, 2, 7, 1]
segment_tree = [0] * (2 * len(nums))
build_tree(0, 0, len(nums) - 1)
print(segment_tree)    # [14, 6, 8, 4, 2, 7, 1, 3, 1, 0]

# Update the number at index 1 to the value = 2
update_tree(1, 2, 0, 0, len(nums) - 1)
print(segment_tree)    # [15, 7, 8, 5, 2, 7, 1, 3, 2, 0]
