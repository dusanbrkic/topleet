class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        sortedPositions = [i for i in range (0, len(position))]
        sortedPositions.sort(key= lambda e : position[e], reverse=True)

        fleets = 1
        carAhead = None
        for i in sortedPositions:
            try:
                arivalTime = (target - position[i]) / speed[i]
                arivalTimeCarAhead = (target - position[carAhead]) / speed[carAhead]
                if arivalTime > arivalTimeCarAhead:
                    fleets += 1
                    carAhead = i
                    
            except TypeError:
                carAhead = i
        
        return fleets