class Solution {
    public int[] countSubTrees(int n, int[][] edges, String labels) {
        List<List<Integer>> adjL = new ArrayList<>();
        for(int i = 0;i < n; i++){
            adjL.add(new ArrayList<>());
        }
        for(int[] edge: edges){
            int src = edge[0];
            int dst = edge[1];
            adjL.get(src).add(dst);
            adjL.get(dst).add(src);
        }

        int count [] = new int[n];
        
        dfs(0,adjL,labels,count,0);
        return count; 
            
        
    }
    Map<Character,Integer> dfs(int index,List<List<Integer>> adj, String labels,int [] count, int parent){
        Map<Character,Integer> labelCount = new HashMap<>();
        for(int nbr:adj.get(index)){
            // System.out.println(nbr + " " + index);
            if(nbr == parent)
                continue;
            Map<Character,Integer> childLabelCount = dfs(nbr,adj,labels,count,index);
            for(char label:childLabelCount.keySet()){
                labelCount.put(label,childLabelCount.get(label) + labelCount.getOrDefault(label,0));
            }
        }
        labelCount.put(labels.charAt(index),1 + labelCount.getOrDefault(labels.charAt(index),0));
        count[index] = labelCount.get(labels.charAt(index));
        return labelCount;
            
    }
}