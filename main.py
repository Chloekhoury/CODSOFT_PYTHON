import tkinter as tk
from tkinter import ttk
import random
from PIL import ImageTk, Image
import pygame
    
game_size='1000x650'

# load the screen
root = tk.Tk()
root.geometry(game_size)
root.title('Rock, Paper, Scissors')
root.resizable(width=False, height=False)

# Load the background image
# Image.LANCZOS is a resampling filter used in the Pillow library when resizing images. 
# It helps to improve the quality of an image when it's being downscaled
background_image = Image.open("pictures/background_menu.png")  # Open the image file
background_image = background_image.resize((1000, 650), Image.LANCZOS)  # Resize the image to fit the window

# Convert the image to a PhotoImage
bg_image = ImageTk.PhotoImage(background_image)

# Create a label to display the background image
background_label = tk.Label(root, image=bg_image)
background_label.place(relwidth=1, relheight=1)  # Place it to cover the entire window


# Initialize the mixer for playing sound
pygame.mixer.init()

# Load the background music
pygame.mixer.music.load("music.wav")


# Function to toggle music on/off
def toggle_music():
    if music_var.get() == 1:
        # Play the background music indefinitely (-1 means loop forever)
        pygame.mixer.music.play(loops=-1)

    else:
        pygame.mixer.music.stop()
        
        
# Add a label for the check button
music_label = tk.Label(root, text="MUSIC:", font=('Segoe Script', 16,'bold'), bg="black", fg='#FF10F0',borderwidth=0)
music_label.place(rely=0.7, relx=0.071)

# Create a check button to start/stop music
music_var = tk.IntVar(value=1)  # Start with music ON
music_checkbutton = tk.Checkbutton(
    root, 
    variable=music_var, 
    command=toggle_music, 
    font=('Segoe Script', 18),  # Larger font for a bigger button
    bg='black',  # Black background
    fg='white',  # White text color
    selectcolor='black',  # Black color when selected
    highlightthickness=0,  # No border when clicked
    borderwidth=0,  # No border around the button
    padx=10,  # Add padding to increase size
    pady=5
)
music_checkbutton.place(rely=0.684,relx=0.195)

# Play the background music indefinitely (-1 means loop forever)
pygame.mixer.music.play(loops=-1)


# functions to have effects when the mouse is on the button
def on_enter(e):
    # Change the button's appearance when the mouse hovers over it
    #new_game_button.config(bg='purple', fg=inner_purple)
    e.widget.config(bg='#1b001b', relief='raised')  # Dark purple background, raised effect

def on_leave(e):
    # Revert to the original appearance when the mouse leaves the button
    e.widget.config(bg='black', fg=inner_purple)


# Or we use tk.Button using font=( ) without style=
#new_game_button = tk.Button(root, text='NEW GAME', style='main.TButton')
outer_purple = '#9400D3'  # Darker purple for outer text
inner_purple = '#FF10F0'  # Lighter purple for inner text
new_game_button = tk.Button(root, text='NEW GAME', 
                            font=('Segoe Script', 18, 'bold'),
                            fg=inner_purple,   # Light purple for text color
                            bg='black',        # Black background
                            activebackground='black',  # Black background when clicked
                            borderwidth=0,     # No border width
                            highlightthickness=0,  # No highlight thickness
                            activeforeground=outer_purple)  # Outer purple when clicked



# Bind the hover event
new_game_button.bind("<Enter>", on_enter)
new_game_button.bind("<Leave>", on_leave)

new_game_button.place(relheight=0.1, relwidth=0.2, rely=0.6, relx=0.05)

def game_start():

    pl_score = 0
    pc_score = 0
    # pc_rock = ImageTk.PhotoImage(Image.open("./pictures/rockpc.png")) # or pictures/...
    # or
    pc_rock = tk.PhotoImage(file="pictures/hands/rockpc.png")
    pc_paper = ImageTk.PhotoImage(Image.open("./pictures/hands/paperpc.png"))
    pc_scissors = ImageTk.PhotoImage(Image.open("./pictures/hands/scissorspc.png"))
    pl_rock = ImageTk.PhotoImage(Image.open("./pictures/hands/rockplayer.png"))
    pl_paper = ImageTk.PhotoImage(Image.open("./pictures/hands/paperplayer.png"))
    pl_scissors = ImageTk.PhotoImage(Image.open("./pictures/hands/scissorsplayer.png"))
    q_mark = ImageTk.PhotoImage(Image.open("./pictures/qmark.png"))
    rock_i = ImageTk.PhotoImage(Image.open("./pictures/icons/rockicon.png"))
    paper_i = ImageTk.PhotoImage(Image.open("./pictures/icons/papericon.png"))
    scissors_i = ImageTk.PhotoImage(Image.open("./pictures/icons/scissorsicon.png"))

    # This method hides the main window (root) without destroying it. 
    # The window is still there in memory but isn't visible on the screen.
    root.withdraw()
    pc_pick=0
    pl_pick=0
    rounds=0
    
    # This creates a new window (a child window) that is associated with the main window (root). 
    gamepage = tk.Toplevel(root)
    gamepage.geometry(game_size)
    gamepage.resizable(width=False, height=False)
    
    # f allows dynamic formatting, so you can update the score in the title as the game progresses.
    gamepage.title(f'Score 0-0')
    
    background_image2 = Image.open("pictures/black.png")  # Open the image file
    background_image2 = background_image2.resize((1000, 650), Image.LANCZOS)  # Resize the image to fit the window

    # Convert the image to a PhotoImage
    bg_image2 = ImageTk.PhotoImage(background_image2)

    # Create a label to display the background image
    background_label2 = tk.Label(gamepage, image=bg_image2)
    background_label2.place(relwidth=1, relheight=1)  # Place it to cover the entire window

    # Keep a reference to the image to prevent it from being garbage collected
    background_label2.image = bg_image2
    
    score_title = ttk.Label(gamepage, text='Score', font=('Segoe Script', 32), background='black',foreground='#FF10F0')
    #  dynamically inserts the player and computer scores into the label.
    score_label = ttk.Label(gamepage, text=f'{pl_score} : {pc_score}', font=('Segoe Script', 24, 'bold'), background='black',foreground='#FF10F0')
    result_label = ttk.Label(gamepage, text=' ', font=('Segoe Script', 32), background='black',foreground='#FF10F0')
    pc_image = ttk.Label(gamepage,background='black')
    pl_image = ttk.Label(gamepage,background='black')
    pc_image.configure(image=q_mark)
    pc_image.image=q_mark
    pl_image.configure(image=q_mark)
    pl_image.image=q_mark
    
    pc_title = ttk.Label(gamepage, text='PC:', font=('Segoe Script', 24, 'bold'), background='black',foreground='#FF10F0')
    pl_title = ttk.Label(gamepage, text='YOU:', font=('Segoe Script', 24, 'bold'), background='black',foreground='#FF10F0')
    
    image_width = paper_i.width()
    image_height = paper_i.height()
    rock_button = tk.Button(gamepage, image=rock_i,bg='black',borderwidth=0.5, highlightthickness=0.4,  width=image_width, height=image_height)
    rock_button.image=rock_i
    paper_button = tk.Button(gamepage, image=paper_i,bg='black',borderwidth=0.5, highlightthickness=0, width=image_width, height=image_height)
    paper_button.image=paper_i
    scissors_button = tk.Button(gamepage, image=scissors_i,bg='black',borderwidth=0.5, highlightthickness=0, width=image_width, height=image_height)
    scissors_button.image=scissors_i
    
    back_button = tk.Button(gamepage, text='MENU', 
                            font=('Segoe Script', 16, 'bold'),
                            fg=inner_purple,   # Light purple for text color
                            bg='black',        # Black background
                            activebackground='black',  # Black background when clicked
                            borderwidth=0,     # No border width
                            highlightthickness=0,  # No highlight thickness
                            activeforeground=outer_purple)  # Outer purple when clicked
    
    playagain_button = tk.Button(gamepage, text='PLAY AGAIN', 
                            font=('Segoe Script', 20, 'bold'),
                            fg=inner_purple,   # Light purple for text color
                            bg='black',        # Black background
                            activebackground='black',  # Black background when clicked
                            borderwidth=0,     # No border width
                            highlightthickness=0,  # No highlight thickness
                            activeforeground=outer_purple)  # Outer purple when clicked
    
    close_button = tk.Button(gamepage, text='Back to menu', 
                            font=('Segoe Script', 13, 'bold'),
                            fg=inner_purple,   # Light purple for text color
                            bg='black',        # Black background
                            borderwidth=0,     # No border width
                            highlightthickness=0,  # No highlight thickness
                            activebackground='black',  # Black background when clicked
                            activeforeground=outer_purple)  # Outer purple when clicked
    
    
    
    # Bind the hover event
    back_button.bind("<Enter>", on_enter)
    back_button.bind("<Leave>", on_leave)
    
     # Bind the hover event
    playagain_button.bind("<Enter>", on_enter)
    playagain_button.bind("<Leave>", on_leave)
    
     # Bind the hover event
    close_button.bind("<Enter>", on_enter)
    close_button.bind("<Leave>", on_leave)
    
    overall_label = ttk.Label(gamepage, font = ('Segoe Script', 20))
    cur_label = ttk.Label(gamepage, text='ROUNDS PLAYED: 0', font=('Segoe Script', 16), background='black',foreground='#1F51FF')

    score_title.place(relx=0.46, rely=0.06)
    score_label.place(relx=0.477, rely=0.17)
    result_label.place(relx=0.402, rely=0.65)
    pc_image.place(relx=0.65, rely=0.3)
    pl_image.place(relx=0.09, rely=0.3)
    pc_title.place(relx=0.755, rely=0.21) 
    pl_title.place(relx=0.18, rely=0.21)
    rock_button.place(relwidth=0.057, relheight=0.1, relx=0.1, rely=0.8)
    paper_button.place(relwidth=0.057, relheight=0.1, relx=0.190, rely=0.8)
    scissors_button.place(relwidth=0.057, relheight=0.1, relx=0.280, rely=0.8)
    close_button.place(relwidth=0.2, relheight=0.07, relx=0.72, rely=0.81)
    cur_label.place(relx=0.40, rely=0.01)

            
    gm=10 # the game finishes when someone reaches 10 



    def close_game():
        # Load the background music
        pygame.mixer.music.load("music.wav")

        # Play the background music indefinitely (-1 means loop forever)
        pygame.mixer.music.play(loops=-1)
        # This makes the hidden window root reappear.
        root.deiconify()
        gamepage.destroy()

    def play_again():

        gamepage.destroy()
        # Load the background music
        pygame.mixer.music.load("music.wav")

        # Play the background music indefinitely (-1 means loop forever)
        pygame.mixer.music.play(loops=-1)
        game_start()

    def game_over(score_a, score_b):
        # to hide objects and we can replace it again using place()
        rock_button.place_forget()
        paper_button.place_forget()
        scissors_button.place_forget()
        result_label.place_forget()
        close_button.place_forget()

        # Initialize Pygame for sound
        pygame.mixer.init()

        def animate_win_image():
            # Load the image
            win_image = Image.open("pictures/win_optimized.png")
           # win_image = win_image.resize((200, 100), Image.ANTIALIAS)
            win_photo = ImageTk.PhotoImage(win_image)

            # Create a label for the image
            win_label = tk.Label(gamepage, image=win_photo, bg='black')
            win_label.image = win_photo  # Keep a reference to the image

            # Start the image above the screen
            win_label.place(relx=0.36, y=50)  # Starting position

            def move_image():
                current_y = win_label.winfo_y()
                if current_y < 200:  # Target position (middle of the screen)
                    win_label.place(y=current_y + 10)  # Move down 5 pixels at a time
                    gamepage.after(10, move_image)  # Repeat every 10 milliseconds
                else:
                    # After reaching the middle, wait for 2 seconds and then hide the image
                    gamepage.after(6000, win_label.place_forget)

            move_image()

        def on_win():
            pygame.mixer.music.load("Winner.ogg")
            pygame.mixer.music.play()
            animate_win_image()
            
        def on_lose():
            pygame.mixer.music.load("lose.wav")
            pygame.mixer.music.play()
            
            
        if score_a>score_b:
            overall_label['text'] = 'C o n g r a t u l a t i o n s,   y o u   w o n!'
            overall_label['background'] = 'black'
            overall_label['foreground'] = '#FF10F0'
            on_win()
        else:
            overall_label['text'] = 'B e t t e r   l u c k   n e x t   t i m e!  : )'
            overall_label['background'] = 'black'
            overall_label['foreground'] = '#FF10F0'
            on_lose()

        overall_label.place(relx=0.2, rely=0.82)
        back_button.place(relwidth=0.14, relheight=0.08, relx=0.43, rely=0.62)
        playagain_button.place(relwidth=0.22, relheight=0.12, relx=0.39, rely=0.46)


    def game_rock(): 
        # The nonlocal keyword is used to indicate that the variables exist in an enclosing scope 
        # (likely in an outer function) and should be modified within this function.
        nonlocal pl_score, pc_score, pl_pick, pc_pick, rounds

        rounds+=1
        pl_pick = 0
        pl_image.configure(image=pl_rock)
        pl_image.image=pl_rock
        pc_pick = random.randint(0, 2)
            
        if pc_pick==0:

            pc_image.configure(image=pc_rock)
            pc_image.image=pc_rock
            result_label['text']='Game tied'

        elif pc_pick==1:

            pc_image.configure(image=pc_paper)
            pc_image.image=pc_paper
            result_label['text']='You lost!'
            pc_score+=1

        else:

            pc_image.configure(image=pc_scissors)
            pc_image.image=pc_scissors
            result_label['text']='You won!'
            pl_score+=1

        score_label['text'] = f'{pl_score} : {pc_score}'
        cur_label['text'] = f'ROUNDS PLAYED: {rounds}'
        gamepage.title(f'Score {pl_score}-{pc_score}')

        if pl_score==gm or pc_score==gm:

            game_over(pl_score, pc_score)

    def game_paper(): 

        nonlocal pl_score, pc_score, pl_pick, pc_pick, rounds

        rounds+=1
        pl_pick = 0
        pl_image.configure(image=pl_paper)
        pl_image.image=pl_paper
        pc_pick = random.randint(0, 2)
            
        if pc_pick==1:

            pc_image.configure(image=pc_paper)
            pc_image.image=pc_paper
            result_label['text']='Game tied'

        elif pc_pick==2:

            pc_image.configure(image=pc_scissors)
            pc_image.image=pc_scissors
            result_label['text']='You lost!'
            pc_score+=1

        else:

            pc_image.configure(image=pc_rock)
            pc_image.image=pc_rock
            result_label['text']='You won!'
            pl_score+=1

        score_label['text'] = f'{pl_score} : {pc_score}'
        cur_label['text'] = f'ROUNDS PLAYED: {rounds}'
        gamepage.title(f'Score {pl_score}-{pc_score}')

        if pl_score==gm or pc_score==gm:

            game_over(pl_score, pc_score)


    def game_scissors(): 
        
        nonlocal pl_score, pc_score, pl_pick, pc_pick, rounds

        rounds+=1
        pl_pick = 0
        pl_image.configure(image=pl_scissors)
        pl_image.image=pl_scissors
        pc_pick = random.randint(0, 2)
                
        if pc_pick==2:

            pc_image.configure(image=pc_scissors)
            pc_image.image=pc_scissors
            result_label['text']='Game tied'

        elif pc_pick==0:

            pc_image.configure(image=pc_rock)
            pc_image.image=pc_rock
            result_label['text']='You lost!'
            pc_score+=1

        else:

            pc_image.configure(image=pc_paper)
            pc_image.image=pc_paper
            result_label['text']='You won!'
            pl_score+=1

        score_label['text'] = f'{pl_score} : {pc_score}'
        cur_label['text'] = f'ROUNDS PLAYED: {rounds}'
        gamepage.title(f'Score {pl_score}-{pc_score}')

        if pl_score==gm or pc_score==gm:

            game_over(pl_score, pc_score)


    rock_button['command'] = lambda: game_rock()
    paper_button['command'] = lambda: game_paper()
    scissors_button['command'] = lambda: game_scissors()
    close_button['command'] = lambda: close_game()
    playagain_button['command'] = lambda: play_again()
    back_button['command'] = lambda: close_game()

new_game_button['command'] = lambda: game_start()

# command attribute of a button is used to specify the function that should be called when the button is clicked.
# The use of lambda here allows you to delay the execution of game_start() until the button is actually clicked.

root.mainloop()