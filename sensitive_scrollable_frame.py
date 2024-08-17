import customtkinter


class SensitiveScrollableFrame(customtkinter.CTkScrollableFrame):
	def __init__(self, parent, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
	
	def _create_grid(self):
		border_spacing = self._apply_widget_scaling(
			self._parent_frame.cget("corner_radius") + self._parent_frame.cget("border_width"))
		
		if self._orientation == "horizontal":
			self._parent_frame.grid_columnconfigure(0, weight=1)
			self._parent_frame.grid_rowconfigure(1, weight=1)
			self._parent_canvas.grid(row=1, column=0, sticky="nsew", padx=border_spacing, pady=(border_spacing, 0))
			self._update_scrollbar(border_spacing)
			
			if self._label_text is not None and self._label_text != "":
				self._label.grid(row=0, column=0, sticky="ew", padx=border_spacing, pady=border_spacing)
			else:
				self._label.grid_forget()
		
		elif self._orientation == "vertical":
			self._parent_frame.grid_columnconfigure(0, weight=1)
			self._parent_frame.grid_rowconfigure(1, weight=1)
			self._parent_canvas.grid(row=1, column=0, sticky="nsew", padx=(border_spacing, 0), pady=border_spacing)
			self._update_scrollbar(border_spacing)
			
			if self._label_text is not None and self._label_text != "":
				self._label.grid(row=0, column=0, columnspan=2, sticky="ew", padx=border_spacing, pady=border_spacing)
			else:
				self._label.grid_forget()
	
	def _fit_frame_dimensions_to_canvas(self, event):
		if self._orientation == "horizontal":
			self._parent_canvas.itemconfigure(self._create_window_id, height=self._parent_canvas.winfo_height())
			if self._parent_canvas.xview() != (0.0, 1.0):
				self._update_scrollbar()
		elif self._orientation == "vertical":
			self._parent_canvas.itemconfigure(self._create_window_id, width=self._parent_canvas.winfo_width())
			if self._parent_canvas.yview() != (0.0, 1.0):
				self._update_scrollbar()
	
	def _update_scrollbar(self, border_spacing=None):
		if border_spacing is None:
			border_spacing = self._apply_widget_scaling(
				self._parent_frame.cget("corner_radius") + self._parent_frame.cget("border_width"))
		if self._orientation == "horizontal":
			if self._parent_canvas.xview() != (0.0, 1.0):
				self._parent_canvas.grid_configure(padx=border_spacing, pady=(border_spacing, 0))
				self._scrollbar.grid(row=2, column=0, sticky="nsew", padx=border_spacing)
			else:
				self._parent_canvas.grid_configure(padx=border_spacing, pady=border_spacing)
				self._scrollbar.grid_remove()
		elif self._orientation == "vertical":
			if self._parent_canvas.yview() != (0.0, 1.0):
				self._parent_canvas.grid_configure(padx=(border_spacing, 0), pady=(border_spacing, 0))
				self._scrollbar.grid(row=1, column=1, sticky="nsew", padx=border_spacing)
			else:
				self._parent_canvas.grid_configure(padx=border_spacing, pady=(border_spacing, 0))
				self._scrollbar.grid_remove()
	
	def get_real_time_canvas_width(self):
		return self._parent_canvas.winfo_width()
	
	def get_real_time_canvas_height(self):
		return self._parent_canvas.winfo_height()


if __name__ == "__main__":
	app = customtkinter.CTk()
	app.title("Sensitive Scrollable Frame")
	app.geometry("500x500")
	
	app.columnconfigure(0, weight=1)
	
	frame = SensitiveScrollableFrame(app)
	frame.grid(row=0, column=0, sticky="nsew")
	
	for i in range(30):
		label = customtkinter.CTkLabel(frame, text=f"Label {i}")
		label.grid(row=i, column=0, sticky="ew", padx=5, pady=5)
	
	app.mainloop()
