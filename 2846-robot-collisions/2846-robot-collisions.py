class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        if len(set(directions)) == 1:
            return healths
        config=[]
        for i in range(len(positions)):
            config.append([positions[i],healths[i],directions[i],i])
        
        config.sort(key = lambda x: x[0])
        st = []

        for position,health,direction,idx in config:
            if (direction == "L" and (len(st) == 0 or st[-1][2] == "L")) or direction == "R":
                st.append([position,health,direction,idx])
            else:
                while len(st)!=0 and st[-1][2] == "R" and st[-1][1] < health:
                    st.pop()
                    health-=1
                if len(st) == 0:
                    st.append([position,health,direction,idx])
                elif st[-1][2] == "R":
                    if st[-1][1] == health:
                        st.pop()
                        continue
                    else:
                        st[-1][1]-=1
                else:
                    st.append([position,health,direction,idx])
        st.sort(key = lambda x : x[3])
        res = []
        for position,health,direction,idx in st:
            res.append(health)
        print(res)
        return res