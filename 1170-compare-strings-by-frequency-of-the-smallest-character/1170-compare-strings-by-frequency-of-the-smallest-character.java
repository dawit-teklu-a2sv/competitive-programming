class Solution {
    public int[] numSmallerByFrequency(String[] queries, String[] words) {
        Arrays.sort(words,(w1,w2)->getValue(w1)-getValue(w2));

        int [] output = new int[queries.length];
            int i = 0;
            for (String query:queries){
                output[i] = words.length - find(words,getValue(query));
                    i++;
            }
        return output;
    }
    int find(String [] words,int bottomLimit){
        
        int low = 0;
        int high = words.length - 1;
        
        while (low < high){
            int mid = low + (high - low ) / 2;
            
            if (getValue(words[mid]) > bottomLimit)
                high = mid;
            else low = mid + 1;
        }
        if (low == high && getValue(words[low]) <= bottomLimit)
            return words.length;
        
        return low;
    }
    HashMap<String,Integer> map = new HashMap<>();
    int getValue(String s){
        if(map.containsKey(s))return map.get(s);
        char lowest = 'z' + 1;
        int freq = 0;
        for(int i = 0;i < s.length();i++){
            if(s.charAt(i) < lowest){
                lowest = s.charAt(i);
                freq = 1;
            }else if (s.charAt(i) == lowest)
                freq ++;
        }
        map.put(s,freq);
        return freq;
    }
}