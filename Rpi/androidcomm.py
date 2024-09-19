import serial

def read_bluetooth_messages(shared_queue,device="/dev/rfcomm0", baudrate=9600):
    try:
        # Open the Bluetooth serial device
        with serial.Serial(device, baudrate, timeout=1) as bt_serial:
            print(f"Listening for messages from {device}...")
            while True:
                # Read up to 1024 bytes from the serial interface
                message = bt_serial.read(1024).strip()
                
                if message:
                    # Decode the message (UTF-8)
                    decoded_message = message.decode('utf-8')
                    print(f"Received message: {decoded_message}")
                    shared_queue.put(decoded_message)
    except serial.SerialException as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("Stopping listener.")
"""
if __name__ == "__main__":
    read_bluetooth_messages()
"""
