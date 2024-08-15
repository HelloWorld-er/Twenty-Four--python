import customtkinter
import fonts


game_modes_list = ["Challenge", "Solver", "Duel"]


class DescriptionFrame(customtkinter.CTkFrame):
	def __init__(self, parent, desc_title="", desc_content="", *args, **kwargs):
		# create frame
		super().__init__(parent, *args, **kwargs)
		
		# initialize the grid manager
		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure((0, 1), weight=1) # description-title & description-content

		# define widgets
		self.desc_title = customtkinter.CTkLabel(self, text=desc_title, font=fonts.get_desc_title())
		self.desc_content = customtkinter.CTkTextbox(self, wrap="word", state="disabled", font=fonts.get_desc_content())
		self.update_desc_content(desc_content)

		# place widgets
		self.desc_title.grid(row=0, column=0, sticky="ew", ipadx=5, ipady=2, padx=10, pady=5)
		self.desc_content.grid(row=1, column=0, sticky="ew", ipadx=5, ipady=2, padx=10, pady=5)

	def update_desc_title(self, desc_title):
		self.desc_title.configure(text=desc_title)

	def update_desc_content(self, desc_content):
		self.desc_content.delete("0.0", "end")
		self.desc_content.insert("0.0", desc_content)


class GameModeFrame(customtkinter.CTkFrame):
	def __init__(self, parent, *args, **kwargs):
		global game_mode_dict
		
		# create frame
		super().__init__(parent, *args, **kwargs)
		
		# initialize the grid manager
		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure(tuple(range(3)), weight=1)
		
		# define widgets
		game_mode_widgets_dict = {}
		for game_mode in game_modes_list:
			game_mode_widgets_dict[game_mode] = customtkinter.CTkButton(self, text=f"{game_mode} Mode", font=fonts.get_game_mode_button(), fg_color=("DarkOrange2", "DarkOrange3"), hover_color=("DarkOrange3", "DarkOrange4"), border_width=2)
		
		# place widgets
		for i, game_mode in enumerate(game_mode_widgets_dict.keys()):
			game_mode_widgets_dict[game_mode].grid(row=i, column=0, sticky="ew", ipady=5, padx=5, pady=5)
		


class AsideBarFrame(customtkinter.CTkFrame):
	def __init__(self, parent, title, corner_radius=0, *args, **kwargs):
		# create frame
		super().__init__(parent, corner_radius=corner_radius, *args, **kwargs)
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


class IntroductionFrame(customtkinter.CTkFrame):
	def __init__(self, parent, *args, **kwargs):
		# create frame
		super().__init__(parent, *args, **kwargs)
		
		# initialize the grid manager
		self.grid_columnconfigure(0, weight=1)
		
		# define widgets
		self.desc = DescriptionFrame(self, desc_title="Twenty Four Introduction", desc_content="")
		
		# place widgets
		self.desc.grid(row=0, column=0, sticky="ew", ipady=5, padx=10, pady=10)


class ChallengeModeFrame(customtkinter.CTkFrame):
	def __init__(self, parent, *args, **kwargs):
		# create frame
		super().__init__(parent, *args, **kwargs)
		
		# initialize the grid manager
		self.grid_columnconfigure(0, weight=1)


class SolverModeFrame(customtkinter.CTkFrame):
	def __init__(self, parent, *args, **kwargs):
		# create frame
		super().__init__(parent, *args, **kwargs)
		
		# initialize the grid manager
		self.grid_columnconfigure(0, weight=1)


class DuelModeFrame(customtkinter.CTkFrame):
	def __init__(self, parent, *args, **kwargs):
		# create frame
		super().__init__(parent, *args, **kwargs)
		
		# initialize the grid manager
		self.grid_columnconfigure(0, weight=1)


class App(customtkinter.CTk):
	def __init__(self, *args, **kwargs):
		# create window
		super().__init__(*args, **kwargs)
		self.title("The Classical Game -- Twenty Four")
		self.geometry("1000x700")
		
		# initialize the gird manager
		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=5)
		self.grid_rowconfigure(0, weight=1)
		
		# define widgets
		self.navigation_bar_frame = AsideBarFrame(self, "Twenty Four")
		self.introduction_frame = IntroductionFrame(self)
		self.challenge_mode_frame = ChallengeModeFrame(self)
		self.solver_mode_frame = SolverModeFrame(self)
		self.duel_mode_frame = DuelModeFrame(self)
		
		# place widgets
		self.navigation_bar_frame.grid(row=0, column=0, sticky="nsew")
		self.introduction_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
		# self.challenge_mode_frame.grid(row=0, column=1, sticky="nsew")
		# self.solver_mode_frame.grid(row=0, column=1, sticky="nsew")
		# self.duel_mode_frame.grid(row=0, column=1, sticky="nsew")
		
		

def main():
	# customtkinter.set_appearance_mode("dark")
	app = App()
	app.mainloop()


if __name__ == '__main__':
	main()