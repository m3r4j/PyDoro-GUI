# Libraries

from tkinter import *
import webbrowser
from PIL import Image, ImageTk
from pygame import mixer


# Proccess:
'''
25
5
25
5
25
5
25
15
'''


# Github
github_url = 'https://github.com/m3r4j'

# Time periods (minutes)
work_time = 25
break_time = 5
last_break_time = 15
ticks = 4
sets = 1
current_interval = None
last_interval = None
paused_time = None

# Variables for timer
starting_minutes = work_time
seconds = 0

# Booleans
paused = False

# A variable to see the amount of clicks on the button 'Start'
amount_of_clicks = 0

# Create the window
root = Tk()
root.title('PyDoro')
root.resizable(0,0)


# This function will display the options
def display_options():
	button_start = Button(root, text='Start', font=(None,20), fg='yellow', command=start)
	button_start.grid(row=0, column=0)

	button_pause = Button(root, text='Pause', font=(None,20), fg='yellow', command=pause)
	button_pause.grid(row=0, column=1)

	button_reset = Button(root, text='Reset', font=(None,20), fg='yellow', command=reset)
	button_reset.grid(row=0, column=2)

	button_reset_all = Button(root, text='Reset All', font=(None,20), fg='yellow', command=reset_all)
	button_reset_all.grid(row=0, column=3)

	button_exit = Button(root, text='Exit', font=(None,20), fg='yellow', command=root.destroy)
	button_exit.grid(row=0, column=4)



# Make a function which resets the time only and the ticks
def reset():
	global current_interval
	global starting_minutes 
	global ticks
	global seconds

	seconds = 0
	add_ticks()

	current_interval = work_time
	ticks = 4
	starting_minutes = 25#s

	timer_label.configure(text=f'{starting_minutes}min {seconds}s remaining')




# A function which resets the time and ticks and sets
def reset_all():
	global sets

	# normal rest
	reset()

	# remove sets
	set_1.place_forget()
	set_2.place_forget()
	set_3.place_forget()
	set_4.place_forget()
	set_5.place_forget()
	set_6.place_forget()

	# assign the value of sets back to "1"
	sets = 1


# Opens to my github
def open_to_github():
	webbrowser.open(github_url)


# This function will display the version number
def display_version():
	version_label = Label(root, text='v1.0', fg='blue', font=(None, 20))
	version_label.grid(row=0, column=5)

# Notify the user with a quick sound
def make_sound():
	mixer.init()
	mixer.music.load('notify.mp3')
	mixer.music.play()


# A function to display the timer
def display_timer():
	global seconds
	global starting_minutes
	global ticks
	global current_interval
	global last_interval
	global paused_time
	global paused

	if paused:
		return

	if starting_minutes == 0 and seconds == 0:
		make_sound()

		if current_interval == work_time:
			if ticks == 4:
				tick_4.place_forget()
				ticks -= 1

			elif ticks == 3:
				tick_3.place_forget()
				ticks -= 1

			elif ticks == 2:
				tick_2.place_forget()
				ticks -= 1

			elif ticks == 1:
				tick_1.place_forget()
				ticks -= 1

			elif ticks == 0:
				add_ticks()
				add_set()


				current_interval = break_time
				last_interval = None
				ticks = 4



		# Intervals
		if current_interval == work_time and last_interval == last_break_time:
			current_interval = work_time

		elif current_interval == work_time:
			current_interval = break_time

		elif current_interval == break_time:
			current_interval = work_time

		starting_minutes = current_interval

		# Last interval
		if ticks == 0:
			starting_minutes = last_break_time
			last_interval = starting_minutes
			current_interval = work_time

		
		paused_time = current_interval
		pause()

	if seconds == 0:
		starting_minutes -= 1
		seconds = 60

	seconds -= 1

	timer_label.configure(text=f'{starting_minutes}min {seconds}s remaining')
	root.after(1000, display_timer)

# Starting the timer
def start():
	global timer_label
	global paused
	global current_interval
	global amount_of_clicks

	amount_of_clicks += 1

	if amount_of_clicks == 1:
		if paused:
			current_interval = paused_time
		else:
			current_interval = work_time

		paused = False 
		start_label.place_forget() # Forget the label
		
		# Put the timer onto the screen
		timer_label = Label(root, text='', fg='cyan', font=('Courier', 25))
		timer_label.place(x=100, y=100)

		display_timer()




# A function that pauses the timer
def pause():
	global paused
	global amount_of_clicks

	amount_of_clicks = 0
	paused = True

# main
def main():
	display_options()
	display_version()


# Main function
main()

# Display the tomato image
tomato_image = ImageTk.PhotoImage(Image.open('tomato.png'))
tomato_label = Label(image=tomato_image)
tomato_label.grid(row=1, column=5)

# Make a start label
start_label = Label(root, text='Press [Start]', fg='cyan', font=('Courier', 25))
start_label.place(x=100, y=100)


# Put the ticks onto the screen
tick_image = Image.open('apple.png')
tick_image = tick_image.resize((50,50), Image.ANTIALIAS)
tick_image = ImageTk.PhotoImage(tick_image)

tick_1 = Label(image=tick_image)
tick_2 = Label(image=tick_image)
tick_3 = Label(image=tick_image)
tick_4 = Label(image=tick_image)

# A function to add the 4 ticks onto the screen
def add_ticks():
	tick_1.place(x=100,y=140)
	tick_2.place(x=160,y=140)
	tick_3.place(x=220,y=140)
	tick_4.place(x=280,y=140)

add_ticks()

# Create the sets
set_image = Image.open('golden_apple.png')
set_image = set_image.resize((50,50), Image.ANTIALIAS)
set_image = ImageTk.PhotoImage(set_image)

# Create 10 sets
set_1 = Label(image=set_image)
set_2 = Label(image=set_image)
set_3 = Label(image=set_image)
set_4 = Label(image=set_image)
set_5 = Label(image=set_image)
set_6 = Label(image=set_image)

# Add the sets

def add_set():
	global sets

	if sets == 1:
		set_1.place(x=100, y=195)

	elif sets == 2:
		set_2.place(x=160, y=195)

	elif sets == 3:
		set_3.place(x=220, y=195)

	elif sets == 4:
		set_4.place(x=280, y=195)

	elif sets == 5:
		set_5.place(x=340, y=195)

	elif sets == 6:
		set_6.place(x=400, y=195)

	else:
		reset_all()


	sets += 1

	
# Ways to forget positioning systems:

# label.place_forget()  
# label.grid_forget()
# label.pack_forget()

# Run the mainloop
root.mainloop()