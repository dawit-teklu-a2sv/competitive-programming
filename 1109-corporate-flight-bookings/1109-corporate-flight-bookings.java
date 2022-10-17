class Solution {
    public int[] corpFlightBookings(int[][] bookings, int n) {
        int res[] = new int[n];
        int start;
        int end;
        int seats;
        for(int i = 0; i< bookings.length;i++){
            start = bookings[i][0];
            end = bookings[i][1];
            seats = bookings[i][2];
            
            res[end-1] += seats;
            
            if (start > 1)
                res[start - 2] -= seats;
            
            
        }
        for (int i = n-2; i >= 0; i--){
            res[i] += res[i+1];
        }
        return res;
        
    }
}