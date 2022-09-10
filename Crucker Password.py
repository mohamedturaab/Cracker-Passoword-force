# import  random
# import pyautogui
#
# character = "0123456789abcdefghijklmnopqrstuvwxyz"
# character_list = list(character)
# passowrd = pyautogui.password("Enter Password Here:")
# guess_password = ''
# while (guess_password!= passowrd):
# 	guess_password = random.choices(character_list,k=len(passowrd))
# 	print(">>>>>"+str(guess_password)+"<<<<<")
# 	if(guess_password ==list(passowrd)):
# 		print("Your Password is:" + "" .join(guess_password))
# 		break

# import  random
# import pyautogui
#
# character =  "0123456789abcdefghiklmnoqprstuvwxyz"
# character_list = list(character)
# password = pyautogui.password("Enter Password Here:")
# guess_Password = ""
# while (guess_Password!=password):
# 	guess_Password = random.choices(character_list,k=len(password))
# 	print(">>>>>"+str(guess_Password)+"<<<<<")
# 	if(guess_Password == list(password)):
# 		print("Your Password is:" + "" .join(guess_Password))
# 		break

# import  random
# import pyautogui
# character = "0123456789abdefghiklmnopqrstuvwxyz"
# character_list = list(character)
# password = pyautogui.password("Enter A Password Here:")
# guess_password = ""
# while (guess_password != password):
# 	guess_password = random.choices(character_list,k=len(password))
# 	print(">>>>>"+str(guess_password)+"<<<<<")
# 	if(guess_password == list(password)):
# 		print("Your Password Is:" + "" .join(guess_password))
# 		break

import  random
import pyautogui
character = "0123456789abdefghiklmnopqrstuvwxyz"
character_list = list(character)
password = pyautogui.password("Enter A Password Here:")
guess_password = ""
while (guess_password!= password):
	guess_password = random.choices(character_list,k=len(password))
	print(">>>>>"+str(guess_password)+"<<<<<")
	if(guess_password ==len(password)):
		print("Your Password is:" + "" .join(guess_password))
		break


