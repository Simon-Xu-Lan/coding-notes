# 去除重复元素
- 给一个整数数组，去除重复的元素。
- 你应该做这些事
1. 在原数组上操作
2. 将去除重复之后的元素放在数组的开头
3. 返回去除重复元素之后的元素个数
```java
// 建立一个指针，指针指向目前位置不同的数的末尾，如果当前元素与末尾不同，则加入到末尾
public class Solution {
    /**
     * @param nums: an array of integers
     * @return: the number of unique integers
     */
    public int deduplication(int[] nums) {
        // write your code here
        if (nums == null || nums.length == 0) return 0;
    
        Arrays.sort(nums);
        
        int slow = 0;
        for (int fast=0; fast<nums.length; ++fast) {
            if (nums[slow] != nums[fast]) nums[++slow] = nums[fast];
        }
        
        return slow + 1;
        
    }
}
```