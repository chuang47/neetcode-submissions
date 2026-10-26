class Solution {
    public boolean hasDuplicate(int[] nums) {

        if(nums.length==0){
            return false;
        }

        ArrayList<Integer> seen = new ArrayList<Integer>();
        seen.add(nums[0]);

        for(int i=1; i<nums.length; i++){
            if(seen.contains(nums[i])) return true;
            seen.add(nums[i]);
        }

        return false;
    }
}