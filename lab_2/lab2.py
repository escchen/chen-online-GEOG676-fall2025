# Part 1: Multiply all items together
part1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

total1 = 1
for i in range(len(part1)):
    total1 *= part1[i]
print('Part 1 multiplied together =', total1)

# Part 2: Add all items together
part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]

total2 = 0
for i in range(len(part2)):
    total2 += part2[i]
print('Part 2 added together =', total2)

# Part 3: Add only even items together
part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21] 
# isEven = num1 % 2 == 0

total3 = 0
for i in range(len(part3)):
    num = part3[i]
    if num % 2 == 0: # even
        total3 += num
print('Part 3 evens added together =', total3)