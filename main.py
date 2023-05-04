()
import openai

with open('../pythonProject2/hidden.txt') as file:
    openai.api_key = file.read()

def ask_openai(text):
    prompt = f"User: {text}\nAI:"
    completions = openai.Completion.create(
        engine="text-davinci-001",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = completions.choices[0].text.strip()
    return message

# Define function to handle user input and generate responses
def handle_message(message):
    if "product specifications" in message.lower() or "product specs" in message.lower() or "what are the specs" in message.lower() or "specifications of the phone" in message.lower() or "display size" in message.lower() or "battery life" in message.lower() or "camera" in message.lower():
        response =  productspecs(message)
    elif "order new product" in message.lower() or "buy new phone" in message.lower() or "order a new mobile" in message.lower():
        response = webscraperproduct()
    elif "exchange offers" in message.lower() or "exchange my phone" in message.lower() or "trade-in" in message.lower():
        response = "We have exchange offers available for old mobile phones. Please visit our website or nearest store for more information.\nhttps://www.apple.com/in/shop/trade-in"
    elif "warranty policy" in message.lower() or "warranty" in message.lower() or "guarantee" in message.lower():
        response = "Our mobile phones come with a 1-year warranty. Please visit our website or nearest store for more information.\nhttps://www.apple.com/legal/warranty/products/accessory-warranty-english.html"
    elif "order status" in message.lower() or "track my order" in message.lower() or "delivery status" in message.lower():
        response = "You can check the status of your order on our website or by contacting our customer support."
    elif "repair status" in message.lower() or "my phone repair" in message.lower() or "service center" in message.lower():
        response = "You can check the status of your phone repair on our website or by contacting our customer support."
    elif "chat with agent" in message.lower() or "talk to representative" in message.lower() or "customer support" in message.lower():
        response = "You can chat with our customer support agent on our website or call our customer support number."
    elif "new announcements" in message.lower() or "latest news" in message.lower() or "updates" in message.lower():
        response = "Please visit our website or follow us on social media for the latest announcements and updates."
    elif "stores near you" in message.lower() or "nearest store" in message.lower() or "store location" in message.lower():
        response = "You can find the nearest store location on our website or by contacting our customer support."
    elif "emi options" in message.lower() or "installments" in message.lower() or "pay in emi" in message.lower():
        response = "We offer EMI options for mobile phone purchases. Please visit our website or nearest store for more information."
    else:
        response = "I'm sorry, I didn't understand your message. Please try again with a different question or request."
    return response



def productspecs(product):

        chatlog.insert(tk.END,  "AI: Which product model are you interested in? (iPhone/iPad/MacBook/iWatch)" + "\n")
        product = inputbox.get().strip
        if "iphone" in product.lower():
            print("AI: Which iPhone model are you interested in? (e.g. iPhone 13 Pro Max)")
            model = input("User: ").strip().lower()
            if "iphone x" in model:
                specs = "Here are the specifications for the iPhone X:\nScreen size: 5.8 inches\nResolution: 1125 x 2436 pixels\nProcessor: Apple A11 Bionic\nRAM: 3GB\nStorage: 64GB or 256GB\nRear camera: Dual 12MP\nFront camera: 7MP\nBattery: 2716 mAh\nOS: iOS 11"
            elif "iphone xr" in model:
                specs = "Here are the specifications for the iPhone XR:\nScreen size: 6.1 inches\nResolution: 828 x 1792 pixels\nProcessor: Apple A12 Bionic\nRAM: 3GB\nStorage: 64GB, 128GB, or 256GB\nRear camera: Single 12MP\nFront camera: 7MP\nBattery: 2942 mAh\nOS: iOS 12"
            elif "iphone xs" in model:
                specs = "Here are the specifications for the iPhone XS:\nScreen size: 5.8 inches\nResolution: 1125 x 2436 pixels\nProcessor: Apple A12 Bionic\nRAM: 4GB\nStorage: 64GB, 256GB, or 512GB\nRear camera: Dual 12MP\nFront camera: 7MP\nBattery: 2658 mAh\nOS: iOS 12"
            elif "iphone xs max" in model:
                specs = "Here are the specifications for the iPhone XS Max:\nScreen size: 6.5 inches\nResolution: 1242 x 2688 pixels\nProcessor: Apple A12 Bionic\nRAM: 4GB\nStorage: 64GB, 256GB, or 512GB\nRear camera: Dual 12MP\nFront camera: 7MP\nBattery: 3174 mAh\nOS: iOS 12"
            elif "iphone 11" in model:
                specs = "Here are the specifications for the iPhone 11:\nScreen size: 6.1 inches\nResolution: 828 x 1792 pixels\nProcessor: Apple A13 Bionic\nRAM: 4GB\nStorage: 64GB, 128GB, or 256GB\nRear camera: Dual 12MP + 12MP\nFront camera: 12MP\nBattery: 3110 mAh\nOS: iOS 13"
            elif "iphone 11 pro" in model:
                specs = "Here are the specifications for the iPhone 11 Pro:\nScreen size: 5.8 inches\nResolution: 1125 x 2436 pixels\nProcessor: Apple A13 Bionic\nRAM: 4GB\nStorage: 64GB, 256GB, or 512GB\nRear camera: Triple 12MP + 12MP + 12MP\nFront camera: 12MP\nBattery: 3046 mAh\nOS: iOS 13"
            elif "iphone 11 pro max" in model:
                specs = "Here are the specifications for the iPhone 11 Pro:\nScreen size: 6.7 inches\nResolution: 1284 x 2778 pixels\nProcessor: Apple A13 Bionic\nRAM: 4GB\nStorage: 64GB, 256GB, or 512GB\nRear camera: Triple 12MP + 12MP + 12MP\nFront camera: 12MP\nBattery: 3046 mAh\nOS: iOS 13"
            elif "iphone 12 mini" in model:
                specs = "Here are the specifications for the iPhone 12 mini:\nScreen size: 5.4 inches\nResolution: 1080 x 2340 pixels\nProcessor: Apple A14 Bionic\nRAM: 4GB\nStorage: 64GB, 128GB, or 256GB\nRear camera: Dual 12MP + 12MP\nFront camera: 12MP\nBattery: 2227 mAh\nOS: iOS 14"
            elif "iphone 12" in model:
                specs = "Here are the specifications for the iPhone 12:\nScreen size: 6.1 inches\nResolution: 1170 x 2532 pixels\nProcessor: Apple A14 Bionic\nRAM: 4GB\nStorage: 64GB, 128GB, or 256GB\nRear camera: Dual 12MP + 12MP\nFront camera: 12MP\nBattery: 2815 mAh\nOS: iOS 14"
            elif "iphone 12 pro" in model:
                specs = "Here are the specifications for the iPhone 12 Pro:\nScreen size: 6.1 inches\nResolution: 1170 x 2532 pixels\nProcessor: Apple A14 Bionic\nRAM: 6GB\nStorage: 128GB, 256GB, or 512GB\nRear camera: Triple 12MP + 12MP + 12MP\nFront camera: 12MP\nBattery: 2815 mAh\nOS: iOS 14"
            elif "iphone 12 pro max" in model:
                specs = "Here are the specifications for the iPhone 12 Pro Max:\nScreen size: 6.7 inches\nResolution: 1284 x 2778 pixels\nProcessor: Apple A14 Bionic\nRAM: 6GB\nStorage: 128GB, 256GB, or 512GB\nRear camera: Triple 12MP + 12MP + 12MP\nFront camera: 12MP\nBattery: 3687 mAh\nOS: iOS 14"
            elif "iphone 13 mini" in model:
                specs = "Here are the specifications for the iPhone 13 mini:\nScreen size: 5.4 inches\nResolution: 1080 x 2340 pixels\nProcessor: Apple A15 Bionic\nRAM: 4GB\nStorage: 128GB, 256GB, or 512GB\nRear camera: Dual 12MP + 12MP\nFront camera: 12MP\nBattery: 2406 mAh\nOS: iOS 15"
            elif "iphone 13" in model:
                specs = "Here are the specifications for the iPhone 13:\nScreen size: 6.1 inches\nResolution: 1170 x 2532 pixels\nProcessor: Apple A15 Bionic\nRAM: 4GB\nStorage: 128GB, 256GB, or 512GB\nRear camera: Dual 12MP + 12MP\nFront camera: 12MP\nBattery: 3095 mAh\nOS: iOS 15"
            elif "iphone 13 pro" in model:
                specs = "Here are the specifications for the iPhone 13 Pro:\nScreen size: 6.1 inches\nResolution: 1170 x 2532 pixels\nProcessor: Apple A15 Bionic\nRAM: 6GB\nStorage: 128GB, 256GB, 512GB, or 1TB\nRear camera: Triple 12MP + 12MP + 12MP"
            else:
                specs = "I'm sorry i dont understand which model you are referring please try again"
            return specs


def webscraperproduct():
    import requests
    from bs4 import BeautifulSoup
    print("AI: Here are the latest iphone products:\n")
    # Request the page content
    url = "https://www.amazon.in/s?k=iphone&ref=nb_sb_noss_1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"
    }
    response = requests.get(url, headers=headers)
    content = response.content

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(content, "html.parser")

    # Find the list of latest iPhone models
    iphone_list = soup.find_all("div", {"class": "s-result-item"})
    count = 0
    # Loop through the iPhone list and extract the name and link for each model
    for iphone in iphone_list:
        if count < 10:
            try:
                name = iphone.find("h2", {"class": "a-size-mini"}).text.strip()
                link = "https://www.amazon.com" + iphone.find("a", {"class": "a-link-normal"})["href"]
                print(name + " - " + link)
                count += 1
            except:
                pass
    return "These are the 10 top products and the links to buy them"



# Define main function to start the chatbot
def main():
    print("Welcome to the mobile repair center chatbot. How can I assist you today?")
    while True:
        message = input("User: ")
        if message.lower() == "exit":
            break
        response = handle_message(message)
        print("AI:", response)

if __name__ == "__main__":
    main