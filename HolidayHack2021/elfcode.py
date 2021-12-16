########### the elf code ################
munchkin.answer(answer)
elf.moveLeft(1)
elf.moveRight(2)
sum = lever.data() * 3
lever.pull(sum)

import elf, munchkins, levers, lollipops, yeeters, pits
# Grab our lever object
lever = levers.get(0)
munchkin = munchkins.get(0)
lollipop = lollipops.get(0)
# move to lever position
elf.moveTo(lever.position)
# get lever int and add 2 and submit val
leverData = lever.data() + 2
lever.pull(leverData)
# Grab lollipop and stand next to munchkin
elf.moveLeft(1)
elf.moveUp(8)
# Solve the munchkin's challenge
munchList = munchkin.ask() # e.g. [1, 3, "a", "b", 4]
answer_list = []
for elem in munchList:
    if type(elem) == int:
        answer_list.append(elem)
munchkin.answer(answer_list)
elf.moveUp(2) # Move to finish


import levers
all_levers = levers.get()
print(all_levers)
# [<levers.lever object <lever(0)>>, <levers.lever object <lever(1)>>]

#### LEVEL 1 
import elf, munchkins, levers, lollipops, yeeters, pits
###elf.moveTo(lollipop.position)

# elf.moveTo(lollipop.position)
# You can get this lollipop and save it to a variable named lollipop using lollipop = lollipops.get(0)
lollipop = lollipops.get(0)
elf.moveTo(lollipop.position)
elf.moveTo({'x':2, 'y':2})


#### LEVEL 2
import elf, munchkins, levers, lollipops, yeeters, pits
# Gets all lollipops as a list
all_lollipops = lollipops.get()
# Can set lollipop1 using:
lollipop1 = all_lollipops[1]
# or:
lollipop0 = all_lollipops[0]
elf.moveTo(lollipop1.position)
elf.moveTo(lollipop0.position)
elf.moveTo({'x':2, 'y':2})



#### Level 3
#You can walk past the Yeeter once you complete lever0's task and lever0.pull(modified_data) in the desired way to disable to Yeeter trap. Click on the lever 0 object in the CURRENT LEVEL OBJECTS panel for more information.
import elf, munchkins, levers, lollipops, yeeters, pits
lever0 = levers.get(0)
lollipop0 = lollipops.get(0)
elf.moveTo(lever0.position)
sum = lever0.data() + 2
lever0.pull(sum)
elf.moveTo(lollipop0.position)
elf.moveTo({'x':2, 'y':2})



#### Level 4
import elf, munchkins, levers, lollipops, yeeters, pits


# Move onto lever4
elf.moveLeft(2)
# This lever wants a str object:
lever4.pull("A String")
# Need more code below:
elf.moveTo(lever3.position)
lever3.pull(False)
elf.moveTo(lever2.position)
lever2.pull(1)
elf.moveTo(lever1.position)
lever1.pull(["A String","another String"])
elf.moveTo(lever0.position)
lever0.pull({"A":0,"B":1})
elf.moveTo({'x':2, 'y':2})

### collapse into a loop
import elf, munchkins, levers, lollipops, yeeters, pits
lever_dict = {4: "A String", 3:False, 2:1, 1:['str','asd'], 0:{"A":0,"B":1}}
for num in lever_dict:
    lever = levers.get(num)
    elf.moveTo(lever.position)
    lever.pull(lever_dict[num])

elf.moveTo({'x':2, 'y':2})


#### Level 5
import elf, munchkins, levers, lollipops, yeeters, pits
# Fix/Complete Code below
lever0, lever1, lever2, lever3, lever4 = levers.get()
elf.moveTo(lever4.position)
lever4.pull("{} concatenate".format(lever4.data()))
elf.moveTo(lever3.position)
lever3.pull(not lever3.data())
elf.moveTo(lever2.position)
lever2.pull(lever2.data()+1)
elf.moveTo(lever1.position)
ans = lever1.data()
ans.append(1)
lever1.pull(ans)
elf.moveTo(lever0.position)
ans = lever0.data()
ans["strkey"] = "strvalue"
lever0.pull(ans)
elf.moveTo({'x':2, 'y':2})


#### Level 6
import elf, munchkins, levers, lollipops, yeeters, pits
# Fix/Complete the below code
lever = levers.get(0)
data = lever.data()
if type(data) == bool:
    data = not data
elif type(data) == int:
    data = data * 2 
elif type(data) == str:
    data = data + data
elif type(data) == dict:
    data["a"] = data["a"] + 1
elif type(data) == list:
    for i in data:
        i =+ i
elf.moveTo(lever.position)
lever.pull(data)
elf.moveTo({'x':2, 'y':2})

#elf.move
#lever.something


#### Level 7 
#Objective
#Navigate through the obstacles and collect the lollipop before arriving at the KringleCon entrance.

#Hints
#Using a for loop can reduce how many lines and/or object function calls are used. This link on for loops may be helpful.

#Using elf.moveLeft(40) will move your elf as far as possible before hitting an obstacle or the end of the screen. Use however large a number you think you need!
import elf, munchkins, levers, lollipops, yeeters, pits
for num in range(2): #not sure if number is right
    elf.moveLeft(3)
    elf.moveUp(12)
    elf.moveLeft(3)
    elf.moveDown(12)
    # needs more code
elf.moveTo({'x':2, 'y':12})
elf.moveTo({'x':2, 'y':2})
    
##### Level 8
import elf, munchkins, levers, lollipops, yeeters, pits
all_lollipops = lollipops.get()
for lollipop in all_lollipops:
    elf.moveTo(lollipop.position)
    # needs more code
lever = levers.get(0)
elf.moveTo(lever.position)
ans = lever.data()
ans.insert(0,"munchkins rule")
lever.pull(ans)
elf.moveTo({'x':8, 'y':4})
elf.moveTo({'x':2, 'y':2})

#### WIN