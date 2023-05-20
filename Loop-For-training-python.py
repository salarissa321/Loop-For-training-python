




#-----------------------------------------
#------- Loop => For Trainings-----------
#-----------------------------------------


# Range


myRange = range(1 , 101)

for number in myRange :
    print(number) # 1 until 100



# Dictionary 

mySkills = {
    "Html" : "90%" ,
    "Css" : "60%" ,
    "PHP" : "70%" ,
    "JS" : "80%" ,
    "Python" : "90%"
}

# print(mySkills["JS"]) # 80%
# print(mySkills.get("Python")) # 90%


for skill in mySkills :
    # print(skill) # HTML , CSS , PHP , Js , Python
    print(f"My Progress in Lang {skill} Is : {mySkills[skill]}") # my progress in lang Html is : 90% # my progress in lang Css is : 60% # My Progress in Lang PHP Is : 70% # My Progress in Lang JS Is : 80% # My Progress in Lang Python Is : 90%
    print(f"My Progress in Lang {skill} Is : {mySkills.get(skill)}") # my progress in lang Html is : 90% # my progress in lang Css is : 60% # My Progress in Lang PHP Is : 70% # My Progress in Lang JS Is : 80% # My Progress in Lang Python Is : 90%


