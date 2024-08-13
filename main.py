import customtkinter
import fonts


class NavigationBarFrame(customtkinter.CTkFrame):
	def __init__(self, master, title):
		super().__init__(master)
		self.title = title
		
		self.grid_columnconfigure(0, weight=1)
		
		self.title = customtkinter.CTkLabel(self, text=self.title, font=fonts.get_heading(), corner_radius=6, fg_color=("grey80", "grey25"))
		
		self.title.grid(row=0, column=0, sticky="ew", ipady=10, padx=10, pady=12)


class App(customtkinter.CTk):
	def __init__(self):
		super().__init__()

		self.title("The Classical Game -- Twenty Four")
		self.geometry("1000x700")
		
		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=3)
		self.grid_rowconfigure(0, weight=1)
		
		self.navigation_bar_frame = NavigationBarFrame(self, "Twenty Four")
		
		self.navigation_bar_frame.grid(row=0, column=0, sticky="nsew")
		
		

def main():
	customtkinter.set_appearance_mode("dark")
	app = App()
	app.mainloop()


if __name__ == '__main__':
	main()