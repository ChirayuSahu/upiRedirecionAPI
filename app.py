from flask import Flask, render_template, redirect, request
import urllib.parse

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_upi', methods=['POST'])
def generate_upi():
    """Handles form submission and redirects to UPI payment link"""
    try:
        vpa = request.form.get('vpa')
        amount = request.form.get('amount')

        if not vpa or not amount:
            return "Error: VPA and Amount are required.", 400

        # Generate UPI deep link
        upi_url = f"upi://pay?pa={urllib.parse.quote(vpa)}&am={amount}&cu=INR"

        return redirect(upi_url)

    except Exception as e:
        return f"Error: {str(e)}", 400

@app.route('/upi/<path:params>', methods=['GET'])
def upi_api(params):
    """Handles direct API access via URL"""
    try:
        decoded_params = urllib.parse.unquote(params)
        if '&' not in decoded_params:
            return "Error: Invalid format. Use /upi/vpa@bank&amount", 400
        
        vpa, amount = decoded_params.split('&')

        # Generate UPI deep link
        upi_url = f"upi://pay?pa={urllib.parse.quote(vpa)}&am={amount}&cu=INR"

        return redirect(upi_url)

    except Exception as e:
        return f"Error: {str(e)}", 400

if __name__ == '__main__':
    app.run(debug=True)
