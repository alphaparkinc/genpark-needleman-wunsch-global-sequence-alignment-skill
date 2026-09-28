# Needleman-Wunsch Global Sequence Alignment Skill

Dynamic programming formulation for rigorous end-to-end global alignment of nucleotide and amino acid sequences.

```mermaid
flowchart TD
    Boundaries["Initialize Top/Left Margins with Cumulative Gap Penalties"] --> Matrix["Dynamic Programming Recurrence: max(Match, Del, Ins)"]
    Matrix --> Traceback["Traceback from Bottom-Right Cell dp[m][n] to dp[0][0]"]
    Traceback --> Global["Global Sequence Alignment (with Optimal Gaps)"]
```

## Features
- **100% Python Standard Library**: Zero third-party dependencies.
- **Global Optimality Guarantee**: Finds true mathematical optimum alignment.
- **Full Traceback Path**: Complete reconstruction of aligned character strings.
