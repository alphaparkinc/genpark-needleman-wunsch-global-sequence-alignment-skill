class NeedlemanWunschAligner:
    """Optimal global pairwise sequence alignment in pure Python."""
    def __init__(self, match_score: int = 1, mismatch_penalty: int = -1, gap_penalty: int = -2):
        self.match = match_score
        self.mismatch = mismatch_penalty
        self.gap = gap_penalty

    def align(self, seq1: str, seq2: str) -> dict:
        n, m = len(seq1), len(seq2)
        score = [[0] * (m + 1) for _ in range(n + 1)]
        trace = [[0] * (m + 1) for _ in range(n + 1)] # 1: Diag, 2: Up, 3: Left

        for i in range(1, n + 1):
            score[i][0] = i * self.gap
            trace[i][0] = 2
        for j in range(1, m + 1):
            score[0][j] = j * self.gap
            trace[0][j] = 3

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                diag = score[i - 1][j - 1] + (self.match if seq1[i - 1] == seq2[j - 1] else self.mismatch)
                up = score[i - 1][j] + self.gap
                left = score[i][j - 1] + self.gap
                best = max(diag, up, left)
                score[i][j] = best
                if best == diag: trace[i][j] = 1
                elif best == up: trace[i][j] = 2
                else: trace[i][j] = 3

        # Backtrack alignment
        aligned1, aligned2 = [], []
        i, j = n, m
        while i > 0 or j > 0:
            if i > 0 and j > 0 and trace[i][j] == 1:
                aligned1.append(seq1[i - 1])
                aligned2.append(seq2[j - 1])
                i -= 1
                j -= 1
            elif i > 0 and trace[i][j] == 2:
                aligned1.append(seq1[i - 1])
                aligned2.append("-")
                i -= 1
            else:
                aligned1.append("-")
                aligned2.append(seq2[j - 1])
                j -= 1

        aln1 = "".join(reversed(aligned1))
        aln2 = "".join(reversed(aligned2))
        matches = sum(1 for a, b in zip(aln1, aln2) if a == b and a != "-")

        return {
            "score": score[n][m],
            "aligned_seq1": aln1,
            "aligned_seq2": aln2,
            "identity_ratio": round(matches / max(1, len(aln1)), 4)
        }
