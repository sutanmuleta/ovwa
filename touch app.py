import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import requests

def get_weather_forecast():
    # Actual function to connect with OpenWeatherMap API
    api_key = "c4079613858d4e2235c25736a3ec6d92"  # Replace with your OpenWeatherMap API key
    city = destination_dropdown.get()
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()
    
    weather_text.delete(1.0, tk.END)
    
    if city and start_date and end_date:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
            weather_description = weather_data['weather'][0]['description']
            temperature = weather_data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
            
            weather_info = (
                f"Weather in {city}:\n"
                f"Description: {weather_description}\n"
                f"Temperature: {temperature:.2f}°C"
            )
            weather_text.insert(tk.END, weather_info)
        else:
            weather_text.insert(tk.END, "Failed to retrieve weather data.")
    else:
        weather_text.insert(tk.END, "Please enter destination and travel dates.")

def get_recommendations():
    # Mock function to simulate recommendations based on weather
    weather_info = weather_text.get(1.0, tk.END).strip()
    
    wardrobe_text.delete(1.0, tk.END)
    
    if "Weather in" in weather_info:
        if "rain" in weather_info.lower():
            recommendations = (
                "Wardrobe Recommendations:\n"
                "- Waterproof jacket\n"
                "- Umbrella\n"
                "- Waterproof boots\n"
            )
        elif "clear" in weather_info.lower():
            recommendations = (
                "Wardrobe Recommendations:\n"
                "- Sunglasses\n"
                "- Light t-shirts\n"
                "- Comfortable shoes\n"
            )
        else:
            recommendations = (
                "Wardrobe Recommendations:\n"
                "- General clothing based on temperature\n"
                "- Consider layers for changing conditions\n"
            )
        
        wardrobe_text.insert(tk.END, recommendations)
    else:
        wardrobe_text.insert(tk.END, "Please fetch the weather data first.")

def show_home():
    hide_all_frames()
    home_frame.pack(fill="both", expand=True)

def show_plan_trip():
    hide_all_frames()
    plan_trip_frame.pack(fill="both", expand=True)

def show_recommendations():
    hide_all_frames()
    recommendations_frame.pack(fill="both", expand=True)

def show_settings():
    hide_all_frames()
    settings_frame.pack(fill="both", expand=True)

def show_help():
    hide_all_frames()
    help_frame.pack(fill="both", expand=True)

def hide_all_frames():
    home_frame.pack_forget()
    plan_trip_frame.pack_forget()
    recommendations_frame.pack_forget()
    settings_frame.pack_forget()
    help_frame.pack_forget()

def create_main_window():
    root = tk.Tk()
    root.title("OVWA - Your Journey, Optimized")
    root.geometry("800x600")

    # Load images
    logo_image = tk.PhotoImage(file="logo.png")
    # You can load more images as needed

    # Header Section
    header_frame = tk.Frame(root, bg="lightblue")
    header_frame.pack(fill="x")

    logo_label = tk.Label(header_frame, image=logo_image, bg="lightblue")
    logo_label.image = logo_image  # Keep a reference to avoid garbage collection
    logo_label.pack(side="left", padx=10, pady=10)

    title_label = tk.Label(header_frame, text="OVWA - Your Journey, Optimized", font=("Arial", 24), bg="lightblue")
    title_label.pack(side="left", padx=10, pady=10)

    menu_frame = tk.Frame(header_frame, bg="lightblue")
    menu_frame.pack(side="right", padx=10, pady=10)

    home_button = tk.Button(menu_frame, text="Home", command=show_home)
    home_button.pack(side="left", padx=5)

    plan_trip_button = tk.Button(menu_frame, text="Plan Your Trip", command=show_plan_trip)
    plan_trip_button.pack(side="left", padx=5)

    recommendations_button = tk.Button(menu_frame, text="Recommendations", command=show_recommendations)
    recommendations_button.pack(side="left", padx=5)

    settings_button = tk.Button(menu_frame, text="Settings", command=show_settings)
    settings_button.pack(side="left", padx=5)

    help_button = tk.Button(menu_frame, text="Help", command=show_help)
    help_button.pack(side="left", padx=5)

    # Home Screen
    global home_frame
    home_frame = tk.Frame(root)
    home_frame.pack(fill="both", expand=True)

    welcome_label = tk.Label(home_frame, text="Welcome to OVWA! Simplify your travel planning with personalized recommendations.", font=("Arial", 18))
    welcome_label.pack(pady=20)

    quick_access_frame = tk.Frame(home_frame)
    quick_access_frame.pack(pady=20)

    plan_trip_quick_button = tk.Button(quick_access_frame, text="Plan Your Trip", command=show_plan_trip)
    plan_trip_quick_button.pack(side="left", padx=20)

    view_recommendations_button = tk.Button(quick_access_frame, text="View Recommendations", command=show_recommendations)
    view_recommendations_button.pack(side="left", padx=20)

    # Plan Your Trip Screen
    global plan_trip_frame
    plan_trip_frame = tk.Frame(root)

    destination_label = tk.Label(plan_trip_frame, text="Enter Destination")
    destination_label.pack(pady=5)
    destination_options = [
        "Paris", "New York", "Tokyo", "London", "Barcelona",
        "Rome", "Dubai", "Singapore", "Bangkok", "Istanbul",
        "Hong Kong", "Sydney", "Los Angeles", "Chicago",
        "San Francisco", "Amsterdam", "Toronto", "Berlin",
        "Vienna", "Moscow"
    ]
    global destination_dropdown
    destination_dropdown = ttk.Combobox(plan_trip_frame, values=destination_options)
    destination_dropdown.pack(pady=5)

    dates_label = tk.Label(plan_trip_frame, text="Select Travel Dates")
    dates_label.pack(pady=5)

    start_date_label = tk.Label(plan_trip_frame, text="Start Date")
    start_date_label.pack(pady=5)
    global start_date_entry
    start_date_entry = DateEntry(plan_trip_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
    start_date_entry.pack(pady=5)

    end_date_label = tk.Label(plan_trip_frame, text="End Date")
    end_date_label.pack(pady=5)
    global end_date_entry
    end_date_entry = DateEntry(plan_trip_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
    end_date_entry.pack(pady=5)

    submit_button = tk.Button(plan_trip_frame, text="Get Recommendations", command=lambda: [get_weather_forecast(), get_recommendations()])
    submit_button.pack(pady=20)

    weather_label = tk.Label(plan_trip_frame, text="Weather Forecast")
    weather_label.pack(pady=5)
    global weather_text
    weather_text = tk.Text(plan_trip_frame, height=10, width=50)
    weather_text.pack(pady=5)

    wardrobe_label = tk.Label(plan_trip_frame, text="Wardrobe Recommendations")
    wardrobe_label.pack(pady=5)
    global wardrobe_text
    wardrobe_text = tk.Text(plan_trip_frame, height=10, width=50)
    wardrobe_text.pack(pady=5)

    # Recommendations Screen
    global recommendations_frame
    recommendations_frame = tk.Frame(root)

    saved_recommendations_label = tk.Label(recommendations_frame, text="Your Saved Recommendations")
    saved_recommendations_label.pack(pady=5)
    saved_recommendations_listbox = tk.Listbox(recommendations_frame)
    saved_recommendations_listbox.pack(pady=5)

    recommendation_details_label = tk.Label(recommendations_frame, text="Recommendation Details")
    recommendation_details_label.pack(pady=5)
    recommendation_details_text = tk.Text(recommendations_frame, height=10, width=50)
    recommendation_details_text.pack(pady=5)

    # Settings Screen
    global settings_frame
    settings_frame = tk.Frame(root)

    language_label = tk.Label(settings_frame, text="Select Language")
    language_label.pack(pady=5)
    language_dropdown = ttk.Combobox(settings_frame, values=["English", "Spanish", "French"])
    language_dropdown.pack(pady=5)

    theme_label = tk.Label(settings_frame, text="Select Theme")
    theme_label.pack(pady=5)
    theme_dropdown = ttk.Combobox(settings_frame, values=["Light", "Dark"])
    theme_dropdown.pack(pady=5)

    notifications_var = tk.IntVar()
    notifications_checkbutton = tk.Checkbutton(settings_frame, text="Enable Notifications", variable=notifications_var)
    notifications_checkbutton.pack(pady=5)

    # Help Screen
    global help_frame
    help_frame = tk.Frame(root)

    faq_label = tk.Label(help_frame, text="Frequently Asked Questions")
    faq_label.pack(pady=5)
    faq_text = tk.Text(help_frame, height=10, width=50)
    faq_text.pack(pady=5)

    contact_support_label = tk.Label(help_frame, text="Need Help? Contact Us")
    contact_support_label.pack(pady=5)
    contact_support_button = tk.Button(help_frame, text="Send Email", command=lambda: messagebox.showinfo("Contact Us", "Email us at support@ovwa.com"))
    contact_support_button.pack(pady=5)

    # Footer Section
    footer_frame = tk.Frame(root, bg="lightgray")
    footer_frame.pack(fill="x", side="bottom")

    footer_label = tk.Label(footer_frame, text="© 2024 OVWA. All rights reserved.", bg="lightgray")
    footer_label.pack(side="left", padx=10, pady=5)

    privacy_policy_link = tk.Label(footer_frame, text="Privacy Policy", fg="blue", bg="lightgray", cursor="hand2")
    privacy_policy_link.pack(side="right", padx=10)

    terms_service_link = tk.Label(footer_frame, text="Terms of Service", fg="blue", bg="lightgray", cursor="hand2")
    terms_service_link.pack(side="right", padx=10)

    return root

if __name__ == "__main__":
    app = create_main_window()
    app.mainloop()
