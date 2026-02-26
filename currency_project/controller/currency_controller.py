from models.currency_model import CurrencyModel
from views.currency_view import CurrencyView


class CurrencyController:
    def __init__(self):
        self.model = CurrencyModel()
        self.view = CurrencyView(self)

    def handle_convert(self):
        amt_str, from_c, to_c = self.view.get_inputs()

        try:
            # check null
            if not amt_str or not from_c or not to_c:
                raise ValueError("Please fill all fields")

            # Handle number formatting (remove '.' and ',' so float() won’t fail)
            # example: "100.000" or "100,000" -> "100000"
            clean_amt = amt_str.replace(',', '').replace('.', '')

            if not clean_amt.isdigit():
                raise ValueError("Amount must be numbers only")

            amount = float(clean_amt)

            # calculate through Model
            res_amount = self.model.calculate_conversion(amount, from_c, to_c)

            # Format number with thousand separators and 2 decimal places
            formatted_num = f"{res_amount:,.2f} {to_c}"

            # Get text representation (Vietnamese for VND, English for other currencies)
            word_desc = self.model.get_text_representation(res_amount, to_c)

            # Update View
            self.view.update_display(formatted_num, word_desc)

        except ValueError as e:
            self.view.show_error(str(e))
        except Exception as e:
            # Catch API errors or non-existent currency codes
            self.view.show_error("Invalid Currency or Connection Error")

    def run(self):
        """Run the application loop"""
        self.view.mainloop()