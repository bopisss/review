data = [
    ["fish", "Food", 120, 400, 425],
    ["beef", "Food", 400, 250, 300],
    ["egg", "Food", 10, 425, 450],
    ["pen", "Non-Food", 20, 312, 401],
    ["eraser", "Non-Food", 5, 252, 301],
    ["sharpener", "Non-Food", 10, 272, 297]
]

#11
for sah in data:
    print(f'Category: {sah [1]}, Product Name: {sah [0]}, Price: {sah [2]} ')
 
 #12
food_sum = 0   
for sah in data:
    if sah[1] == "Food":
        food_sum += sum(sah[2:5])

print(f'sum: {food_sum}')

#13
food_sum = 0
food_count = 0
non_f = 0
non_count = 0

for sah in data:
    if sah[1] == 'Food':
        food_sum += sum(sah[2:5])
        food_count += len(sah[2:5])
    elif sah[1] == 'Non-Food':
        non_f += sum(sah[2:5])
        non_count += len(sah[2:5])
        
print(f'Average of Food Prices: {food_sum/food_count}')
print(f'Average of Food Prices: {non_f/non_count}')

#14
highest = 0
for sah in data:
    if sah[1] == "Non-Food":
        highest = max(highest, max(sah[2:5]))
        
print(f'Highest Price of Non-Food: {highest}')

#15
june = 0
for sah in data:
    if sah[1] == 'Food':
        june += sum(sah[3:4])
        
print(f'Total sales of June: {june}')

#16
june = 0
july = 0 

for sah in data:
    if sah[1] == "Non-Food":
        june += sum(sah[3:4])
        july += sum(sah[4:5])

print(f'Total sales of Non-Food(June and july): {june+july}')