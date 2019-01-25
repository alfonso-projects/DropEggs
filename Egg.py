#we could create a class and encapsulate the functions and the variables inside of it.

'''
    Ez dificulty:

        available_eggs = 100
        high = 100
        
    medium dificulty:

        available_eggs = 2
        high = 100
    hard dificulty:

        high = the quantity that you want
        available_eggs = the quantity that you want

'''

#MODIFY VARIABLES HERE. GLOBAL VARIABLES

available_eggs = 100
high = 40
critical_floor = 10



'''

EXLANATION:

        we pass to the function the start and the finish of the skycrapper. We throw an egg from the middle of the skrycapper if the egg breaks we discart 
        the floor from it has fallen to the finish of the skrycapper, and we anotate that we have used another egg.

        if has not been broken we bounded the building from 0 to to the floor that we have fallen the egg. 

        We repeat this operation until we have only twoo floors or one. When we arrive to this situation we drop an egg from the middle flor, if the eggs broke the critical floor is
        the floor that we have dropped it minus one.


        In the case that we only have one egg left for drop we can not use the avobe operation because we could waste the egg and not find the critical floor for that reason we will
        start from the start index point and we will drop the egg from start + 2, if it breaks we know that the critical floor will be start -1, if is not broken, we update start 
        to the last floor that we have dropped the egg and we will repeat the operation. Resolving the problem at this way will be more expensive but at the same time
        we make sure that we wont waste the last egg that we have available
        

'''


#______________________________________________
#basic medium and hard difficulty
# we pass to this funcion the number of available eggs and the high of the skycrapper and returns the numbers of tries to find the critical floor
#______________________________________________


def minEggDropper100(eggs , high):
    
    def recursive_function(start, finish, eggs_used,tries):

        if(eggs_used == eggs-1):
            return dropEgssCarefully(start, finish,eggs_used, tries) 
        else:
            middle =  (start+finish) // 2

            if finish - start == 2 or finish-start == 1:

                if(aux_egg_drop(middle) == False):
                    #critical_floor_searched = start
                    eggs_used = eggs_used + 1
                    tries = tries +1
                    return tries
                else:
                    tries = tries +1
                    
                if(aux_egg_drop(finish)== False):
                    #critical_floor_searched = middle
                    tries = tries +1
                    eggs_used = eggs_used + 1
                else:
                    tries = tries + 1
                    critical_floor_searched = middle
                    
                return tries

            if aux_egg_drop(middle) == False: # si el medio es mayor que la planta critica entonces lo hemos jodido
                eggs_used = eggs_used +1
                finish = middle
                tries = tries+1
                res = recursive_function(start, finish, eggs_used, tries)
            else: # sino miramos desde inicio hasta final
                start = middle
                tries = tries+1
                res = recursive_function(start, finish, eggs_used, tries)

            return res

    def dropEgssCarefully(start, finish, eggs_used, tries):

        critical_floor_searched = None
        while start <  finish:
            if aux_egg_drop(start) == False:
                tries = tries +1
                eggs_used = eggs_used +1
                critical_floor_searched = start -1
                break
            else:
                tries=tries+1
                start = start + 2

        if finish == start and critical_floor_searched is None:
            critical_floor_searched = finish

        return tries

    eggs_used = 0
    tries = 0
    min_drops = recursive_function(0, high, eggs_used, tries)
    return min_drops


#______________________________________________
#Auxiliar function. Drop an egg from a floor and returns true if the egss has broken and false if its fine and we can reuse the egg for the next try
#______________________________________________

def aux_egg_drop(floor): # true si no se ha roto, false si se ha roto

    if(floor > critical_floor):
        return False
    else:
        return True


if __name__ == "__main__":

    result = minEggDropper100(available_eggs, high)
    print("the total tries to find the critical floor are {0}".format(result))