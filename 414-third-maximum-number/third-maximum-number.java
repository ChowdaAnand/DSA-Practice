class Solution {
    public int thirdMax(int[] nums) {
        int lar=nums[0];
        int n=nums.length;
        for(int i=0;i<n;i++){
            if(nums[i]>lar){
                lar=nums[i];
            }
        }
       Integer s_lar=null;
       for(int i=0;i<n;i++){
        if(nums[i]!=lar &&(s_lar==null || s_lar<nums[i])){
            s_lar=nums[i];
        }
       }
       if(s_lar==null){
        return lar;
       }
       Integer thi=null;
       for(int i=0;i<n;i++){
        if(nums[i]!=lar && nums[i]!=s_lar && (thi==null || nums[i]>thi)){
            thi=nums[i];
        }
       }
       if(thi==null){
        return lar;
       }
       return thi;
    }
}