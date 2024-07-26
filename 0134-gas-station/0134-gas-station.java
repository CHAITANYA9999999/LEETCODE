class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int g = 0;
        for(int ga : gas) g += ga;

        int c = 0;
        for(int co : cost) c += co;

        if(c>g) return -1;

        int starting = 0;
        int total_gas = 0;
        for(int i =0; i<gas.length; i++){
            total_gas += gas[i] - cost[i];
            if(total_gas<0){
                total_gas = 0;
                starting = i+1;
            }
        }
        return starting;

    }
}