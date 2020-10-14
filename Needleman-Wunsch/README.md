# Homework 2 - Needleman-Wunsch

## Wiley Bui | buixx206@umn.edu | 5368469

## Files

```
.
├── AlignmentResults.txt
        Results from Anchored & Non-anchored version of Needleman-Wunsch algorithm
├── CoV_N_Histogram.png
        Histogram plots of permuted and observed alignment scores of N.
├── CoV_S_Histogram.png
        Histogram plots of permuted and observed alignment scores of S.
├── Match_N.txt
        Provided starting & ending of CoV1 and CoV2
├── Match_S.txt
        Provided starting & ending of CoV1 and CoV2
├── Needleman-Wunsch.py
        Implementation of the Needleman-Wunsch algorithm.
├── README.md
        This
├── Requirements.pdf
        Provided requirements for this project
├── SARS-CoV-1_N_protein.fna
        Provided Cov1 Protein (N)
├── SARS-CoV-1_S_protein.fna
        Provided Cov1 Protein (S)
├── SARS-CoV-2_N_protein.fna
        Provided Cov2 Protein (N)
└── SARS-CoV-2_S_protein.fna
        Provided Cov2 Protein (S)
```

## How to run count_codons

- ```python3 Needleman-Wunsch.py <input_CoV_query_file> <input_CoV_ref_file>```
- ```python3 Needleman-Wunsch.py <input_CoV_query_file> <input_CoV_ref_file> <match_file_for_anchored_version>```


## 100 Permutation Results for Non-Anchored Version

- SARS-CoV-N
        ```
                [-740, -757, -743, -728, -709, -761, -765, -749, -756, -764, -753, -764, -758, -775, -732, -798, -760, -731, -775, -764, -762, -775, -741, -801, -757, -784, -756, -710, -746, -702, -813, -757, -747, -728, -750, -744, -732, -780, -687, -774, -763, -734, -807, -750, -739, -738, -766, -717, -769, -754, -724, -778, -741, -750, -744, -760, -719, -756, -759, -769, -747, -748, -753, -742, -722, -749, -750, -730, -750, -762, -745, -728, -734, -765, -769, -747, -770, -796, -713, -784, -743, -753, -763, -740, -756, -783, -744, -790, -707, -769, -756, -759, -813, -763, -755, -774, -715, -753, -761, -725]
        ```

- SARS-CoV-S
        ```
                [-2150, -2153, -2168, -2121, -2128, -2144, -2142, -2210, -2203, -2172, -2082, -2137, -2159, -2072, -2172, -2165, -2118, -2154, -2135, -2162, -2128, -2119, -2178, -2135, -2132, -2145, -2113, -2142, -2233, -2117, -2162, -2137, -2071, -2202, -2211, -2204, -2100, -2093, -2128, -2135, -2165, -2092, -2123, -2161, -2149, -2153, -2131, -2105, -2130, -2076, -2161, -2154, -2151, -2080, -2176, -2158, -2123, -2098, -2105, -2185, -2116, -2165, -2173, -2113, -2157, -2205, -2151, -2080, -2104, -2137, -2091, -2143, -2158, -2111, -2202, -2114, -2170, -2128, -2158, -2152, -2156, -2176, -2179, -2175, -2191, -2197, -2159, -2132, -2172, -2181, -2092, -2110, -2114, -2177, -2125, -2142, -2081, -2152, -2209, -2012]
        ```