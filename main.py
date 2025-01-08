import random
import tkinter as tk
from tkinter import messagebox

def get_country():
    countries = [
        "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", 
        "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", 
        "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", 
        "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", 
        "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", 
        "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", 
        "Congo", "Costa Rica", "Croatia", "Cuba", "Cyprus", 
        "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", 
        "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", 
        "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", 
        "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", 
        "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", 
        "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", 
        "Ivory Coast", "Jamaica", "Japan", "Jordan", "Kazakhstan", 
        "Kenya", "Kiribati", "North Korea", "South Korea", "Kosovo", 
        "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", 
        "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", 
        "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", 
        "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", 
        "Montenegro", "Morocco", "Mozambique", "Myanmar", "Burma", "Namibia", "Nauru", 
        "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", 
        "Macedonia", "Norway", "Oman", "Pakistan", "Palau", 
        "Palestine State", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", 
        "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", 
        "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", 
        "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", 
        "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", 
        "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain", 
        "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", 
        "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", 
        "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", 
        "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", 
        "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", 
        "Vietnam", "Yemen", "Zambia", "Zimbabwe"
    ]
    return random.choice(countries)

def generate_question():
    ranCountry = get_country()
    quesCountry = ranCountry
    numSpace = random.randint(1, len(ranCountry)-2)
    spacelist = {}
    
    for i in range(numSpace):
        sp = random.randint(0, len(ranCountry) - 1)
        while ranCountry[sp] == " " or quesCountry[sp] == "_":
            sp = random.randint(0, len(ranCountry) - 1)
        spacelist.setdefault(ranCountry[sp].lower(), []).append(sp)
        quesCountry = quesCountry[:sp] + "_" + quesCountry[sp + 1:]

    return quesCountry, ranCountry, spacelist

def check_answer():
    quesCountry, ranCountry, spacelist = generate_question()
    check_answer.chance = 3

    def submit_answer():
        nonlocal quesCountry, ranCountry, spacelist
        answer = entry.get().strip().lower()
        entry.delete(0, 'end')
        
        if answer in spacelist:
            positions = spacelist[answer]
            for pos in positions:
                quesCountry = quesCountry[:pos] + ranCountry[pos] + quesCountry[pos + 1:]
            spacelist.pop(answer)
            label_ques.config(text=f"Fill the blank space for this country: {quesCountry}")
            messagebox.showinfo("Correct!", "Correct!")
        else:
            messagebox.showerror("Incorrect!", "Incorrect!")
            check_answer.chance -= 1
        
        if "_" not in quesCountry:
            messagebox.showinfo("Congratulations!", f"The country is {ranCountry}")
            new_game()
        elif check_answer.chance == 0:
            messagebox.showerror("Game Over!", f"The correct country was {ranCountry}")
            new_game()

    def new_game():
        nonlocal quesCountry, ranCountry, spacelist
        quesCountry, ranCountry, spacelist = generate_question()
        label_ques.config(text=f"Fill the blank space for this country: {quesCountry}")
        check_answer.chance = 3

    root = tk.Tk()
    root.title("Country Guessing Game")
    root.geometry("600x300")
    root.configure(bg="#171b53")
    root.resizable(False, False)  

    label_ques = tk.Label(root, text=f"Fill the blank space for this country: {quesCountry}", font=("Helvetica", 14), bg="#171b53",fg="#ffd700")
    label_ques.pack(pady=20,expand=True)

    entry = tk.Entry(root, font=("Helvetica", 14), bg="#171b30", fg="#ffd788", relief="sunken", bd=3)
    entry.pack(expand=True)

    button_submit = tk.Button(root, text="Submit", command=submit_answer, font=("Helvetica", 14), bg="#171d30", fg="#ffd800", relief="raised", bd=3)
    button_submit.pack(pady=10,expand=True)

    root.mainloop()

if __name__ == "__main__":
    check_answer()
