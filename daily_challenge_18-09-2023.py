class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # Create a list of tuples containing row index and soldier count, then sort it
        rows_count = sorted(((i, sum(row)) for i, row in enumerate(mat)), key=lambda x: (x[1], x[0]))
        # Extract the row indices of the k weakest rows
        return [x[0] for x in rows_count[:k]]