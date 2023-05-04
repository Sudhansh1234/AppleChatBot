
from tkinter import scrolledtext
import webbrowser
import tkinter as tk
from tkinter import ttk
import openai
from tkinter import *
from PIL import ImageTk, Image
import pandas as pd
from tkinter import simpledialog

# Create the main window
window = tk.Tk()
window.geometry("740x500")
window.title("Apple Support Chatbot")
window.configure(bg='#1E1E1E')

# Add a background image
background_img = ImageTk.PhotoImage(Image.open("image.jpg"))
background_label = tk.Label(window, image=background_img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a frame to hold the chat log
chat_frame = tk.Frame(window, bg="#252525")
chat_frame.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.6, anchor="n")

# Create a label for the chat log
chat_label = tk.Label(chat_frame, text="Chat Log", font=("Arial", 14), bg="#252525", fg="white")
chat_label.pack(pady=10)

# Create a scrolled text widget for the chat log
chatlog = scrolledtext.ScrolledText(chat_frame, width=70, height=18, bg='#2E2E2E', fg='#FFFFFF', font=("Arial", 12))
chatlog.pack(pady=10)

# Create a frame to hold the input box and send button
input_frame = tk.Frame(window, bg="#252525")
input_frame.place(relx=0.5, rely=0.75, relwidth=0.9, relheight=0.1, anchor="n")

# Create an input box for sending messages
inputbox = tk.Entry(input_frame, width=50, bg='#2E2E2E', fg='#FFFFFF', insertbackground='#FFFFFF', font=("Arial", 12))
inputbox.pack(side="left", padx=10)


# define a function to handle sending messages
def handle_message(message):
    if "product specifications" in message.lower() or "product specs" in message.lower() or "what are the specs" in message.lower() or "specifications of the phone" in message.lower() or "display size" in message.lower() or "battery life" in message.lower() or "camera" in message.lower():
        response = productspecs()
    elif "order new product" in message.lower() or "buy new phone" in message.lower() or "order a new mobile" in message.lower():
        response = webscraperproduct()
    elif "exchange offers" in message.lower() or "exchange my phone" in message.lower() or "trade-in" in message.lower():
        response = "We have exchange offers available for old mobile phones. Please visit our website or nearest store for more information.\nhttps://www.apple.com/in/shop/trade-in"
    elif "warranty policy" in message.lower() or "warranty" in message.lower() or "guarantee" in message.lower():
        response = "Our mobile phones come with a 1-year warranty. Please visit our website or nearest store for more information.\nhttps://www.apple.com/legal/warranty/products/accessory-warranty-english.html"
    elif "order status" in message.lower() or "track my order" in message.lower() or "delivery status" in message.lower():
        response = orderstatus()
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

def orderstatus():

        df = pd.read_excel("orders.xlsx")

        # Use simpledialog to prompt the user for input
        phone_number = simpledialog.askstring("Order Status", "Please enter your phone number:").astype(str)

        # Convert the phone number column to a string data type
        df['Phone Number'] = df['Phone Number'].astype(str)
        df['Order Status'] = df['Order Status'].astype(str)

        row = df.loc[df['Phone Number'] == phone_number]

        # Check if a row was found
        if not row.empty:
            # Print the order status for the matching phone number
            chatlog.insert(tk.END, "Order status for phone number", phone_number, "is", row['Order Status'].iloc[0])
        else:
            # Print an error message if no matching phone number was found
            chatlog.insert(tk.END, "No order found for phone number", phone_number)


def productspecs():
 model_window1 = tk.Toplevel(window)
 model_window1.geometry("600x400")
 model_window1.title("Which product specifications are you looking for")

 tk.Label(model_window1, text="Select Product:").grid(row=0, column=0, padx=10, pady=10)
 models = ["iPhone", "Macbook", "Airpods"]

 var = tk.StringVar(value=models[0])
 for i, model in enumerate(models):
     tk.Radiobutton(model_window1, text=model, variable=var, value=model).grid(row=i + 1, column=0)

 def getproduct():
     def productspecsairpods():
         model_window = tk.Toplevel(window)
         model_window.geometry("600x400")
         model_window.title("Choose Airpod Model")

         # create a label and radio buttons for selecting the iPhone model
         tk.Label(model_window, text="Select Airpod Model:").grid(row=0, column=0, padx=10, pady=10)
         models = ["AirPods", "AirPods Pro"]
         var = tk.StringVar(value=models[0])
         for i, model in enumerate(models):
             tk.Radiobutton(model_window, text=model, variable=var, value=model).grid(row=i + 1, column=0)

         def get_airpod_specs():
             model = var.get()
             model_specs = {
                 "AirPods": "Here are the specifications for AirPods:\nBattery life: up to 5 hours\nCharging case battery life: over 24 hours\nCharging time: about 2 hours\nConnectivity: Bluetooth 5.0\nCompatibility: iOS and Android devices",
                 "AirPods Pro": "Here are the specifications for AirPods Pro:\nBattery life: up to 4.5 hours\nCharging case battery life: over 24 hours\nCharging time: about 2 hours\nConnectivity: Bluetooth 5.0\nNoise cancellation: Yes\nTransparency mode: Yes\nCompatibility: iOS and Android devices"
             }
             # update the chatlog with the selected model's specifications
             chatlog.insert(tk.END, model_specs[model] + "\n\n")
             model_window.destroy()

         tk.Button(model_window, text="Get Specifications", command=get_airpod_specs).grid(row=5, column=0, pady=10)

     def productspecsmacbook():
         # create a new window to select the iPhone model
         model_window = tk.Toplevel(window)
         model_window.geometry("600x400")
         model_window.title("Choose Macbook Model")

         # create a label and radio buttons for selecting the iPhone model
         tk.Label(model_window, text="Select Macbook Model:").grid(row=0, column=0, padx=10, pady=10)
         models = ["MacBook Air", "MacBook Pro 13-inch", "MacBook Pro 16-inch"]
         var = tk.StringVar(value=models[0])
         for i, model in enumerate(models):
             tk.Radiobutton(model_window, text=model, variable=var, value=model).grid(row=i + 1, column=0)

         def get_macbook_specs():
             model = var.get()
             model_specs = {
                 "MacBook Air": "Here are the specifications for the MacBook Air:\nScreen size: 13.3 inches\nResolution: 2560 x 1600 pixels\nProcessor: Apple M1 chip with 8-core CPU and 7-core GPU\nRAM: 8GB or 16GB\nStorage: 256GB, 512GB, 1TB, or 2TB\nBattery: Up to 15 hours of web browsing\nOS: macOS Big Sur",
                 "MacBook Pro 13-inch": "Here are the specifications for the MacBook Pro 13-inch:\nScreen size: 13.3 inches\nResolution: 2560 x 1600 pixels\nProcessor: Apple M1 chip with 8-core CPU and 8-core GPU\nRAM: 8GB or 16GB\nStorage: 256GB, 512GB, 1TB, or 2TB\nBattery: Up to 17 hours of web browsing\nOS: macOS Big Sur",
                 "MacBook Pro 16-inch": "Here are the specifications for the MacBook Pro 16-inch:\nScreen size: 16 inches\nResolution: 3072 x 1920 pixels\nProcessor: Intel Core i7 or i9\nRAM: 16GB, 32GB, or 64GB\nStorage: 512GB, 1TB, 2TB, 4TB, or 8TB\nBattery: Up to 11 hours of web browsing\nOS: macOS Big Sur"
             }
             # update the chatlog with the selected model's specifications
             chatlog.insert(tk.END, model_specs[model] + "\n\n")
             model_window.destroy()

         # create a button to get the specifications for the selected MacBook model
         tk.Button(model_window, text="Get Specifications", command=get_macbook_specs).grid(row=5, column=0, pady=10)

     def productspecsiphone():
         # create a new window to select the iPhone model
         model_window = tk.Toplevel(window)
         model_window.geometry("600x400")
         model_window.title("Choose iPhone Model")

         # create a label and radio buttons for selecting the iPhone model
         tk.Label(model_window, text="Select iPhone Model:").grid(row=0, column=0, padx=10, pady=10)
         models = ["iPhone X", "iPhone XR", "iPhone XS", "iPhone XS Max"]
         var = tk.StringVar(value=models[0])
         for i, model in enumerate(models):
             tk.Radiobutton(model_window, text=model, variable=var, value=model).grid(row=i + 1, column=0)

         def get_specsiphone():
             model = var.get()
             model_specs = {
                 "iPhone X": "Here are the specifications for the iPhone X:\nScreen size: 5.8 inches\nResolution: 1125 x 2436 pixels\nProcessor: Apple A11 Bionic\nRAM: 3GB\nStorage: 64GB or 256GB\nRear camera: Dual 12MP\nFront camera: 7MP\nBattery: 2716 mAh\nOS: iOS 11",
                 "iPhone XR": "Here are the specifications for the iPhone XR:\nScreen size: 6.1 inches\nResolution: 828 x 1792 pixels\nProcessor: Apple A12 Bionic\nRAM: 3GB\nStorage: 64GB, 128GB, or 256GB\nRear camera: Single 12MP\nFront camera: 7MP\nBattery: 2942 mAh\nOS: iOS 12",
                 "iPhone XS": "Here are the specifications for the iPhone XS:\nScreen size: 5.8 inches\nResolution: 1125 x 2436 pixels\nProcessor: Apple A12 Bionic\nRAM: 4GB\nStorage: 64GB, 256GB, or 512GB\nRear camera: Dual 12MP\nFront camera: 7MP\nBattery: 2658 mAh\nOS: iOS 12",
                 "iPhone XS Max": "Here are the specifications for the iPhone XS Max:\nScreen size: 6.5 inches\nResolution: 1242 x 2688 pixels\nProcessor: Apple A12 Bionic\nRAM: 4GB\nStorage: 64GB, 256GB, or 512GB\nRear camera: Dual 12MP\nFront camera: 7MP\nBattery: 3174 mAh\nOS: iOS 12"
             }
             # update the chatlog with the selected model's specifications
             chatlog.insert(tk.END, model_specs[model] + "\n\n")
             model_window.destroy()

         # create a button to get the specifications for the selected iPhone model
         tk.Button(model_window, text="Get Specifications", command=get_specsiphone).grid(row=5, column=0, pady=10)

     model = var.get()
     if model == "iPhone":
         productspecsiphone()
     elif model == "Macbook":
         productspecsmacbook()
     elif model == "Airpods":
         productspecsairpods()

     # update the chatlog with the selected model's specifications

     model_window1.destroy()


 # create a button to get the specifications for the selected MacBook model
 tk.Button(model_window1, text="Done", command=getproduct).grid(row=5, column=0, pady=10)

def open_link():
    product_link = iphone_list[0].find("a", {"class": "a-link-normal"})["href"]
    product_id = product_link.split("/")[5].split("?")[0]
   
    url = f"https://www.amazon.in/dp/{product_id}"
    webbrowser.open_new(url)

def webscraperproduct():
    import requests
    from bs4 import BeautifulSoup
    chatlog.insert(tk.END, "AI: Here are the latest iphone products:\n")
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
    global iphone_list
    iphone_list = soup.find_all("div", {"class": "s-result-item"})
    count = 0
    # Loop through the iPhone list and extract the name and link for each model
    for iphone in iphone_list:
        if count < 10:
            try:
                name = iphone.find("h2", {"class": "a-size-mini"}).text.strip()
                link = "https://www.amazon.in/" + iphone.find("a", {"class": "a-link-normal"})["href"]
                chatlog.insert(tk.END, name + "-" + link + '\n')
                count += 1
            except:
                pass

    # Create a button to open the first link in a new browser window
    open_button = tk.Button(input_frame, text="Open link", font=("Arial", 12), bg="#4CAF50", fg="white", activebackground="#3e8e41", pady=5, padx=10, bd=0, command=open_link)
    open_button.pack(side="left", padx=10)

    return "These are the 10 top products and the links to buy them"

def send_message(event=None):
    # get the user's message from the input box
    message = inputbox.get()
    # add the user's message to the chat log
    chatlog.insert(tk.END, "You: " + message + "\n")
    # clear the input box
    inputbox.delete(0, tk.END)
    # get the chatbot's response
    response = handle_message(message) or ""
    # add the chatbot's response to the chat log
    chatlog.insert(tk.END, response + "\n")
chatlog.insert(tk.END,"Welcome to the mobile repair center chatbot. How can I assist you today?\n")
# bind the enter key to the send_message function
window.bind('<Return>', send_message)

# create a button to send messages
sendbutton = tk.Button(input_frame, text="Send", font=("Arial", 12), bg="#4CAF50", fg="white", activebackground="#3e8e41", pady=5, padx=10, bd=0, command=send_message)
sendbutton.pack(side="left", padx=10)

# start the GUI event loop
window.mainloop()

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








