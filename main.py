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
	a = 4.0 * (x/size[0] - 0.5)
	b = 3.0 * (y/size[1] - 0.5)
	# Starting z
	z = [0, 0]
	z_n = [0, 0]

	# Formula: z_{n+1} = z_n^2 + (a+ib)

	n = 0
	for n in range(0, 32):
		# Squaring the complex number
		z_n[0] = z[0]**2 - z[1]**2
		z_n[1] = 2.0 * z[0] * z[1]
		z = z_n

		# Adding a+jb
		z[0] += a
		z[1] += b
		if z[0]**2 + z[1]**2 > 4:
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
