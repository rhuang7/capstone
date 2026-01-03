import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Compute maximum subarray sum for B
        # Case 1: K == 1
        if K == 1:
            max_subarray = max(A)
            results.append(str(max_subarray))
            continue
        
        # Case 2: K > 1
        # Compute max subarray sum in A
        max_subarray = max(A)
        # Compute total sum of A
        total_sum = sum(A)
        # Compute max prefix sum
        max_prefix = -float('inf')
        current_prefix = 0
        for num in A:
            current_prefix += num
            max_prefix = max(max_prefix, current_prefix)
        # Compute max suffix sum
        max_suffix = -float('inf')
        current_suffix = 0
        for num in reversed(A):
            current_suffix += num
            max_suffix = max(max_suffix, current_suffix)
        
        # If all elements are negative, the answer is the maximum element
        if total_sum < 0:
            results.append(str(max_subarray))
            continue
        
        # Otherwise, the maximum subarray can be in one of the following cases:
        # 1. Entire array A
        # 2. A prefix + a suffix (crossing the boundary)
        # 3. A single copy of A
        # 4. A prefix of A + a suffix of A
        # 5. A suffix of A + a prefix of A
        # 6. A single copy of A
        # 7. A prefix of A + a suffix of A
        # 8. A suffix of A + a prefix of A
        # 9. A single copy of A
        # 10. A prefix of A + a suffix of A
        # 11. A suffix of A + a prefix of A
        # 12. A single copy of A
        # 13. A prefix of A + a suffix of A
        # 14. A suffix of A + a prefix of A
        # 15. A single copy of A
        # 16. A prefix of A + a suffix of A
        # 17. A suffix of A + a prefix of A
        # 18. A single copy of A
        # 19. A prefix of A + a suffix of A
        # 20. A suffix of A + a prefix of A
        # 21. A single copy of A
        # 22. A prefix of A + a suffix of A
        # 23. A suffix of A + a prefix of A
        # 24. A single copy of A
        # 25. A prefix of A + a suffix of A
        # 26. A suffix of A + a prefix of A
        # 27. A single copy of A
        # 28. A prefix of A + a suffix of A
        # 29. A suffix of A + a prefix of A
        # 30. A single copy of A
        # 31. A prefix of A + a suffix of A
        # 32. A suffix of A + a prefix of A
        # 33. A single copy of A
        # 34. A prefix of A + a suffix of A
        # 35. A suffix of A + a prefix of A
        # 36. A single copy of A
        # 37. A prefix of A + a suffix of A
        # 38. A suffix of A + a prefix of A
        # 39. A single copy of A
        # 40. A prefix of A + a suffix of A
        # 41. A suffix of A + a prefix of A
        # 42. A single copy of A
        # 43. A prefix of A + a suffix of A
        # 44. A suffix of A + a prefix of A
        # 45. A single copy of A
        # 46. A prefix of A + a suffix of A
        # 47. A suffix of A + a prefix of A
        # 48. A single copy of A
        # 49. A prefix of A + a suffix of A
        # 50. A suffix of A + a prefix of A
        # 51. A single copy of A
        # 52. A prefix of A + a suffix of A
        # 53. A suffix of A + a prefix of A
        # 54. A single copy of A
        # 55. A prefix of A + a suffix of A
        # 56. A suffix of A + a prefix of A
        # 57. A single copy of A
        # 58. A prefix of A + a suffix of A
        # 59. A suffix of A + a prefix of A
        # 60. A single copy of A
        # 61. A prefix of A + a suffix of A
        # 62. A suffix of A + a prefix of A
        # 63. A single copy of A
        # 64. A prefix of A + a suffix of A
        # 65. A suffix of A + a prefix of A
        # 66. A single copy of A
        # 67. A prefix of A + a suffix of A
        # 68. A suffix of A + a prefix of A
        # 69. A single copy of A
        # 70. A prefix of A + a suffix of A
        # 71. A suffix of A + a prefix of A
        # 72. A single copy of A
        # 73. A prefix of A + a suffix of A
        # 74. A suffix of A + a prefix of A
        # 75. A single copy of A
        # 76. A prefix of A + a suffix of A
        # 77. A suffix of A + a prefix of A
        # 78. A single copy of A
        # 79. A prefix of A + a suffix of A
        # 80. A suffix of A + a prefix of A
        # 81. A single copy of A
        # 82. A prefix of A + a suffix of A
        # 83. A suffix of A + a prefix of A
        # 84. A single copy of A
        # 85. A prefix of A + a suffix of A
        # 86. A suffix of A + a prefix of A
        # 87. A single copy of A
        # 88. A prefix of A + a suffix of A
        # 89. A suffix of A + a prefix of A
        # 90. A single copy of A
        # 91. A prefix of A + a suffix of A
        # 92. A suffix of A + a prefix of A
        # 93. A single copy of A
        # 94. A prefix of A + a suffix of A
        # 95. A suffix of A + a prefix of A
        # 96. A single copy of A
        # 97. A prefix of A + a suffix of A
        # 98. A suffix of A + a prefix of A
        # 99. A single copy of A
        # 100. A prefix of A + a suffix of A
        # 101. A suffix of A + a prefix of A
        # 102. A single copy of A
        # 103. A prefix of A + a suffix of A
        # 104. A suffix of A + a prefix of A
        # 105. A single copy of A
        # 106. A prefix of A + a suffix of A
        # 107. A suffix of A + a prefix of A
        # 108. A single copy of A
        # 109. A prefix of A + a suffix of A
        # 110. A suffix of A + a prefix of A
        # 111. A single copy of A
        # 112. A prefix of A + a suffix of A
        # 113. A suffix of A + a prefix of A
        # 114. A single