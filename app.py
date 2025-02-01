from flask import Flask, render_template, redirect, request
import urllib.parse

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upi/<path:params>', methods=['GET'])
def generate_upi(params):
    try:
        decoded_params = urllib.parse.unquote(params)
        vpa, rest = decoded_params.split('@')
        bank, amount = rest.split('&')
        upi_url = f"upi://pay?pa={vpa}@{bank}&am={amount}&cu=INR"
        return redirect(upi_url)
    except Exception as e:
        return f"Error: Invalid format - {str(e)}", 400

@app.route('/generate_upi', methods=['POST'])
def generate_upi_from_form():
    vpa = request.form['vpa']
    bank = request.form['bank']
    amount = request.form['amount']
    upi_url = f"upi://pay?pa={vpa}@{bank}&am={amount}&cu=INR"
    return redirect(upi_url)

# Only for local development, Vercel doesn't use this
if __name__ == '__main__':
    app.run(debug=True)
