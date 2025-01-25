import tkinter as tk
from tkinter import ttk

morse_dict = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.", ".": ".-.-.-", ",": "--..--", "@": ".--.-.",
    "?": "..--..", "'": ".----.", "!": "-.-.--", "/": "-..-.", "(": "-.--.",
    ")": "-.--.-", ":": "---...", ";": "", "=": "-...-", "-": "-....-",
    "_": "··--·-", "\"": ".-..-.", "%": "", "+": ".-.-.", "&": ".-...",
    " ": "......."
}

def text_to_morse(text: str) -> str:
    """Convert the text passed to the function to morse code.
    It converts the provided text letter by letter.

    Args:
        text (str): Letter, word, or paragraph to convert to
        morse code
    """
    morse = ""
    for letter in text:
        morse += (morse_dict[letter.upper()]) + " "
    return morse.strip()

def morse_to_text(morse: str) -> str:
    """Converts the morse code passed to text.
    It converts the provided morse code as chunks
    separated by space.

    Args:
        morse (str): Morse code to convert to text
    """
    chunks = morse.strip().replace("/", ".......").split(".......")
    result = ""

    for chunk in chunks:
        chars = chunk.strip().split()
        for char in chars:
            for key, value in morse_dict.items():
                if value == char:
                    result += key
                    break
        result += " "

    return result.strip()

class MorseConverterGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Morse Code Converter")
        self.window.geometry("800x600")
        
        # Exit and Clear All
        top_frame = ttk.Frame(self.window, padding="15")
        top_frame.pack(fill=tk.X)
        ttk.Button(top_frame, text="Exit", command=self.window.quit).pack(side=tk.RIGHT, padx=5)
        ttk.Button(top_frame, text="Clear All", command=self.clear_all).pack(side=tk.RIGHT)
        
        
        # Main Window
        main_frame = ttk.Frame(self.window, padding="5")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Input Frame
        input_frame = ttk.LabelFrame(main_frame, text="Input", padding="10")
        input_frame.pack(fill=tk.BOTH, padx=5, pady=5, expand=True)
        
        self.input_text = tk.Text(input_frame, height=5)
        self.input_text.pack(fill=tk.BOTH, expand=True)
        
        # Buttons
        
        button_frame = ttk.Frame(main_frame, padding="10")
        button_frame.pack()
        
        self.to_morse_btn = ttk.Button(button_frame, text="Text to Morse", 
                                     command=self.convert_to_morse)
        self.to_morse_btn.pack(side=tk.LEFT, padx=5)
        
        self.to_text_btn = ttk.Button(button_frame, text="Morse to Text", 
                                    command=self.convert_to_text)
        self.to_text_btn.pack(side=tk.LEFT, padx=5)
        
        # Output frame
        output_frame = ttk.LabelFrame(main_frame, text="Output", padding="10")
        output_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.output_text = tk.Text(output_frame, height=5, state='disabled')
        self.output_text.pack(fill=tk.X)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = ttk.Label(self.window, textvariable=self.status_var, 
                             relief=tk.SUNKEN, padding=(2, 2))
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def clear_all(self):
        self.input_text.delete("1.0", tk.END)
        self.output_text.config(state='normal')
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state='disabled')
        self.status_var.set("All fields cleared")

    def convert_to_morse(self):
        input_value = self.input_text.get("1.0", tk.END).strip()
        try:
            result = text_to_morse(input_value)
            self.update_output(result)
            self.status_var.set("Text converted to Morse code")
        except KeyError:
            self.update_output("Error: Invalid character found")
            self.status_var.set("Error in conversion")

    def convert_to_text(self):
        input_value = self.input_text.get("1.0", tk.END).strip()
        result = morse_to_text(input_value)
        if result:
            self.update_output(result)
            self.status_var.set("Morse code converted to text")
        else:
            self.update_output("Error: Invalid Morse code")
            self.status_var.set("Error in conversion")

    def update_output(self, text):
        self.output_text.config(state='normal')
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert("1.0", text)
        self.output_text.config(state='disabled')

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    script = MorseConverterGUI()
    script.run()