import autopy
import time
import pyHook
import sys
import pythoncom
import os
import threading

def click_common(x, y):
	autopy.mouse.smooth_move(x,y)
	autopy.mouse.click(1)


def click_seal(x = 1020, y = 700):
	print x, y
	autopy.mouse.move(x, y)
	autopy.mouse.click(1)

def click_prepare(x = 1780, y = 650):
	print x, y
	autopy.mouse.move(x, y)
	autopy.mouse.click(1)

def click_in(x = 1680, y = 400):
	print x, y
	autopy.mouse.move(x, y)
	autopy.mouse.click(1)

def click_team(x = 1080, y = 750):
	print x, y
	autopy.mouse.move(x, y)
	autopy.mouse.click(1)

def click_begin(x = 1691, y = 680):
	print x, y
	autopy.mouse.move(x, y)
	autopy.mouse.click(1)

def onKeyboardEvent(event):
	print str(event.Key)
	if str(event.Key) == "Return":
		os._exit(0)
	return True

def hook():
	hm = pyHook.HookManager()
	hm.KeyDown = onKeyboardEvent
	hm.HookKeyboard()
	pythoncom.PumpMessages()

def click_main():
	while True:
		click_seal()
		click_in()
		click_prepare()
		click_team()
		time.sleep(0.5)

def tupo(x, y):
	w = 300
	h = 100
	for i in range(0, 3):
		for j in range(0, 3):
			w_x = x + i * w
			w_y = y + j * h
			click_common(w_x, w_y)

def yuhun_friend():
	pos = [(1780, 650), (1691, 710), (1691, 710), (1420, 610), (1691, 710)]
	while True:
		for item in pos:
			click_common(item[0], item[1])


def end_shua():
	time.sleep(1*4000)
	os._exit(0)


threads = []
t1 = threading.Thread(target=hook, args=())
t2 = threading.Thread(target=click_main, args=())
t3 = threading.Thread(target=end_shua, args=())
t4 = threading.Thread(target=yuhun_friend, args=())
threads.append(t1)
# threads.append(t2)
# threads.append(t3)
threads.append(t4)

if __name__ == '__main__':
	for i in threads:
		# t.setDaemon(True)
		i.start()
	# click_common(1691, 710)
	# yuhun_friend()



# autopy.mouse.smooth_move(1000,500)
# # autopy.mouse.smooth_move(1680,410)
# autopy.mouse.click(1)
# # time.sleep(5)
# autopy.mouse.toggle(True)
# # time.sleep(1)
# autopy.mouse.toggle(False)

# from pymouse import PyMouse
# import time
# mouse = PyMouse()
# print mouse.position()
# mouse.move(1000, 500)
# mouse.click(1000, 500, 2)
