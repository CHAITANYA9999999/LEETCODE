class Solution {
    public List<Integer> luckyNumbers (int[][] matrix) {
        HashSet<Integer> col_max = new HashSet<>();
        for(int i=0; i<matrix[0].length; i++){
            int max = matrix[0][i];
            for(int j=1; j<matrix.length; j++){
                max = Math.max(max,matrix[j][i]);
            }
            col_max.add(max);
        }
        
        List<Integer> lucky = new ArrayList<>();

        for(int i=0; i<matrix.length; i++){
            int min = matrix[i][0];
            for(int j=1; j<matrix[0].length; j++) min = Math.min(min,matrix[i][j]);
            System.out.println(min);
            if(col_max.contains(min)) lucky.add(min);
        }
        return lucky;
    }
}