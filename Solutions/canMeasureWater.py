class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        # Combined amount of water in the 2 jugs is equal to the target capacity
        # Can only work with integer amounts of water
        seen = set()

        @cache # Memoization
        def can_measure_helper(total_volume):
            if total_volume == targetCapacity:
                return True
            elif total_volume in seen or total_volume < 0 or total_volume > (jug1Capacity + jug2Capacity):
                return False
            
            seen.add(total_volume)
            return can_measure_helper(total_volume + jug1Capacity) or can_measure_helper(total_volume + jug2Capacity) or can_measure_helper(total_volume - jug1Capacity) or can_measure_helper(total_volume - jug2Capacity)

        return can_measure_helper(0)