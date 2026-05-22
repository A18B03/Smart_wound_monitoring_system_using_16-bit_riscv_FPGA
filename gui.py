import serial
import tkinter as tk
import re

# =====================================
# SERIAL PORT
# =====================================
ser = serial.Serial('COM7', 115200, timeout=1)

# =====================================
# WINDOW
# =====================================
root = tk.Tk()
root.title("Wound Monitor")
root.geometry("700x520")
root.configure(bg="white")

# =====================================
# TITLE
# =====================================
title = tk.Label(
    root,
    text="WOUND MONITOR",
    font=("Arial", 24, "bold"),
    bg="white"
)
title.pack(pady=15)

# =====================================
# VALUES
# =====================================
temp_label = tk.Label(
    root,
    text="Temperature: -- °C",
    font=("Arial", 18),
    bg="white"
)
temp_label.pack(pady=10)

moist_label = tk.Label(
    root,
    text="Moisture: -- %",
    font=("Arial", 18),
    bg="white"
)
moist_label.pack(pady=10)

# =====================================
# TEMPERATURE STATUS
# =====================================
temp_status = tk.Label(
    root,
    text="Temperature Status: --",
    font=("Arial", 18, "bold"),
    bg="white"
)
temp_status.pack(pady=10)

temp_reason = tk.Label(
    root,
    text="",
    font=("Arial", 14),
    bg="white"
)
temp_reason.pack()

# =====================================
# MOISTURE STATUS
# =====================================
moist_status = tk.Label(
    root,
    text="Moisture Status: --",
    font=("Arial", 18, "bold"),
    bg="white"
)
moist_status.pack(pady=10)

moist_reason = tk.Label(
    root,
    text="",
    font=("Arial", 14),
    bg="white"
)
moist_reason.pack()

# =====================================
# OVERALL STATUS
# =====================================
overall = tk.Label(
    root,
    text="Overall: --",
    font=("Arial", 22, "bold"),
    bg="white"
)
overall.pack(pady=20)

# =====================================
# BUFFER
# =====================================
buffer = ""

# =====================================
# UPDATE FUNCTION
# =====================================
def update_data():
    global buffer

    try:
        data = ser.read(100).decode(errors='ignore')
        print("RAW:", data)

        buffer += data

        # Match format: 31,97 H
        matches = re.findall(r'(\d{2}),(\d{2})\s*([HNL])', buffer)

        for temp, moist, status in matches:

            t = int(temp)
            m = int(moist)

            temp_label.config(text=f"Temperature: {t} °C")
            moist_label.config(text=f"Moisture: {m} %")

            # -----------------------------
            # TEMPERATURE STATUS
            # -----------------------------
            if t > 37:
                temp_status.config(
                    text="Temperature Status: HIGH",
                    fg="red"
                )
                temp_reason.config(
                    text="Possible infection / inflammation",
                    fg="red"
                )

            elif t < 32:
                temp_status.config(
                    text="Temperature Status: LOW",
                    fg="blue"
                )
                temp_reason.config(
                    text="Possible ischemia / poor perfusion",
                    fg="blue"
                )

            else:
                temp_status.config(
                    text="Temperature Status: NORMAL",
                    fg="green"
                )
                temp_reason.config(
                    text="Normal wound surface temperature",
                    fg="green"
                )

            # -----------------------------
            # MOISTURE STATUS
            # -----------------------------
            if m > 80:
                moist_status.config(
                    text="Moisture Status: HIGH",
                    fg="red"
                )
                moist_reason.config(
                    text="Excess moisture / maceration risk",
                    fg="red"
                )

            elif m < 30:
                moist_status.config(
                    text="Moisture Status: LOW",
                    fg="blue"
                )
                moist_reason.config(
                    text="Wound too dry / delayed healing",
                    fg="blue"
                )

            else:
                moist_status.config(
                    text="Moisture Status: NORMAL",
                    fg="green"
                )
                moist_reason.config(
                    text="Optimal wound moisture",
                    fg="green"
                )

            # -----------------------------
            # OVERALL STATUS
            # -----------------------------
            if (32 <= t <= 37) and (30 <= m <= 80):
                overall.config(
                    text="Overall: OPTIMAL",
                    fg="green"
                )
            else:
                overall.config(
                    text="Overall: NEEDS ATTENTION",
                    fg="orange"
                )

        if len(buffer) > 200:
            buffer = buffer[-100:]

    except Exception as e:
        print("Error:", e)

    root.after(300, update_data)

# =====================================
# START
# =====================================
update_data()
root.mainloop()
