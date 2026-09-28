"""Example demonstrating Needleman-Wunsch global alignment."""
from client import NeedlemanWunschAligner

def main():
    s1 = "GCATGCG"
    s2 = "GATTACA"
    res = NeedlemanWunschAligner.align(s1, s2)
    print("Global Alignment Results:")
    print("  Score:", res["score"])
    print("  Align 1:", res["align1"])
    print("  Align 2:", res["align2"])

if __name__ == "__main__":
    main()
