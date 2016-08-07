### Author: Max Zangs
### Description: Computes simple Mandelbrot set
### Category: Random
### License: MIT
### Appname: Mandelbrot
### Built-in: no

import pyb
import ugfx
import buttons

ugfx.init()
buttons.init()
buttons.disable_menu_reset()

playing = 1
size = [320.0, 240.0]

def get_color(val):
	return ((val & 0x1f) << 11) | ((val & 0x1f) << 6) | (val & 0x1f)

def m(x, y):
	# Normalised coordinates
	a = 4.0 * (x/size[0] - 0.66)
	b = 3.0 * (y/size[1] - 0.50)

	z = 0
	for n in range(32):
		z = z**2 + a + b*1j
		if abs(z) > 4:
			break
	return 31-n

ugfx.clear(ugfx.GREY)
ugfx.text(30, int(size[1])-30, 'Computing...', ugfx.BLACK)

for y in range(size[1]):
	for x in range(size[0]):
		c = m(x, y)
		ugfx.area(x, y, 1, 1, get_color(c))

	if buttons.is_triggered("BTN_B"):
		break

while playing:
	ugfx.text(30, int(size[1])-30, 'Mandelbrot done :)', ugfx.WHITE)

	while True:
		# pyb.wfi() # Some low power stuff
		if buttons.is_triggered("BTN_A"):
			break

		if buttons.is_triggered("BTN_MENU"):
			playing = 0 #pyb.hard_reset()
			break
