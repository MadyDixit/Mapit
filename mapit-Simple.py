import webbrowser


address = str(input("Enter The Name of City, State and Contry: "))
webbrowser.open('https://www.google.com/maps/place/' + address)
