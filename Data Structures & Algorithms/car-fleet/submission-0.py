from math import inf


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        fleet_reach_at = -1
        for pos, speed in cars:
            reach_at = (target - pos) / speed
            if reach_at > fleet_reach_at + 0.000001:
                fleets += 1
                fleet_reach_at = reach_at
        return fleets