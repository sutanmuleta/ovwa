import tkinter as tk
from tkinter import ttk

def create_main_window():
    root = tk.Tk()
    root.title("OVWA - Your Journey, Optimized")
    root.geometry("800x600")

    # Header Section
    header_frame = tk.Frame(root, bg="lightblue")
    header_frame.pack(fill="x")

    logo_label = tk.Label(header_frame, text="OVWA Logo", bg="lightblue")
    logo_label.pack(side="left", padx=10, pady=10)

    title_label = tk.Label(header_frame, text="OVWA - Your Journey, Optimized", font=("Arial", 24), bg="lightblue")
    title_label.pack(side="left", padx=10, pady=10)

    menu_frame = tk.Frame(header_frame, bg="lightblue")
    menu_frame.pack(side="right", padx=10, pady=10)

    home_button = tk.Button(menu_frame, text="Home")
    home_button.pack(side="left", padx=5)

    plan_trip_button = tk.Button(menu_frame, text="Plan Your Trip")
    plan_trip_button.pack(side="left", padx=5)

    recommendations_button = tk.Button(menu_frame, text="Recommendations")
    recommendations_button.pack(side="left", padx=5)

    settings_button = tk.Button(menu_frame, text="Settings")
    settings_button.pack(side="left", padx=5)

    help_button = tk.Button(menu_frame, text="Help")
    help_button.pack(side="left", padx=5)

    # Home Screen
    home_frame = tk.Frame(root)
    home_frame.pack(fill="both", expand=True)

    welcome_label = tk.Label(home_frame, text="Welcome to OVWA! Simplify your travel planning with personalized recommendations.", font=("Arial", 18))
    welcome_label.pack(pady=20)

    quick_access_frame = tk.Frame(home_frame)
    quick_access_frame.pack(pady=20)

    plan_trip_quick_button = tk.Button(quick_access_frame, text="Plan Your Trip")
    plan_trip_quick_button.pack(side="left", padx=20)

    view_recommendations_button = tk.Button(quick_access_frame, text="View Recommendations")
    view_recommendations_button.pack(side="left", padx=20)

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
