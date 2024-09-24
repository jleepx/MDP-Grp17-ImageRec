import serial
import time

def initialize_serial_connection(port='/dev/ttyUSB1', baudrate=115200, timeout=1):
    """Initialize the serial connection."""
    return serial.Serial(port, baudrate=baudrate, timeout=timeout)


# A5 function to move stm to detect object, fail then move it left
# 4 steps: BW40, FL10, FW20, C170
def changeSide(ser):

    #Step 1 BW40
    message = "BW40"
    # Send the user input to STM32
    ser.write((message + '\n').encode('utf-8'))
    print(f"Sent: {message}")

    # Wait for STM32 response
    time.sleep(1)  # Adjust this based on STM32's response time

    if ser.in_waiting > 0:
        incoming_data = ser.readline().decode('utf-8').strip()
        print(f"Received from STM32: {incoming_data}")
    else:
    print("No data received.")
        time.sleep(0.5)

    #Step 2 FL10
    message = "FL10"
    # Send the user input to STM32
    ser.write((message + '\n').encode('utf-8'))
    print(f"Sent: {message}")

    # Wait for STM32 response
    time.sleep(1)  # Adjust this based on STM32's response time

    if ser.in_waiting > 0:
        incoming_data = ser.readline().decode('utf-8').strip()
        print(f"Received from STM32: {incoming_data}")
    else:
    print("No data received.")
        time.sleep(0.5)

    #Step 3 FW20
    message = "FW20"
    # Send the user input to STM32
    ser.write((message + '\n').encode('utf-8'))
    print(f"Sent: {message}")

    # Wait for STM32 response
    time.sleep(1)  # Adjust this based on STM32's response time

    if ser.in_waiting > 0:
        incoming_data = ser.readline().decode('utf-8').strip()
        print(f"Received from STM32: {incoming_data}")
    else:
    print("No data received.")
        time.sleep(0.5)

    #Step 4 C170
    message = "C170"
    # Send the user input to STM32
    ser.write((message + '\n').encode('utf-8'))
    print(f"Sent: {message}")

    # Wait for STM32 response
    time.sleep(1)  # Adjust this based on STM32's response time

    if ser.in_waiting > 0:
        incoming_data = ser.readline().decode('utf-8').strip()
        print(f"Received from STM32: {incoming_data}")
    else:
    print("No data received.")
        time.sleep(0.5)

    return;
#end of changeside function    

def send_to_stm32(shared_queue,ser):
    """Send data to STM32 and handle serial exceptions."""
    try:
        while True:
            if shared_queue:
                message = shared_queue.get()
                # Send the user input to STM32
                ser.write((message + '\n').encode('utf-8'))
                print(f"Sent: {message}")

                # Wait for STM32 response
                time.sleep(1)  # Adjust this based on STM32's response time

                if ser.in_waiting > 0:
                    incoming_data = ser.readline().decode('utf-8').strip()
                    print(f"Received from STM32: {incoming_data}")
                else:
                    print("No data received.")
            time.sleep(0.5)
            
    except serial.SerialException:
        print("Serial port issue, trying to reconnect...")
        reconnect_serial(ser)

def reconnect_serial(ser):
    """Close and reopen the serial connection to recover from an error."""
    try:
        ser.close()
        time.sleep(1)  # Wait for a moment before reopening
        ser.open()  # Attempt to reopen the serial connection
        print("Reconnected to the serial port.")
    except serial.SerialException:
        print(f"Failed to reconnect: {e}")
        initialize_serial_connection('/dev/ttyUSB1')
"""
if __name__ == "__main__":
    # Initialize the serial connection
    port = '/dev/ttyUSB0'  # Adjust based on your setup
    ser = initialize_serial_connection(port)

    try:
        while True:
            user_input = input("Enter string: ")

            if user_input.lower() == 'exit':
                print("Exiting program.")
                break

            # Send data to STM32
            send_to_stm32(ser, user_input)

    except KeyboardInterrupt:
        print("Communication stopped by user.")
    
    finally:
        ser.close()
        print("Serial connection closed.")
"""
