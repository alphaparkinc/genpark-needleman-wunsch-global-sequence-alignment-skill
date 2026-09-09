from client import NeedlemanWunschAligner

def main():
    print("=== Needleman-Wunsch Global Sequence Aligner ===")
    aligner = NeedlemanWunschAligner(match_score=1, mismatch_penalty=-1, gap_penalty=-2)
    res = aligner.align("GCATGCG", "GATTACA")

    print("Alignment Result:", res)
    assert res["score"] == -1
    assert len(res["aligned_seq1"]) == len(res["aligned_seq2"])
    print("Needleman-Wunsch Aligner verified successfully!")

if __name__ == "__main__":
    main()
