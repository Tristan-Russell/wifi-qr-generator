import qrcode

def generate_wifi_qr_code(ssid, password, filename):
    """
    Generate a WiFi QR code with the provided SSID and password.

    :param ssid: SSID (Network Name)
    :param password: WiFi Password
    :param output_file: Output file name for the QR code image
    """
    wifi_info = f'WIFI:T:WPA;S:{ssid};P:{password};;'
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(wifi_info)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename+'.png')

def get_wifi_credentials():
    """
    Get WiFi credentials (SSID and Password) from the user.
    :return: Tuple containing SSID and Password
    """
    ssid = input("Enter SSID (Network Name): ")
    password = input("Enter Password: ")
    filename = input("Enter filename (New Image Name): ")
    return ssid, password, filename

if __name__ == "__main__":
    try:
        ssid, password, filename = get_wifi_credentials()
        generate_wifi_qr_code(ssid, password, filename)
        print("WiFi QR code generated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
