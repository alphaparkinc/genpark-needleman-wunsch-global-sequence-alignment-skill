"""Needleman-Wunsch Global Sequence Alignment.
100% Python Standard Library.
"""

class NeedlemanWunschAligner:
    """Computes global end-to-end alignment between two sequences."""
    @staticmethod
    def align(seq1, seq2, match_score=1, mismatch_penalty=-1, gap_penalty=-1):
        m, n = len(seq1), len(seq2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i * gap_penalty
        for j in range(n + 1):
            dp[0][j] = j * gap_penalty
            
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                match = dp[i-1][j-1] + (match_score if seq1[i-1] == seq2[j-1] else mismatch_penalty)
                delete = dp[i-1][j] + gap_penalty
                insert = dp[i][j-1] + gap_penalty
                dp[i][j] = max(match, delete, insert)
                
        align1, align2 = [], []
        i, j = m, n
        while i > 0 or j > 0:
            if i > 0 and j > 0 and dp[i][j] == dp[i-1][j-1] + (match_score if seq1[i-1] == seq2[j-1] else mismatch_penalty):
                align1.append(seq1[i-1])
                align2.append(seq2[j-1])
                i -= 1
                j -= 1
            elif i > 0 and dp[i][j] == dp[i-1][j] + gap_penalty:
                align1.append(seq1[i-1])
                align2.append('-')
                i -= 1
            else:
                align1.append('-')
                align2.append(seq2[j-1])
                j -= 1
                
        return {
            "score": dp[m][n],
            "align1": "".join(reversed(align1)),
            "align2": "".join(reversed(align2))
        }
