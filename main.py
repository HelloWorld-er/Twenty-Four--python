import customtkinter
import fonts


class GameModeFrame(customtkinter.CTkFrame):
	def __init__(self, parent):
		# create frame
		super().__init__(parent)
		
		# initialize the grid manager
		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure(tuple(range(3)), weight=1)
		
		# define widgets
		game_mode_dict = {"Challenge": None, "Solver": None, "Duel": None}
		for game_mode in game_mode_dict.keys():
			game_mode_dict[game_mode] = customtkinter.CTkButton(self, text=f"{game_mode} Mode", font=fonts.get_game_mode_button(), fg_color=("DarkOrange2", "DarkOrange3"), hover_color=("DarkOrange3", "DarkOrange4"), border_width=2)
		
		# place widgets
		for i, game_mode in enumerate(game_mode_dict.keys()):
			game_mode_dict[game_mode].grid(row=i, column=0, sticky="ew", ipady=5, padx=5, pady=5)
		


class AsideBarFrame(customtkinter.CTkFrame):
	def __init__(self, parent, title, corner_radius=0):
		# create frame
		super().__init__(parent, corner_radius=corner_radius)
		self.title = title
		
		# initialize the grid manager
		self.grid_columnconfigure(0, weight=1)
		
		# define widgets
		self.title = customtkinter.CTkLabel(self, text=self.title, font=fonts.get_heading())
		self.introduction_button = customtkinter.CTkButton(self, text="Introduction", font=fonts.get_aside_bar_default(), corner_radius=6, border_width=2)
		self.navigation_frame = GameModeFrame(self)
		self.settings_button = customtkinter.CTkButton(self, text="Settings", font=fonts.get_aside_bar_default(), corner_radius=6, border_width=2)
		
		# place widgets
		self.title.grid(row=0, column=0, sticky="ew", ipadx=5, ipady=10, padx=10, pady=12)
		self.introduction_button.grid(row=1, column=0, sticky="ew", ipadx=5, ipady=10, padx=10, pady=10)
		self.navigation_frame.grid(row=2, column=0, sticky="ew", ipadx=5, ipady=10, padx=10, pady=10)
		self.settings_button.grid(row=3, column=0, sticky="ew", ipadx=5, ipady=10, padx=10, pady=10)


class App(customtkinter.CTk):
	def __init__(self):
		# create window
		super().__init__()
		self.title("The Classical Game -- Twenty Four")
		self.geometry("1000x700")
		
		# initialize the gird manager
		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=5)
		self.grid_rowconfigure(0, weight=1)
		
		# define widgets
		self.navigation_bar_frame = AsideBarFrame(self, "Twenty Four")
		
		# place widgets
		self.navigation_bar_frame.grid(row=0, column=0, sticky="nsew")
		
		

def main():
	customtkinter.set_appearance_mode("dark")
	app = App()
	app.mainloop()


if __name__ == '__main__':
	main()