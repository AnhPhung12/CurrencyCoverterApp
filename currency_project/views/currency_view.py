import customtkinter as ctk


class CurrencyView(ctk.CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        # Configure main window
        self.title("Global Currency Converter Pro")
        self.geometry("450x600")
        ctk.set_appearance_mode("dark")

        # Bilingual title
        self.label = ctk.CTkLabel(
            self,
            text="CURRENCY CONVERTER\n(FOREIGN EXCHANGE)",
            font=("Arial", 22, "bold"),
            text_color="#F080A0"
        )
        self.label.pack(pady=30)

        # Amount input field (Placeholder guides user to enter numbers with separators)
        self.amount_entry = ctk.CTkEntry(
            self,
            placeholder_text="Amount (e.g. 100.000 or 100000)",
            width=320,
            height=40
        )
        self.amount_entry.pack(pady=10)

        # Currency code input fields
        self.from_entry = ctk.CTkEntry(
            self,
            placeholder_text="From (e.g. USD)",
            width=320
        )
        self.from_entry.pack(pady=10)

        self.to_entry = ctk.CTkEntry(
            self,
            placeholder_text="To (e.g. VND)",
            width=320
        )
        self.to_entry.pack(pady=10)

        # Convert button (Pink color)
        self.convert_btn = ctk.CTkButton(
            self,
            text="CONVERT",
            command=self.controller.handle_convert,
            fg_color="#F080A0",
            hover_color="#EF91AD",
            height=45,
            font=("Arial", 14, "bold")
        )
        self.convert_btn.pack(pady=15)

        # Reset button (Gray color)
        self.reset_btn = ctk.CTkButton(
            self,
            text="RESET",
            command=self.reset_ui,
            fg_color="#444444",
            hover_color="#555555"
        )
        self.reset_btn.pack(pady=5)

        # Result display area
        self.result_num = ctk.CTkLabel(
            self,
            text="Result: ---",
            font=("Arial", 20, "bold")
        )
        self.result_num.pack(pady=(25, 5))

        # Text representation (English/Vietnamese)
        self.result_text = ctk.CTkLabel(
            self,
            text="",
            font=("Arial", 13, "italic"),
            text_color="#F080A0",
            wraplength=400
        )
        self.result_text.pack(pady=5)

    def get_inputs(self):
        """Retrieve raw data from input fields"""
        return self.amount_entry.get(), self.from_entry.get().upper(), self.to_entry.get().upper()

    def update_display(self, num_val, text_val):
        """Update results on the screen"""
        self.result_num.configure(text=num_val, text_color="white")
        self.result_text.configure(text=f"In words: {text_val}")

    def show_error(self, message):
        """Display error message and auto-clear after 3 seconds"""
        self.result_num.configure(text="Error!", text_color="#FF6B6B")
        self.result_text.configure(text=message, text_color="#FF6B6B")
        self.after(3000, lambda: self.result_text.configure(text="", text_color="#F080A0"))

    def reset_ui(self):
        """Clear all inputs and results"""
        self.amount_entry.delete(0, 'end')
        self.from_entry.delete(0, 'end')
        self.to_entry.delete(0, 'end')
        self.result_num.configure(text="Result: ---", text_color="white")
        self.result_text.configure(text="")