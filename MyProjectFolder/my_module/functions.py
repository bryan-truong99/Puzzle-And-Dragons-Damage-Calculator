"""Functions that are used in the Puzzle and Dragons damage calculator"""

def card_identity(monster_name):
    """Takes monster name provided by user, searches through library, and provides attack value.
    
    Parameters
    ----------
    monster_name: string
        The name of the monster that is searched in the card library
        
    Returns
    -------
    attack_value: integer
        The monster's corresponding attack value.
        
    """
    
    #Contains monster names and their respective attack value
    card_library = {
        'Mega Awoken Dark Angel Metatron': '2640', 
        'Black Dragon, Fatalis': '4000',
        'Spirit Detective, Yusuke Urameshi': '1820',
        'Super Reincarnated Haku': '2595',
        'Zeta (Dark Color)': '2683',
        'Hello Kitty' : '554',
        'Super Saiyan 3 - Goku': '1604',
        'Massacre Demon Diablos': '3953',
        'Attack on Titan, Eren Yeager' : '1801',
        'Reincarnated Ra': '1548'
    }
        
    #Explains what the desired monster's attack value is, given that it is in the library, and stores attack value
    if monster_name in card_library:
        
        attack_value = int(card_library[monster_name])
        
        print ('Your card\'s attack value is '+ card_library[monster_name])
        
        return attack_value
    
    else:
        
        print ('Your card does not exist in the database.')
        
        attack_value = 0
        
        return attack_value
    
    
    
def combo_multiplier(amt_of_combos, same_attribute_combos, amt_of_orb_enhance):
    
    """Takes amount of combos inputted, including same attribute combos,
    and amount of enhanced orbs and returns the damage multiplier.
    
    Parameters
    ----------
    amt_of_combos: string
        The total amount of combos that will be applied to the formula, converted into int
        
    same_attribute_combos: string 
        The amount of same attribute combos that will be applied to the formula,
        which cannot exceed the total amount of combos, converted into int
    
    amt_of_orbenhance: string
        The amount of orbs that are enhanced in the combos done by the user, will
        be factored in the formula for the final multiplier, converted into int
    
    Returns
    -------
    output_multiplier: integer or float
        The final multiplier after applying the formula to the three inputs
    
    """
    
    #Checks to see if user input is int so that it may go further and apply the combo formula
    if amt_of_combos.isdigit() and same_attribute_combos.isdigit() and amt_of_orb_enhance.isdigit():
        
        #The total amount of combos must be greater or equal to the amount of same attribute combos in order to continue
        if int(amt_of_combos) >= int(same_attribute_combos):
       
            #Takes inputted int values and applies combo formula, returns the multiplier value
            if int(amt_of_combos)!=0 and int(same_attribute_combos)!=0:
        
                output_multiplier = ((1+((int(amt_of_combos)-1)/4))* 
            
                ((1+(int(amt_of_orb_enhance)*0.06))*int(same_attribute_combos)))
        
                print('Your combo multiplier is '+str(output_multiplier))
                
                return output_multiplier
        
            else:
        
                print ('LOL are you even trying?')
            
                output_multiplier = 0
        
                return output_multiplier
        
        else:
            
            print('It is not possible to have more same attribute combos than your total amount of combos.')
            
            output_multiplier = 0
        
            return output_multiplier
        
    else:
        
        print('Please enter a valid number.')
        
        output_multiplier = 0
        
        return output_multiplier
    
    
    
def damage_awakenings(number_of_damage_awakenings):
    
    """Takes number of damage awakenings from user provided list and 
    calculates the total multiplier from the damage awakenings and their
    individual multipliers.
    
    Parameters
    ----------
    list_of_damage_awakenings: string
        User inputted string that will be turned into a list and converted to int,
        so that its elements may be operated on, resulting in the final output
    
    Returns
    -------
    total_awakening_multiplier: integer or float
        The total multiplier that results from the inputs after they are operated on
    
    """
    
    int_change_list= number_of_damage_awakenings.split()
    
    str_of_int_change_list=''.join(int_change_list)
    
    #Checks if provided list consists of numbers, so that it may be operated on
    if str_of_int_change_list.isdigit():
        
        list_of_damage_awakenings=[]
        
        #Converts string of responses into integers so that they may be operated on in the next step
        for amount in int_change_list:
            int_conversion = int(amount)
            list_of_damage_awakenings.append(int_conversion)
            
        #If length of the list is sufficient, the values will be used and multiplied together
        if len(list_of_damage_awakenings)==9:
        
            #Each individual multiplier is stored in a variable and will be used in the total multiplier
            tpa_multiplier = 1.5**(list_of_damage_awakenings[0])
    
            the_7c_multiplier = 2**(list_of_damage_awakenings[1])
    
            the_10c_multiplier = 5**(list_of_damage_awakenings[2])
    
            row_enhance_multiplier = 1+.1*(list_of_damage_awakenings[3])
    
            the_80_or_more_multiplier = 1.5**(list_of_damage_awakenings[4])
    
            the_50_or_less_multiplier = 2**(list_of_damage_awakenings[5])
    
            l_attack_multiplier = 1.5**(list_of_damage_awakenings[6])
    
            vdp_multiplier = 2.5**(list_of_damage_awakenings[7])
    
            sfua_multiplier = 2**(list_of_damage_awakenings[8])
    
        
            total_awakening_multiplier = tpa_multiplier* \
            the_7c_multiplier* \
            the_10c_multiplier* \
            row_enhance_multiplier* \
            the_80_or_more_multiplier* \
            the_50_or_less_multiplier* \
            l_attack_multiplier* \
            vdp_multiplier* \
            sfua_multiplier
    
            print('Your total multiplier from your monster\'s damage awakenings is '+ str(total_awakening_multiplier))
    
            return total_awakening_multiplier

        else: 
        
            print('Please enter a valid amount of values')
            
            total_awakening_multiplier=1
            
            return total_awakening_multiplier
            
    else:
        
        print('Please enter the values correctly')
        
        total_awakening_multiplier = 1
            
        return total_awakening_multiplier
    
    
      
def damage_enhancing_skills(damage_skill_multiplier):
    """Takes integer number that represents the multiplier of the damage/leader skill, if
    an integer is not provided, such as if the user inputs 'no', then the default
    multiplier will be 1x.
    
    Parameters
    ---------- 
    damage_skill_multiplier: string
        User inputted string that will be converted into int so that its value may be returned
    
    Returns
    -------
    total_damage_skill_multiplier: integer
        The int that results from converting the user inputted string
        
    """
    
    #Checks if the user input is able to become an int, so that it may be returned as a value
    if damage_skill_multiplier.isdigit():
        
        total_damage_skill_multiplier = int(damage_skill_multiplier)
        
        print('Your damage multiplier is ' + damage_skill_multiplier)
        
    else:
        
        total_damage_skill_multiplier = 1
        
        print('Your damage multiplier is 1')
        
    return total_damage_skill_multiplier



def total_attack_damage(baseattack, combomultiplier, damageawakenings, enhanceskills, leaderskills):
    
    """Takes the total amount of multipliers and multiplies them all together.
    
    Parameters
    ----------
    baseattack: integer or float
        The int or float that is returned from the card_identity() function
    
    combomultiplier: integer or float
        The int or float that is returned from the combo_multiplier() function
        
    damageawakenings: integer or float
        The int or float that is returned from the damage_awakenings() function
        
    enhanceskills: integer or float
        The int or float that is returned from the damage_enhancing_skills() function
        
    leaderskills: integer or float
        The int or float that is returned from the damage_enhancing_skills() function
    
    Returns
    -------
    total_damage: integer or float
        The int or float that results from multiplying all the above values together
        
    """
    
    #Multiplies all the total multipliers to the base attack so that it may be displayed later
    total_damage = baseattack*combomultiplier*damageawakenings*enhanceskills*leaderskills
    
    #Checks to see if the total damage is valid so that it may be shown to the user
    if total_damage != 0:
        
        print('Your monster\'s total damage output will be ' + str(total_damage))
        
    else:
        
        print('Are you sure you got your numbers right?')
        
    return total_damage
            