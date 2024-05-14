# Import necessary modules
from anvil import open_form
import stripe

# Set your Stripe API key
stripe.api_key = "YOUR_STRIPE_API_KEY"

# Define the CheckoutForm class
class CheckoutForm(StripeCheckoutFormTemplate):
    def __init__(self, **properties):
        # Set up the form
        self.init_components(**properties)

    # Event handler for the "Pay" button click event
    def pay_button_click(self, **event_args):
        try:
            # Create a checkout session with Stripe
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'kes',
                        'unit_amount': 13000,  # Amount in cents (e.g., 10000 = KES 100.00)
                        'product_data': {
                            'name': '3D Architecture Design',
                        },
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url='https://https://3darchitectureengineering.anvil.app/success',
                cancel_url='https://https://3darchitectureengineering.anvil.app/cancel',
            )

            # Redirect the user to the Stripe Checkout session
            self.link_checkout.url = f"https://checkout.stripe.com/en/pay/{checkout_session.id}"
        except Exception as e:
            # Handle errors gracefully
            print(f"Error: {e}")

# Run the app
if __name__ == '__main__':
    open_form('CheckoutForm')
