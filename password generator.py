import random

charset_lower_case = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
charset_upper_case = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
charset_special_characters = ["!","£","$","%","*","#"]
charset_numbers = ["1","2","3","4","5","6","7","8","9","0"]
def password(charset_lower_case,charset_upper_case,charset_special_characters):
    
    
        lower_case1 = random.choice(charset_lower_case)
        upper_case1 = random.choice(charset_upper_case)
        special_character1 = random.choice(charset_special_characters)
        numbers1 = random.choice(charset_numbers)
    
        password = []
        password.append(lower_case1)
        password.append(upper_case1)
        password.append(special_character1)
        password.append(numbers1)
        

        lower_case2 = random.choice(charset_lower_case)
        upper_case2 = random.choice(charset_upper_case)
        special_character2 = random.choice(charset_special_characters)
        numbers2 = random.choice(charset_numbers)
    
        
        password.append(lower_case2)
        password.append(upper_case2)
        password.append(special_character2)
        password.append(numbers2)

        lower_case3 = random.choice(charset_lower_case)
        upper_case3 = random.choice(charset_upper_case)
        special_character3 = random.choice(charset_special_characters)
        numbers3 = random.choice(charset_numbers)
        
        password.append(lower_case3)
        password.append(upper_case3)
        password.append(special_character3)
        password.append(numbers3)
        
        
        return password


print("Password generator, your new password is: ")
print(password(charset_lower_case,charset_upper_case,charset_special_characters))