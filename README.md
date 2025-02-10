
<img src="https://socialify.git.ci/ChirayuSahu/upiRedirectionAPI/image?language=1&name=1&owner=1&stargazers=1&theme=Dark" alt="upiRedirectionAPI"/>

![cover](https://github.com/user-attachments/assets/a7779007-b4e3-4fd3-92ee-52b84a766f8e)

# UPI Payment API

A simple API that generates UPI payment links and QR codes for easy transactions. This web application allows users to generate UPI payment links by providing the Virtual Payment Address (VPA) and the payment amount. The generated UPI link can be used to redirect users to their UPI apps like Google Pay, PhonePe, etc.

## Features

- **Generate UPI Links:** Users can generate UPI links for specific VPAs and amounts.
- **QR Code Generation:** A QR code is generated for easy scanning to make payments.
- **Customizable UPI Links:** Allows users to customize payment details, like VPA and amount, using the generated URL.

## Technologies Used

- **Frontend:** HTML, CSS (Tailwind CSS)
- **Backend:** Python (Flask)
- **QR Code Generation:** Python's `qrcode` library
- **Payment Redirection:** Custom UPI links for Google Pay, PhonePe, etc.
- **JSON Response:** Users can receive a JSON response containing payment details.
- **Valid UPI Endings:** Provides a list of valid UPI endings for different banks and payment services.

## Usage

1. **Enter the VPA (Virtual Payment Address):**
   Example: `vpa@bank`

2. **Enter the Amount:**
   Enter the payment amount in INR (e.g., `100`).

3. **Click "Generate UPI Link":**
   Upon submission, the app will generate a UPI link and QR code for the payment.

4. **Payment Options:**
   You can select your preferred payment method (e.g., Google Pay, PhonePe) to initiate the payment.

## Direct UPI Link Format

You can directly generate a UPI link by visiting the following URL format:

```
https://upi-redirection-api.vercel.app/qr/vpa@bank&amount
```
You can also receive a JSON response and obtain a list of valid UPI endings by using:

```
https://upi-redirection-api.vercel.app/upi/api/vpa@bank&amount

https://upi-redirection-api.vercel.app/upi/api/validEndings
```

Replace `vpa@bank` with the actual VPA and `amount` with the payment amount.

## Contributing

If you have suggestions or want to contribute, feel free to create an issue or a pull request. Contributions are welcome!

## License

This project is open-source and available under the MIT License.
