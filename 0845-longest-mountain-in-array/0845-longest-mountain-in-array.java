class Solution {
    public int longestMountain(int[] arr) {
        int res = 0;
        int n = arr.length;
        for (int i = 1;i<n;i++){
            int count = 1;
            boolean flag = false;
            int j = i;
            while(j < n && arr[j] > arr[j-1]){//increasing sequence
                count++;
                j ++;
            }
            while(i != j && j < n && arr[j]  < arr[j-1]){//decreasing sequence
                j ++;
                count ++;
                flag = true;
            }
            if(i!=j && flag && count > 2){
                res = Math.max(res,count);
                j--;
                
            }
            i = j;
        }
        return res;
    }
}