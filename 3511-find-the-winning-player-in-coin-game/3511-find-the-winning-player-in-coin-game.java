class Solution {
    public String losingPlayer(int x, int y) {
        boolean isAliceWinner = false;
        while(x>=1 && y>=4){
            isAliceWinner = !isAliceWinner;
            x-=1;
            y-=4;
        }
        return isAliceWinner ? "Alice" : "Bob";
    }
}