"""
AI Generated Answer
Mental model upgrade (this is the unlock)

Instead of thinking:

“Which character am I converting to?”

Think:

“How far is this window from being uniform?”

That distance is:
window_size - max_freq
"""

from collections import defaultdict


class Solution:
    # TODO: Use a freq_map to track the max_freq_in_window - only look for letters that are of the max freq in the window
    def characterReplacement(self, s: str, k: int) -> int:
        longest_streak = 0

        for curr_streak_letter in set(s):
            i = 0
            changes_remaining = k

            for j in range(len(s)):
                if s[j] != curr_streak_letter:
                    changes_remaining -= 1

                while changes_remaining < 0:
                    if s[i] != curr_streak_letter:
                        changes_remaining += 1
                    i += 1

                longest_streak = max(longest_streak, j - i + 1)

        return longest_streak

    def characterReplacementMoreEfficient(self, s: str, k: int) -> int:
        def get_highest_freq_char_in_window(
            char_freq_map_in_window_dict: dict[str, int],
        ) -> str:
            # TODO: Is there a dict-like data structure that we can get the max in O(1) time?
            all_freqs = list(char_freq_map_in_window_dict.items())
            # TODO: Is this always alphabetical with entry[0] (the character ord?)
            # return sorted(all_freqs, key=lambda entry: entry[1])[0][0]
            return max(all_freqs, key=lambda entry: entry[1])[0]

        if len(s) == 0:
            return 0

        longest_streak = 0
        i = 0
        char_freq_map_in_window = defaultdict(int)
        curr_char_with_highest_freq = s[0]
        char_conversions_remaining_in_window = k

        for j in range(len(s)):
            char_freq_map_in_window[s[j]] += 1
            curr_char_with_highest_freq = get_highest_freq_char_in_window(
                char_freq_map_in_window
            )
            if s[j] == curr_char_with_highest_freq:
                longest_streak = max(longest_streak, j - i + 1)
            elif (
                s[j] != curr_char_with_highest_freq
                and char_conversions_remaining_in_window > 0
            ):
                char_conversions_remaining_in_window -= 1
                longest_streak = max(longest_streak, j - i + 1)
            else:
                while i < j and char_conversions_remaining_in_window == 0:
                    if s[i] != curr_char_with_highest_freq:
                        char_conversions_remaining_in_window += 1
                    char_freq_map_in_window[s[i]] -= 1
                    # NOTE: It doesn't matter what the order of the chars is in the window that you're looking at
                    # All that matters is the number of the character that we want to extend the streak
                    # We can greedily assume this is the most frequent element in the window since we can place the
                    # replacement chars as any character in any order in the string
                    prev_char_with_highest_freq = curr_char_with_highest_freq
                    curr_char_with_highest_freq = get_highest_freq_char_in_window(
                        char_freq_map_in_window
                    )
                    if prev_char_with_highest_freq != curr_char_with_highest_freq:
                        char_conversions_remaining_in_window += 1

                    i += 1

        return longest_streak

    def characterReplacementMostEfficient(self, s: str, k: int) -> int:
        count = defaultdict(int)
        max_freq = 0
        i = 0
        longest = 0

        # Step 1: Expand the sliding window to the right
        # Step 2: Restore the loop invariant if neccesary
        # Step 3: Compute the desired quantity

        for j in range(len(s)):
            count[s[j]] += 1
            max_freq = max(max_freq, count[s[j]])
            window_size = j - i + 1
            # NOTE: Key loop invariant - how far is the window from being uniform?
            while window_size - max_freq > k:
                count[s[i]] -= 1
                i += 1

            longest = max(longest, j - i + 1)

        return longest

        # TODO: I'm on the tail of the most efficient solution, just do the O(alphabet_size * s) solution first
        # longest_streak = 1
        # i,j = 0,0
        # num_letter_changes_remaining = k
        # curr_streak_letter = s[0]
        # while j < len(s):
        #     j += 1
        #     if s[j] == curr_streak_letter:
        #         longest_streak = max(longest_streak, j - i + 1)
        #     elif s[j] != curr_streak_letter and num_letter_changes_remaining > 0:
        #         num_letter_changes_remaining -= 1
        #         longest_streak = max(longest_streak, j - i + 1)
        #     elif s[j] != curr_streak_letter and num_letter_changes_remaining == 0:
        #         while i < j:
        #             if s[i] != current_streak_letter:
        #                 # Use a num_letter_changes_remaining to break out of the loop
        #                 break
        #             i += 1
        #         if i == j:
        #             curr_streak_letter = s[i]
        #             num_letter_changes_remaining = k
        # return longest_streak
