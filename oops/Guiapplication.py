import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import random
import webbrowser
from datetime import datetime

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Desktop App")
        self.root.geometry("800x600")
        self.root.minsize(600, 400)
        
        # Configure style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.theme_use('clam')
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        self.style.configure('TButton', font=('Arial', 10))
        self.style.configure('Header.TLabel', font=('Arial', 16, 'bold'))
        self.colors = {
            'primary': '#4a6fa5',
            'secondary': '#166088',
            'accent': '#4fc3f7',
            'text': '#ffffff',
            'background': '#f0f0f0',
            'success': '#4caf50',
            'warning': '#ff9800',
            'error': '#f44336'
        }
        
        # Create main container
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.style.configure('TFrame', background=self.colors['background'])
        self.style.configure('TLabel', background=self.colors['background'], font=('Arial', 10))
        self.style.configure('TButton', font=('Arial', 10), background=self.colors['primary'],
                           foreground=self.colors['text'])
        self.style.map('TButton', 
                     background=[('active', self.colors['secondary']), ('pressed', self.colors['accent'])])
        self.style.configure('Header.TLabel', font=('Arial', 16, 'bold'), 
                           background=self.colors['primary'], foreground=self.colors['text'])
        
        # Header
        self.header_frame = ttk.Frame(self.main_frame)
        self.header_frame.pack(fill=tk.X, padx=10, pady=10)
        self.header_frame = ttk.Frame(self.main_frame, style='TFrame')
        self.header_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.header_label = ttk.Label(
            self.header_frame, 
            text="",  # Start empty for animation
            style='Header.TLabel'
        )
        

        self.header_label.pack(side=tk.LEFT)
        
        self.time_label = ttk.Label(
            self.header_frame, 
            text=self.get_current_time()
        )
        self.time_label.pack(side=tk.RIGHT)
        
        # Content area with notebook (tabs)
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        
        # Create tabs
        self.create_home_tab()
        self.create_calculator_tab()
        self.create_text_editor_tab()
        self.create_games_tab()
        self.create_settings_tab()
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        
        self.status_bar = ttk.Label(
            self.main_frame, 
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        self.status_bar.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        # Update time every second
        self.update_time()
        
    def get_current_time(self):
        return datetime.now().strftime("%H:%M:%S %d/%m/%Y")
    
    def update_time(self):
        self.time_label.config(text=self.get_current_time())
        self.root.after(1000, self.update_time)
    
    def create_home_tab(self):
        self.home_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.home_tab, text="Home")
        
        # Welcome message
        welcome_frame = ttk.Frame(self.home_tab)
        welcome_frame.pack(fill=tk.X, padx=10, pady=10)
        
        welcome_label = ttk.Label(
            welcome_frame, 
            text="Welcome to the Interactive Desktop App!\nExplore the different tabs to use various features.",
            justify=tk.CENTER
        )
        welcome_label.pack()
        
        # Quick actions frame
        actions_frame = ttk.LabelFrame(self.home_tab, text="Quick Actions")
        actions_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Action buttons
        button_data = [
            ("Open Calculator", self.show_calculator),
            ("Open Text Editor", self.show_text_editor),
            ("Play Game", self.show_games),
            ("Open Website", self.open_website),
            ("Show Info", self.show_info)
        ]
        
        for text, command in button_data:
            btn = ttk.Button(actions_frame, text=text, command=command)
            btn.pack(side=tk.LEFT, padx=5, pady=5, expand=True)
    
    def create_calculator_tab(self):
        self.calc_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.calc_tab, text="Calculator")
        
        # Calculator display
        self.calc_var = tk.StringVar()
        self.calc_var.set("0")
        
        calc_display = ttk.Entry(
            self.calc_tab,
            textvariable=self.calc_var,
            font=('Arial', 20),
            justify=tk.RIGHT,
            state='readonly'
        )
        calc_display.pack(fill=tk.X, padx=10, pady=10)
        
        # Calculator buttons
        buttons_frame = ttk.Frame(self.calc_tab)
        buttons_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', 'C', '+'),
            ('(', ')', '=', '⌫')
        ]
        
        for row in buttons:
            row_frame = ttk.Frame(buttons_frame)
            row_frame.pack(fill=tk.BOTH, expand=True)
            
            for btn_text in row:
                btn = ttk.Button(
                    row_frame, 
                    text=btn_text,
                    command=lambda t=btn_text: self.calc_button_click(t)
                )
                btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=2, pady=2)
    
    def calc_button_click(self, button_text):
        current = self.calc_var.get()
        
        if button_text == 'C':
            self.calc_var.set('0')
        elif button_text == '⌫':
            self.calc_var.set(current[:-1] if len(current) > 1 else '0')
        elif button_text == '=':
            try:
                result = eval(current)
                self.calc_var.set(str(result))
            except:
                self.calc_var.set('Error')
        else:
            if current == '0' or current == 'Error':
                self.calc_var.set(button_text)
            else:
                self.calc_var.set(current + button_text)
    
    def create_text_editor_tab(self):
        self.text_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.text_tab, text="Text Editor")
        
        # Text widget with scrollbar
        text_frame = ttk.Frame(self.text_tab)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.text_editor = tk.Text(
            text_frame,
            wrap=tk.WORD,
            font=('Arial', 12)
        )
        
        scrollbar = ttk.Scrollbar(text_frame, command=self.text_editor.yview)
        self.text_editor.config(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Editor buttons
        button_frame = ttk.Frame(self.text_tab)
        button_frame.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        ttk.Button(
            button_frame,
            text="Open File",
            command=self.open_file
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            button_frame,
            text="Save File",
            command=self.save_file
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            button_frame,
            text="Clear",
            command=self.clear_text
        ).pack(side=tk.LEFT, padx=5)
    
    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.text_editor.delete(1.0, tk.END)
                self.text_editor.insert(tk.END, content)
            self.status_var.set(f"Opened: {file_path}")
    
    def save_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text_editor.get(1.0, tk.END))
            self.status_var.set(f"Saved: {file_path}")
    
    def clear_text(self):
        self.text_editor.delete(1.0, tk.END)
    
    def create_games_tab(self):
        self.games_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.games_tab, text="Games")
        
        # Game selection
        game_frame = ttk.LabelFrame(self.games_tab, text="Select a Game")
        game_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        ttk.Button(
            game_frame,
            text="Guess the Number",
            command=self.play_guess_number,
            width=20
        ).pack(pady=10)
        
        ttk.Button(
            game_frame,
            text="Rock Paper Scissors",
            command=self.play_rps,
            width=20
        ).pack(pady=10)
    
    def play_guess_number(self):
        game_win = tk.Toplevel(self.root)
        game_win.title("Guess the Number")
        game_win.geometry("300x200")
        
        self.secret_number = random.randint(1, 100)
        self.guesses = 0
        
        ttk.Label(
            game_win,
            text="I'm thinking of a number between 1 and 100.\nCan you guess it?",
            justify=tk.CENTER
        ).pack(pady=10)
        
        self.guess_var = tk.StringVar()
        ttk.Entry(game_win, textvariable=self.guess_var).pack(pady=5)
        
        ttk.Button(
            game_win,
            text="Submit Guess",
            command=self.check_guess
        ).pack(pady=5)
        
        self.guess_result = ttk.Label(game_win, text="")
        self.guess_result.pack(pady=5)
    
    def check_guess(self):
        try:
            guess = int(self.guess_var.get())
            self.guesses += 1
            
            if guess < self.secret_number:
                self.guess_result.config(text="Too low! Try again.")
            elif guess > self.secret_number:
                self.guess_result.config(text="Too high! Try again.")
            else:
                self.guess_result.config(text=f"Correct! You guessed it in {self.guesses} tries.")
                self.guess_var.set("")
        except ValueError:
            self.guess_result.config(text="Please enter a valid number!")
    
    def play_rps(self):
        game_win = tk.Toplevel(self.root)
        game_win.title("Rock Paper Scissors")
        game_win.geometry("300x200")
        
        ttk.Label(
            game_win,
            text="Choose your move:",
            justify=tk.CENTER
        ).pack(pady=10)
        
        moves_frame = ttk.Frame(game_win)
        moves_frame.pack()
        
        self.rps_result = ttk.Label(game_win, text="", justify=tk.CENTER)
        self.rps_result.pack(pady=10)
        
        for move in ["Rock", "Paper", "Scissors"]:
            ttk.Button(
                moves_frame,
                text=move,
                command=lambda m=move: self.play_rps_round(m),
                width=10
            ).pack(side=tk.LEFT, padx=5)
    
    def play_rps_round(self, player_move):
        moves = ["Rock", "Paper", "Scissors"]
        computer_move = random.choice(moves)
        
        if player_move == computer_move:
            result = "It's a tie!"
        elif (player_move == "Rock" and computer_move == "Scissors") or \
             (player_move == "Paper" and computer_move == "Rock") or \
             (player_move == "Scissors" and computer_move == "Paper"):
            result = f"You win! {player_move} beats {computer_move}"
        else:
            result = f"You lose! {computer_move} beats {player_move}"
        
        self.rps_result.config(text=f"Computer chose {computer_move}\n{result}")
    
    def create_settings_tab(self):
        self.settings_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.settings_tab, text="Settings")
        
        # Theme selection
        theme_frame = ttk.LabelFrame(self.settings_tab, text="Theme")
        theme_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.theme_var = tk.StringVar(value='clam')
        
        for theme in ['clam', 'alt', 'default', 'classic']:
            ttk.Radiobutton(
                theme_frame,
                text=theme.capitalize(),
                variable=self.theme_var,
                value=theme,
                command=self.change_theme
            ).pack(side=tk.LEFT, padx=5)
    
    def change_theme(self):
        self.style.theme_use(self.theme_var.get())
    
    def show_calculator(self):
        self.notebook.select(self.calc_tab)
    
    def show_text_editor(self):
        self.notebook.select(self.text_tab)
    
    def show_games(self):
        self.notebook.select(self.games_tab)
    
    def open_website(self):
        webbrowser.open("https://www.google.com")
    
    def show_info(self):
        messagebox.showinfo(
            "About",
            "Interactive Desktop App\nVersion 1.0\nCreated with Python and Tkinter"
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()