def crop_yield_predictor(): 
    area = float(input("Enter cultivated area (in acres): ")) 
    rainfall = float(input("Enter rainfall (in mm): ")) 
    fertilizer = float(input("Enter fertilizer used (in kg): ")) 
    yield_estimate = (0.8 * area) + (0.02 * rainfall) + (0.5 * fertilizer) 
    print(f"Estimated Crop Yield: {yield_estimate:.2f} quintals") 
def irrigation_scheduler(): 
    crop = input("Enter crop type (wheat/rice/maize): ").lower() 
    soil = input("Enter soil type (clay/loam/sandy): ").lower() 
    moisture = float(input("Enter current soil moisture (%): ")) 
    if crop == "wheat": 
        base_days = 7 
    elif crop == "rice": 
        base_days = 5 
    else: 
        base_days = 10 
    if soil == "sandy": 
        base_days -= 2 
    elif soil == "clay": 
        base_days += 1 
    if moisture < 30: 
        print("Recommendation: Irrigate today.") 
    else: 
        print(f"Recommendation: Next irrigation after {base_days} days.") 
def soil_health_monitor(): 
    ph = float(input("Enter soil pH value: ")) 
    nitrogen = float(input("Enter nitrogen level (in ppm): ")) 
    if 6.0 <= ph <= 7.5: 
        ph_status = "Optimal" 
    elif ph < 6.0: 
        ph_status = "Acidic" 
    else: 
        ph_status = "Alkaline" 
    if nitrogen < 50: 
        nitrogen_status = "Low" 
    elif nitrogen <= 100: 
        nitrogen_status = "Moderate" 
    else: 
        nitrogen_status = "High" 
    print(f"Soil pH Status: {ph_status}") 
    print(f"Nitrogen Level: {nitrogen_status}") 
def main_menu(): 
    while True: 
        print("\n====== Agriculture Assistant ======") 
        print("1. Crop Yield Predictor") 
        print("2. Irrigation Scheduler") 
        print("3. Soil Health Monitor") 
        print("4. Exit") 
        choice = input("Enter your choice (1-4): ") 
        if choice == '1': 
            crop_yield_predictor() 
        elif choice == '2': 
            irrigation_scheduler() 
        elif choice == '3': 
            soil_health_monitor() 
        elif choice == '4': 
            print("Exiting the program. Thank you!") 
            break 
        else: 
            print("Invalid choice! Please try again.")
main_menu()
    