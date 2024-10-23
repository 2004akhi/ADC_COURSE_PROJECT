# Question : Implement AM modulation using Python .Plot the final waveform . 
# Also find out the Maximum and Minimum Modulated Voltage along with the Power

import numpy as np
import matplotlib.pyplot as plt

# Parameters
Ac = 1    # Carrier amplitude
Am = 0.5  # Modulating signal amplitude
#user input
#Ac = int(input("Enter the amplitude of the carrier signal (Ac): "))
#Am = int(input("Enter the amplitude of the modulating signal (Am): "))
fc = 100  # Carrier frequency (Hz)
fm = 5    # Modulating signal frequency (Hz)
duration = 1  # Duration of the signal in seconds
sampling_rate = 5000  # Samples per second
t = np.linspace(0, duration, int(sampling_rate * duration))  # Time array

# Generate carrier, modulating, and AM signals
carrier = Ac * np.cos(2 * np.pi * fc * t)  #c(t)=Ac *cos(2πfct)
modulating_signal = Am * np.cos(2 * np.pi * fm * t)  #m(t)=Am*cos(2πfmt)
modulation_index = Am / Ac # μ=Am/Ac
am_signal = (1 + modulation_index * (modulating_signal/Am)) * carrier  #s(t)=Ac[1+μcos(2πfmt)]cos(2πfct)

#Modulated Voltage
Vmax = Ac*(1+modulation_index)  # Vmax = Ac(1+μ)
Vmin = Ac*(1-modulation_index)  # Vmin = Ac(1−μ)

#Power
Pc = (Ac**2)/2                                       # R be 1 Ohm (Carrier Power ,Pc=Ac^2/2R )
Psb = ((modulation_index**2)*(Ac**2)) /8             # (Side Band Power ,Psb=(μ^2Ac^2)/8R )
Pt = ((Ac**2)/2)*(1+(modulation_index**2)/2)         # (Total Power , Pt = (Ac^2/2)(1+μ^2/2) )

# Plotting the signals
#plt.figure(figsize=(14, 10))

# Horizontal lines for Vmax and Vmin
#plt.axhline(y=Vmax, color='r', linestyle='--', label=f'Vmax = {Vmax:.2f}')
#plt.axhline(y=Vmin, color='b', linestyle='--', label=f'Vmin = {Vmin:.2f}')


# Plot the Modulating (Message) Signal
plt.subplot(3, 1, 1)
plt.plot(t, modulating_signal, color='blue', label="Modulating Signal (Message)")
plt.title('Message Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

# Plot the Carrier Signal
plt.subplot(3, 1, 2)
plt.plot(t, carrier, color='orange', label="Carrier Signal")
plt.title('Carrier Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

# Plot the AM Modulated Signal
plt.subplot(3, 1, 3)
plt.plot(t, am_signal, color='green', label="AM Signal")

# Horizontal lines for Vmax and Vmin
plt.axhline(y=Vmax, color='r', linestyle='--', label=f'Vmax = {Vmax:.2f}')
plt.axhline(y=Vmin, color='b', linestyle='--', label=f'Vmin = {Vmin:.2f}')

plt.title('AM Modulated Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

print(f"Maximum Modulated Voltage (Vmax): {Vmax:.2f}")
print(f"Minimum Modulated Voltage (Vmin): {Vmin:.2f}")

print(f"Carrier Power : {Pc:.2f} W")
print(f"Side Band Power : {Psb:.2f} W")
print(f"Total Power of the Modulated Signal: {Pt:.2f} W")

# Adjusting layout for better display
plt.tight_layout()
plt.show()
