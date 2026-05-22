# Smart_wound_monitoring_system_using_16-bit_riscv_FPGA
This project presents a Smart Wound Monitoring System designed to continuously monitor wound conditions using temperature and moisture sensing. The system processes real-time sensor data using a 16-bit RISC-V inspired soft-core processor implemented on FPGA, enabling early detection of abnormal wound conditions such as infection or improper healing.

The system integrates Arduino, FPGA (Gowin), UART communication, and a Python-based GUI to provide a complete end-to-end healthcare monitoring solution.

 Objectives
To develop a real-time wound monitoring system

To implement a 16-bit RISC-inspired processor on FPGA

To classify wound condition as High / Low / Normal

To provide low-cost and portable healthcare monitoring

Working Principle
The SHT3x sensor measures temperature and humidity (moisture).

Arduino reads sensor data using I²C protocol.

Data is sent as ASCII values via UART (e.g., 32,83).

FPGA receives data using UART RX module.

A parser converts ASCII into numerical values.

Data is stored in 16-bit registers inside the CPU.

The ALU performs threshold comparison:

Temp < 32 or Humidity < 30 → Low (L)

Temp > 37 or Humidity > 80 → High (H)

Otherwise → Normal (N)

Result is transmitted via UART TX.

Python GUI displays real-time output.

CPU Architecture (RISC-V Inspired)
Program Counter (PC)

Instruction Memory (IMEM)

Execute Unit / ALU

Register File (16-bit)

Control Logic

UART Interface

Note: This is a custom RISC-inspired soft core, not full ISA-compliant RISC-V.

Technologies Used
Verilog HDL

Icarus Verilog (Simulation)

GTKWave (Waveform Analysis)

Gowin FPGA

Arduino (Sensor Interface)

Python (GUI Visualization)

## 📜 License  

All Rights Reserved.  

This project is the intellectual property of the author.  
No part of this code may be copied, modified, or reused without permission.
