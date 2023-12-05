import qrcode

def generate_wifi_qr_code(ssid, password):
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
    img.save("wifi_qr_code.png")

if __name__ == "__main__":
    ssid = input("Enter SSID (Network Name): ")
    password = input("Enter Password: ")
    generate_wifi_qr_code(ssid, password)
