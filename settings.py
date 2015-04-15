APP_NAME = 'payment'
PRODUCT_NAME = 'remoover.com'
DOMAIN = 'http://localhost:9000'
SUCCESS_URL = '{}/payment/success'.format(DOMAIN) + "?transaction_id="
CANCEL_URL = '{}/payment/cancel'.format(DOMAIN) + "?transaction_id="

# --- Gateway names ------
PAYPAL = "Paypal"
STRIPE = "Stripe"
AMAZON = "Amazon Payments"
WEPAY = "We pay"
AUTHORIZE_NET = "Authorize.net"
CHECKOUT = "checkout"
GOPAY = "Gopay"

# --- Paypal -----
PAYPAL_CLIENT_ID = 'AQk4WhZ5SEWwwJ6hBOKSUr8DTflniPGgWaugqs1kSJBPIyR4eMnrgSIFHRnIMeRCHAhOvAkWbUWItk7R'

# --- Stripe -----
STRIPE_SECRETE_KEY = 'sk_test_mHtW6W31yxhAhc3oxQ4imUd700btOK0Bqy'
STRIPE_PUBLISHABLE_KEY = 'pk_test_h0UArzKkBT4IauH5dmUZownB00W1QjAkMr'

