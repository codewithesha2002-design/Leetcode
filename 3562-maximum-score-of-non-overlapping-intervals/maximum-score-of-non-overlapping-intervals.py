from bisect import bisect_left

class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        n = len(intervals)
        
        # Store original index along with [l, r, weight]
        # Format: (r, l, weight, original_index)
        sorted_intervals = []
        for i, (l, r, w) in enumerate(intervals):
            sorted_intervals.append((r, l, w, i))
        
        # Sort primarily by end time 'r'
        sorted_intervals.sort(key=lambda x: x[0])
        
        # Array of end times to binary search on
        end_times = [x[0] for x in sorted_intervals]
        
        # dp[k][i] = (max_weight, tuple_of_sorted_original_indices)
        # using tuples for automatic lexicographical comparison
        # We store (weight, lexicographically_smallest_indices_tuple)
        
        # Base state: 0 items taken, 0 weight, empty index set
        # dp[k] stores the best state after considering up to index i for k intervals
        dp = [[(0, ())] * (n + 1) for _ in range(5)]
        
        for i in range(1, n + 1):
            r, l, w, orig_idx = sorted_intervals[i - 1]
            
            # Find index of last interval ending strictly before l
            # end_times[:prev_idx] are all end times < l
            prev_idx = bisect_left(end_times, l)
            
            for k in range(1, 5):
                # Option 1: Don't pick the i-th interval
                best_without = dp[k][i - 1]
                
                # Option 2: Pick the i-th interval
                prev_weight, prev_indices = dp[k - 1][prev_idx]
                curr_weight = prev_weight + w
                
                # Insert orig_idx in sorted order into the index tuple
                # to keep indices sorted within the selection
                curr_indices = tuple(sorted(prev_indices + (orig_idx,)))
                best_with = (curr_weight, curr_indices)
                
                # Custom tie-breaking:
                # 1. Higher weight wins
                # 2. If weight is equal, lexicographically smaller index tuple wins
                if best_with[0] > best_without[0]:
                    dp[k][i] = best_with
                elif best_with[0] < best_without[0]:
                    dp[k][i] = best_without
                else:
                    # Weights are equal: choose smaller index tuple
                    if best_with[1] < best_without[1]:
                        dp[k][i] = best_with
                    else:
                        dp[k][i] = best_without

        # Find the overall best result across selecting 1, 2, 3, or 4 intervals
        best_overall = (0, ())
        for k in range(1, 5):
            cand_weight, cand_indices = dp[k][n]
            if cand_weight > best_overall[0]:
                best_overall = (cand_weight, cand_indices)
            elif cand_weight == best_overall[0] and cand_weight > 0:
                if cand_indices < best_overall[1]:
                    best_overall = (cand_weight, cand_indices)
                    
        return list(best_overall[1])