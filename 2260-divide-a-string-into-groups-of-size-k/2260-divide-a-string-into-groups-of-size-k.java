class Solution {
    public String[] divideString(String s, int k, char fill) {
        int size = s.length()/k;
        int remainder = s.length()%k;
        String[] ans;
        if(remainder!=0) ans = new String[size+1];
        else ans = new String[size];
        for(int i=0;i<size;i++){
            ans[i] = s.substring(i*k,i*k+k);
        }
        if(remainder!=0){
            ans[ans.length-1] = s.substring(s.length()-remainder);
            for(int i=0;i<k-remainder;i++){
                ans[ans.length-1] += Character.toString(fill);
            }
        }
        return ans;
    }
}