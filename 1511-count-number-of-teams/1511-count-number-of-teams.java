class Solution {
    public int numTeams(int[] rating) {
        int num_teams = 0;
        for(int i=0; i<rating.length; i++){
            int left_greater = 0, left_smaller = 0, right_greater = 0, right_smaller = 0;

            int left = i-1, right = i+1;
            while(left>=0){
                if(rating[i]>rating[left]) left_smaller++;
                else if(rating[i]<rating[left]) left_greater++;
                left--;
            }

            while(right<rating.length){
                if(rating[i]>rating[right]) right_smaller++;
                else if(rating[i]<rating[right]) right_greater++;
                right++;
            }

            num_teams += left_greater*right_smaller + left_smaller*right_greater;
        }
        return num_teams;
    }
}