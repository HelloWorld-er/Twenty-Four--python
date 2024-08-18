import customtkinter


class SensitiveScrollableFrame(customtkinter.CTkScrollableFrame):
	_scrollbar_update_time = 200
	
	def __init__(self, parent, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		self._hide_x_scrollbar = True
		self._hide_y_scrollbar = True
		if self._orientation == "horizontal":
			self._create_grid(re_grid_frame=True, re_grid_x_scrollbar=True)
		elif self._orientation == "vertical":
			self._create_grid(re_grid_frame=True, re_grid_y_scrollbar=True)
		self.after(50, self._check_if_scrollbars_needed, None, True)
	
	def _create_grid(self, re_grid_frame=False, re_grid_x_scrollbar=False, re_grid_y_scrollbar=False):
		border_spacing = self._apply_widget_scaling(
			self._parent_frame.cget("corner_radius") + self._parent_frame.cget("border_width"))
		
		if re_grid_frame:
			self._parent_frame.grid_columnconfigure(0, weight=1)
			self._parent_frame.grid_rowconfigure(1, weight=1)
			self._parent_canvas.grid(row=1, column=0, sticky="nsew")
		
		if re_grid_x_scrollbar:
			if self._hide_x_scrollbar:
				self._parent_canvas.grid_configure(padx=border_spacing, pady=border_spacing)
				self._scrollbar.grid_forget()
			else:
				self._parent_canvas.grid_configure(padx=border_spacing, pady=(border_spacing, 0))
				self._scrollbar.grid(row=2, column=0, sticky="nsew", padx=border_spacing)
			
			if self._label_text is not None and self._label_text != "":
				self._label.grid(row=0, column=0, sticky="ew", padx=border_spacing, pady=border_spacing)
			else:
				self._label.grid_forget()
		
		if re_grid_y_scrollbar:
			if self._hide_y_scrollbar:
				self._parent_canvas.grid_configure(padx=border_spacing, pady=border_spacing)
				self._scrollbar.grid_forget()
			else:
				self._parent_canvas.grid_configure(padx=(border_spacing, 0), pady=border_spacing)
				self._scrollbar.grid(row=1, column=1, sticky="nsew", pady=border_spacing)
			
			if self._label_text is not None and self._label_text != "":
				self._label.grid(row=0, column=0, columnspan=2, sticky="ew", padx=border_spacing, pady=border_spacing)
			else:
				self._label.grid_forget()
	
	def _check_if_scrollbars_needed(self, event=None, continue_loop: bool = False):
		if self._orientation == "horizontal":
			if self._parent_canvas.xview() != (0.0, 1.0) and not self._scrollbar.winfo_ismapped():  # x scrollbar needed
				self._hide_x_scrollbar = False
				self._create_grid(re_grid_x_scrollbar=True)
			elif self._parent_canvas.xview() == (0.0, 1.0) and self._scrollbar.winfo_ismapped():  # x scrollbar not needed
				self._hide_x_scrollbar = True
				self._create_grid(re_grid_x_scrollbar=True)
		elif self._orientation == "vertical":
			# print(self._hide_y_scrollbar, self._parent_canvas.yview())
			if self._parent_canvas.yview() != (0.0, 1.0) and not self._scrollbar.winfo_ismapped():  # y scrollbar needed
				self._hide_y_scrollbar = False
				self._create_grid(re_grid_y_scrollbar=True)
			elif self._parent_canvas.yview() == (0.0, 1.0) and self._scrollbar.winfo_ismapped():  # y scrollbar not needed
				self._hide_y_scrollbar = True
				self._create_grid(re_grid_y_scrollbar=True)
		
		if self._parent_canvas.winfo_exists() and continue_loop is True:
			self.after(self._scrollbar_update_time, lambda: self._check_if_scrollbars_needed(continue_loop=True))
	
	def _set_dimensions(self, width=None, height=None):
		super()._set_dimensions(width, height)
		self._create_grid(re_grid_frame=True, re_grid_x_scrollbar=True,
		                                           re_grid_y_scrollbar=True)
	
	def configure(self, **kwargs):
		super().configure(**kwargs)
		self._create_grid(re_grid_frame=True, re_grid_x_scrollbar=True,
		                                           re_grid_y_scrollbar=True)
	
	def destroy(self):
		super().destroy()
	
	def get_real_time_canvas_width(self):
		return self._parent_canvas.winfo_width()
	
	def get_real_time_canvas_height(self):
		return self._parent_canvas.winfo_height()


if __name__ == "__main__":
	app = customtkinter.CTk()
	app.title("Sensitive Scrollable Frame")
	app.geometry("500x500")
	
	app.columnconfigure(0, weight=1)
	
	frame = SensitiveScrollableFrame(app, width=100, height=100)
	frame.grid(row=0, column=0, sticky="nsew")
	
	for i in range(4):
		label = customtkinter.CTkLabel(frame, text=f"Label {i}")
		label.grid(row=i, column=0, sticky="ew", padx=5, pady=5)
	
	app.mainloop()
