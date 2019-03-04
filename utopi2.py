
import pyautogui
import time
import csv

with open('sample.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter =',')

	for row in readCSV:
            try:
                        time.sleep(30)
                        pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down'])
                        time.sleep(15)
                        pyautogui.click(pyautogui.locateCenterOnScreen('writepost.png'))
                        time.sleep(15)
                        pyautogui.click(pyautogui.locateCenterOnScreen('whats.png'))
                        time.sleep(15)
                        pyautogui.move(100,50)
                        pyautogui.typewrite(str(row[0]))
                        pyautogui.press('enter')
                        pyautogui.typewrite(str(row[1]))
                        pyautogui.press('enter')
                        pyautogui.typewrite('Email :'+str(row[4]+' .'))
                        pyautogui.press('enter')
                        time.sleep(15)
                        pyautogui.click(pyautogui.locateCenterOnScreen('post.png'))
                        time.sleep(5)
                        pyautogui.press('f6')
                        pyautogui.typewrite("https://m.facebook.com/groups/jobs4usuae/")
                        pyautogui.press('enter')
                        time.sleep(30)
                        pyautogui.press(['up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up'])
                        print(str(row[0]))
            except:
            			pyautogui.press('f6')
            			pyautogui.typewrite("https://m.facebook.com/groups/jobs4usuae/")
            			pyautogui.press('enter')
            			time.sleep(5)
            			pyautogui.press(['up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up'])
		

	

