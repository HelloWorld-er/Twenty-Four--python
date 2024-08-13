import customtkinter


def get_font(family="Arial", size=14, weight="normal", slant="roman"):
	return customtkinter.CTkFont(family=family, size=size, weight=weight, slant=slant)


def get_heading(size=18):
	return get_font(size=size, weight="bold")
