#Author:- @python.expert

#import dependencies
try:
    import pyqrcode 
    from pyqrcode import QRCode
except:
    print("Please install Dependencies using pip")
 
#Get a File name to store QR code
name = input("Enter a Name of link:- ")

#Get a Link
url = input("\nEnter a Long URL:- ")
 
# Generate QR code 
url = pyqrcode.create(url) 
  
# Create and save the svg file naming "(you given name).svg" 
url.svg(name+".svg", scale = 8) 