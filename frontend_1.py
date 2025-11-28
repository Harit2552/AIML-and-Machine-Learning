import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import joblib

# ---------------- LOAD MODEL ----------------
model = joblib.load("car_price_model.pkl")
feature_cols = joblib.load("feature_columns.pkl")

# BRAND → MODEL mapping
brand_models = {
    'AMBASSADOR': ['CLASSIC'],
    'AUDI': ['A3', 'A4', 'A6', 'Q3', 'Q5', 'Q7'],
    'BMW': ['3 SERIES', '5 SERIES', '7 SERIES', 'X1', 'X3', 'X5'],
    'CHEVROLET': ['BEAT', 'CRUZE', 'SPARK', 'TRAILBLAZER', 'SAIL'],
    'FIAT': ['PUNTO', 'LINEA', 'AVVENTURA'],
    'FORD': ['ECOSPORT', 'FIGO', 'ASPIRE', 'ENDEAVOUR', 'FREESTYLE'],
    'HONDA': ['CITY', 'AMAZE', 'JAZZ', 'BR-V', 'WR-V', 'CIVIC'],
    'HYUNDAI': ['I20', 'CRETA', 'VERNA', 'GRAND I10', 'SANTRO', 'AURA', 'VENUE', 'TUCSON'],
    'JEEP': ['COMPASS', 'WRANGLER', 'GRAND CHEROKEE'],
    'KIA': ['SELTOS', 'SONET', 'CARNIVAL'],
    'MAHINDRA': ['XUV300', 'XUV500', 'BOLERO', 'SCORPIO', 'THAR', 'KUV100', 'MARAZZO'],
    'MARUTI': ['SWIFT', 'BALENO', 'ALTO', 'ERTIGA', 'WAGON R', 'CELERIO', 'DZIRE', 'CIAZ', 'BREZZA', 'IGNIS'],
    'MG': ['HECTOR', 'ASTOR', 'GLOSTER', 'ZS EV'],
    'MERCEDES': ['C CLASS', 'E CLASS', 'S CLASS', 'GLA', 'GLC', 'GLE'],
    'NISSAN': ['MICRA', 'SUNNY', 'KICKS', 'TERRANO', 'MAGNITE'],
    'RENAULT': ['KWID', 'TRIBER', 'KIGER', 'DUSTER', 'LODGY'],
    'SKODA': ['RAPID', 'OCTAVIA', 'SUPERB', 'KUSHAQ', 'SLAVIA'],
    'TATA': ['NEXON', 'ALTROZ', 'TIAGO', 'TIGOR', 'HARRIER', 'SAFARI', 'PUNCH'],
    'TOYOTA': ['FORTUNER', 'INNOVA', 'GLANZA', 'URBAN CRUISER', 'ETIOS', 'YARIS', 'CAMRY'],
    'VOLKSWAGEN': ['POLO', 'VENTO', 'TAIGUN', 'JETTA']
}

location_list = [
    "Delhi", "New Delhi", "Noida", "Gurgaon", "Ghaziabad", "Faridabad",
    "Mumbai", "Navi Mumbai", "Thane", "Pune",
    "Bangalore", "Hyderabad", "Chennai", "Kolkata",
    "Ahmedabad", "Surat", "Vadodara", "Jaipur", "Jodhpur", "Udaipur",
    "Lucknow", "Kanpur", "Agra", "Varanasi", "Prayagraj", "Bareilly",
    "Mathura", "Meerut", "Moradabad",
    "Patna", "Gaya", "Ranchi", "Jamshedpur",
    "Bhopal", "Indore", "Gwalior",
    "Kochi", "Thiruvananthapuram", "Kozhikode",
    "Chandigarh", "Ludhiana", "Amritsar",
    "Bhubaneswar", "Cuttack",
    "Guwahati", "Shillong",
    "Dehradun", "Haridwar",
    "Shimla", "Jammu", "Srinagar",
    "Panaji", "Margao",
    "Nagpur", "Nasik", "Aurangabad",
    "Coimbatore", "Madurai", "Salem", "Tiruchirappalli"
]



# ---------------- PREDICTION FUNCTION ----------------
def predict_price():
    try:
        data = {
            "car_make": car_make.get(),
            "car_model": car_model.get(),
            "car_age": float(car_age.get()),
            "engine": float(engine.get()),
            "fuel_type": fuel_type.get(),
            "kilometers_driven": float(km_driven.get()),
            "location": location.get(),
            "mileage": float(mileage.get()),
            "power": float(power.get()),
            "region": region.get(),
            "seats": float(seats.get()),
            "transmission": transmission.get()
        }

        df = pd.DataFrame([data])
        df_enc = pd.get_dummies(df)

        missing = list(set(feature_cols) - set(df_enc.columns))
        df_missing = pd.DataFrame(0, index=df_enc.index, columns=missing)

        df_final = pd.concat([df_enc, df_missing], axis=1)[feature_cols]

        price = model.predict(df_final)[0]
        price_lakh = price / 100000

        messagebox.showinfo("Predicted Price", 
                            f"Price: ₹ {price:,.0f}\n({price_lakh:.2f} Lakhs)")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------- TKINTER UI ----------------
root = tk.Tk()
root.title("Used Car Price Predictor")
root.geometry("850x550")
root.configure(bg="#f2f2f2")

title = tk.Label(root, text="Car Price Prediction", font=("Arial", 22, "bold"), bg="#f2f2f2")
title.pack(pady=20)

form_frame = tk.Frame(root, bg="#f2f2f2")
form_frame.pack()

# Left & Right Columns
left = tk.Frame(form_frame, bg="#f2f2f2")
left.grid(row=0, column=0, padx=40)

right = tk.Frame(form_frame, bg="#f2f2f2")
right.grid(row=0, column=1, padx=40)


# Helper Functions
def make_field(parent, label):
    frame = tk.Frame(parent, bg="#f2f2f2")
    frame.pack(pady=8, anchor="w")
    tk.Label(frame, text=label, font=("Arial", 12), bg="#f2f2f2").pack(anchor="w")
    entry = tk.Entry(frame, width=25, font=("Arial", 12))
    entry.pack()
    return entry

def make_dropdown(parent, label, options):
    frame = tk.Frame(parent, bg="#f2f2f2")
    frame.pack(pady=8, anchor="w")
    tk.Label(frame, text=label, font=("Arial", 12), bg="#f2f2f2").pack(anchor="w")
    box = ttk.Combobox(frame, values=options, width=22, state="readonly", font=("Arial", 12))
    box.pack()
    return box


# LEFT INPUTS
car_make = make_dropdown(left, "Car Make:", list(brand_models.keys()))

# DYNAMIC MODEL DROPDOWN (initial empty)
car_model = make_dropdown(left, "Car Model:", [])

car_age = make_field(left, "Car Age (years):")
engine = make_field(left, "Engine CC:")
fuel_type = make_dropdown(left, "Fuel Type:", ["Petrol", "Diesel"])
km_driven = make_field(left, "Kilometers Driven:")

# RIGHT INPUTS
location = make_dropdown(right, "Location:", location_list)
mileage = make_field(right, "Mileage (km/l):")
power = make_field(right, "Power (BHP):")
region = make_dropdown(right, "Region:", ["North", "South", "East", "West"])
seats = make_field(right, "Seats:")
transmission = make_dropdown(right, "Transmission:", ["Manual", "Automatic"])


# ---------------- UPDATE MODEL LIST BASED ON BRAND ----------------
def update_models(event):
    brand = car_make.get()
    models = brand_models.get(brand, [])
    car_model["values"] = models
    if models:
        car_model.current(0)

car_make.bind("<<ComboboxSelected>>", update_models)


# Predict Button
predict_btn = tk.Button(root, text="Predict Price", font=("Arial", 16, "bold"),
                        bg="#4CAF50", fg="white", width=20, command=predict_price)
predict_btn.pack(pady=30)

root.mainloop()
