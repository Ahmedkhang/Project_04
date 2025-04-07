import qrcode

data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    'country': "USA",
    'occupation': "Software Engineer",
    'hobbies': ["reading", "coding", "hiking"],
    'email' : 'jhon@gmail.com'
}
qr = qrcode.QRCode(version=1,border=5,box_size=10)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color='blue', back_color='white')  
# img = qrcode.make(data)
img.save('C:/Users/DELL/Pictures/Camera Roll/my_qr_code.png')