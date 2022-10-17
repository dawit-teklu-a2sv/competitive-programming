class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        output = [0] * n 
        for i in range(len(bookings)):
            start = bookings[i][0]
            end = bookings[i][1]
            seats = bookings[i][2]
            
            output[end - 1] += seats
            
            if start > 1:
                output[start-2] -= seats
        print(output)
        for j in range(n- 2,-1,-1):
            output[j] += output[j+1]
        return output
        
                