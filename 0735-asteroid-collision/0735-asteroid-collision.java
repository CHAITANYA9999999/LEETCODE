class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> st = new Stack<>();
        for(int num : asteroids){
                if(st.isEmpty() || num>0) st.push(num);
                else{
                    boolean equal = false;
                    while(!st.empty()&&st.peek()>0&&st.peek()<Math.abs(num)){
                    st.pop();
                }
                if(!st.isEmpty()&&st.peek()>0){
                    if(st.peek()==Math.abs(num)){
                        st.pop();
                    }
                }
                else{
                    st.push(num);
                }
                }
        }
        int len = st.size();
        int[] arr = new int[len];
        for(int i=len-1;i>=0;i--){
            arr[i] = st.pop();
        }
        return arr;
    }
}