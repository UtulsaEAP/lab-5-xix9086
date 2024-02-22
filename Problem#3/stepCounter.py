def feet_to_steps(user_feet):
   return(user_feet / 2.5)
   #write your code here

if __name__ == '__main__':
    feet_steps = float(input())#take input feet steps here
    steps = int(feet_to_steps(feet_steps))#store it into the function
    print(steps)#print your steps here