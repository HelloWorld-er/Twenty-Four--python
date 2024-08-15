import customtkinter


def get_font(family="Arial", size=14, weight="normal", slant="roman"):
	return customtkinter.CTkFont(family=family, size=size, weight=weight, slant=slant)


def get_heading(size=26):
	return get_font(size=size, weight="bold")


def get_aside_bar_default(size=20):
	return get_font(size=size)


def get_game_mode_button(size=18):
	return get_font(size=size)