class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []
        sorted_pairs = sorted(zip(position, speed), reverse=True)

        # 2. Unpack them back into individual lists
        sorted_position = [pos for pos, spd in sorted_pairs]
        sorted_speed = [spd for pos, spd in sorted_pairs]


        for car in range(len(sorted_position)):
            time = ((target - sorted_position[car]) / sorted_speed[car])

            if stack:
                if time > stack[-1]:
                    stack.append(time)
            else:
                stack.append(time)

        return len(stack)