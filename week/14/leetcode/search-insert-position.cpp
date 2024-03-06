class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
      int min = 0;
    int max = nums.size() - 1;
  
    while (min <= max) {
        int middle = (int)((max + min) / 2);
        if (target == nums[middle]) {
            return middle;
        } else if (target > nums[middle]) {
            min = middle + 1;
        } else {
            max = middle - 1;
        }
    }
    return min;   
    }
};
