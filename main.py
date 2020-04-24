import random

def estimate(n):
    num_points_circle = 0
    num_points_total = 0
    for _ in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        dis = x**2 + y**2
        if dis <= 1:
            num_points_circle += 1
        num_points_total += 1
    
    value = 4 * num_points_circle/num_points_total
    print(value)  



if __name__ == '__main__':
    n = input("Enter the number: ")
    n = int(n)
    estimate(n)

