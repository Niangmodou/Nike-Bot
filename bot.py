from selenium import webdriver
import time


#CUSTOMER CLASS TO STORE SHIPPING INFORMATION
class Customer:
    def __init__(self,size):
        self.size = size

    def getFirstName(self):
        self.first_name = input("Enter First Name: ")
        return self.first_name
    
    def getLastName(self):
        self.last_name = input("Enter last Name: ")
        return self.last_name

    def getAddress(self):
        self.address = input("Enter Street Adress: ")
        return self.address
    
    def getCity(self):
        self.city = input("Enter City: ")
        return self.city
        
    def getState(self):
        self.state = "TN"#input("Enter State Abrreviation(2 letters): ").upper()
        return self.state

    def getEmail(self):
        self.email = input("Enter Email: ")
        return self.email
    
    def getNumber(self):
        self.number = input("Enter Phone Number: ")
        return self.number

class Card:
    def __init__(self):
         self.name = "Card"

    def getCard(self):
        self.card = input("Enter Card Number(16 Digits): ")
        return self.card

    def getExp(self):
        self.expdate = input("Enter Card Exp Date(MM/YY): ")
        return self.expdate

    def getCVV(self):
        self.cvv = input("Enter CVV Number: ")
        return self.cvv

#XPATHS FOR PAYMENT INFORMATION
paymentXpath = {"Card Number": "//*[@id=\"creditCardNumber\"]",
    "Exp Date": "//*[@id=\"expirationDate\"]",
        "CVV": "//*[@id=\"cvNumber\"]"}

#XPATHS FOR SHIPPING INFORMATION
shippingXpath = {
"firstName":"//*[@id=\"firstName\"]",
"lastName": "//*[@id=\"lastName\"]",
"address": "//*[@id=\"address1\"]",
"city": "//*[@id=\"city\"]",
"state": "//*[@id=\"state\"]/option[44]",
"postalCode": "//*[@id=\"postalCode\"]",
"email": "//*[@id=\"email\"]",
"number": "//*[@id=\"email\"]"
}

#XPATHS FOR SHOE SIZE INFORMATION
shoeXpath = {
8: "//*[@id=\"buyTools\"]/div[1]/div[2]/label[2]",
8.5: "//*[@id=\"buyTools\"]/div[1]/div[2]/label[3]",
9: "//*[@id=\"buyTools\"]/div[1]/div[2]/label[4]",
9.5: "//*[@id=\"buyTools\"]/div[1]/div[2]/label[5]",
10: "//*[@id=\"buyTools\"]/div[1]/div[2]/label[6]",
10.5: "//*[@id=\"buyTools\"]/div[1]/div[2]/label[7]",
11: "//*[@id=\"buyTools\"]/div[1]/div[2]/label[8]",
11.5: "//*[@id=\"buyTools\"]/div[1]/div[2]/label[9]",
12: "//*[@id=\"buyTools\"]/div[1]/div[2]/label[10]",
12.5: "//*[@id=\"buyTools\"]/div[1]/div[2]/label[11]"}

#XPATHS FOR NAVIGATION
navigation = {
"AddCart": "//*[@id=\"buyTools\"]/div[2]/button[1]",
"Checkout": "//*[@id=\"PDP\"]/div/div[4]/div/div/div/div/div/div/div/div/div/div[3]/button[2]",
"Checkout2": "//*[@id=\"react-root\"]/div/div[7]/div/button",
"saveContinue": "//*[@id=\"shipping\"]/div/div/div/form/div/div/div/div[2]/button[2]",
"continuePayment": "//*[@id=\"shipping\"]/div/div/div/div[4]/div/button",
"placeOrder":"//*[@id=\"placeorderAB3576\"]/div/div[1]/button"

}


#RETRIEVE XPATH FOR SHOE SIZE
def retrieveSize(size):
    size = int(size)
    if (size in shoeXpath):
        return shoeXpath[size]
    else:
        print("SIZE IS NOT SUPPORTED!")
        return -1

#Function to retrive shipping Information
def retrieveShippingInfo():
    global currXpath,address,city,state
    global firstName,lastName,number,email

    size = input("Enter Shoe Size: ")
    currXpath = retrieveSize(size)
    
    customerObj = Customer(size)
    
    firstName = customerObj.getFirstName()
    lastName = customerObj.getLastName()

    address = customerObj.getAddress()
    city = customerObj.getCity()
    state = customerObj.getState()

    number = customerObj.getNumber()
    email = customerObj.getEmail()

    print("====================================================")

#Function to retrive Card Information
def retrieveCardInfo():
    global cardNum,cardDate,cardCVV

    cardObj = Card()

    cardNum = cardObj.getCard()
    cardDate = cardObj.getExp()
    cardCVV = cardObj.getCVV()

    print("====================================================")

#ADD SHOE TO CART
def selectShoe():
    currXpath = "//*[@id=\"buyTools\"]/div[1]/div[2]/label[2]"
    sizePath = driver.find_elements_by_xpath(currXpath)[0]
    sizePath.click()
    
    print("SELECTED SIZE")
    
    #AddToCart
    cartPath = driver.find_elements_by_xpath(navigation["AddCart"])[0]
    cartPath.click()
    
    print("ADDED SHOE TO CART")

    #PAUSE SO ITEM COULD BE ADDED TO CART
    time.sleep(1)

#CLICKS CHECKOUT BUTTONS TO TAKE YOU TO CART
def checkoutButton():
    checkoutPath = driver.find_elements_by_xpath(navigation["Checkout"])[0]
    checkoutPath.click()
    
    print("Selected Checkout Button")
    
    #Checkout Page
    checkoutPage = driver.find_elements_by_xpath(navigation["Checkout2"])[0]
    checkoutPage.click()
    
    print("Pressed Checkout Button")

    #Guest Checkout
    guestCheckout = driver.find_elements_by_xpath("//*[@id=\"react-root\"]/div/div[4]/div/div/button[1]")[0]
    guestCheckout.click()

    time.sleep(1)

#Add Shipping Information
def shippingInfo():
    firstNamePath = driver.find_elements_by_xpath(shippingXpath["firstName"])[0].send_keys(firstName)
    lastNamePath = driver.find_elements_by_xpath(shippingXpath["lastName"])[0].send_keys(lastName)
    addressPath = driver.find_elements_by_xpath(shippingXpath["address"])[0].send_keys(address)
    cityPath = driver.find_elements_by_xpath(shippingXpath["city"])[0].send_keys(city)
    codePath = driver.find_elements_by_xpath(shippingXpath["postalCode"])[0].send_keys(postalCode)
    statePath = driver.find_elements_by_xpath(shippingXpath["state"])[0].send_keys("TN")
    emailPath = driver.find_elements_by_xpath(shippingXpath["email"])[0].send_keys(email)
    numberPath = driver.find_elements_by_xpath(shippingXpath["number"])[0].send_keys(number)

    print("ADDED SHIPPING INFORMATION")
    
    driver.find_elements_by_xpath(navigation["saveContinue"])[0].click()
    
    time.sleep(1)
    
    driver.find_elements_by_xpath(navigation["continuePayment"])[0].click()

    time.sleep(1)

#ADD PAYMENT INFORMATION
def cardInfo():
    cardPath = driver.find_elements_by_xpath()[0].send_keys(cardNum)
    expPath = driver.find_elements_by_xpath()[0].send_keys(cardDate)
    cvvPath = driver.find_elements_by_xpath()[0].send_keys(cardCVV)

def navigatePage():
    #Checkout
    selectShoe()
    
    #Click Checkout Button
    checkoutButton()

    #Add Shipping Information
    shippingInfo()
    
    #Add Credit Card Information
    cardInfo()

    print("====================================================")


def main():
    global driver
    
    print("Welcome to NIKE VaporMax BOT")
    print("====================================================")
    retrieveShippingInfo()
    retrieveCardInfo()
    driver = webdriver.Chrome("/Users/ModouNiang/Documents/Python Programs/Nike-Bot/chromedriver")
    driver.get("https://www.nike.com/t/air-vapormax-plus-mens-shoe-w4xgr4/924453-100")
    

    navigatePage()

    orderPath = driver.find_elements_by_xpath(navigation["placeOrder"])[0].click()

    print("THANK YOU! \n Your Order has Been Placed!")

main()

#MADE WITH LOVE BY MODOU NIANG

