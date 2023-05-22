from tkinter import *
import tkinter as tk
import joblib 
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from tkinter import *
from PIL import ImageTk, Image
# from tkinter import Tk, Label, PhotoImage
stop_words = set(stopwords.words('english'))
# Load the vectorizer
vectorizer = joblib.load('vectorizer.joblib') 
# Load the model
model = joblib.load('m.joblib') 
def submit():
    # Function to handle submit button click
    # This is where you can call your model to make a prediction
    input_text = input_box.get()
    # Transform the input using the vectorizer
    input_vec = vectorizer.transform([input_text])
    # Predict the output

    predicted_emotion = model.predict(input_vec)[0]
    input_box.delete(0, tk.END)
    # Update the output box with the predicted emotion
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, predicted_emotion)
    
root = Tk()


# Set the window size
window_width = 400
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

root.title('Emotion in Text Detector')
# l2 = tk.Label(root, text = "EMOTION DETECTION\n", font=('Times', 25, "bold"), foreground="white",bg="brown")

#h_label = Label(root, text="Emotion in Text",bg='pink', font=("Comic Sans MS", 24), command=None)
#h_label.grid(row=0, column=3, padx=10, pady=10)
#h_label.pack(padx=45,pady=10)



bg_image = ImageTk.PhotoImage(Image.open("no1.jpg"))
# bg_image = bg_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
bg_label = Label(root, image=bg_image)
bg_label.place(y=0)# relwidth=0, relheight=0)
#bg_label.pack()
# img = Image.open("uk.jpeg")
# bg_img = ImageTk.PhotoImage(img)
# canvas = Canvas(root, width=width, height=height)
# canvas.pack(fill=BOTH, expand=YES)
# canvas.create_image(0, 0, image=bg_img, anchor=NW)

# Create input box
input_box = Entry(root, width=40)
input_box.place(relx=0.8, rely=0.4, anchor=CENTER)

# Create submit button
submit_button = Button(root, text="Submit", command=submit)
submit_button.place(relx=0.8, rely=0.5, anchor=CENTER)
# Create a text box to display the output
output_box = tk.Text(root, height=1, width=20)
output_box.place(relx=0.8, rely=0.65, anchor="center")

root.mainloop()
