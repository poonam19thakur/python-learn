#1
team_A = 56
team_B = 20
team_C = 40
team_D = 73
team_E = 43


#2.
total = team_A + team_B + team_C + team_D + team_E
average = total/5

print('Total points are:',total)
print('Average points are:',average)


#3.
stars_per_point = 20
total_reward_stars = 20 * total

print('Total Reward Stars:',total_reward_stars)


#4.
box_storage = 25
print('Boxes Needed:',total_reward_stars//box_storage)
print('Stars left:',total_reward_stars%box_storage)


#5.
last_week = 350
print('Last week had greater stars:',last_week >= total)
print('Both had equal stars:',last_week == total)
print('Last week had lesser stars:',last_week <= total)


#6.
total_reward_stars += 20


print('After bonus:',total_reward_stars) 


total_reward_stars -= 6


print('After missed tasks:',total_reward_stars) 