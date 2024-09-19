from multiprocessing import Process, Manager
import androidcomm
import stmcomm



manager = Manager()
shared_queue = manager.Queue()  # Shared list to store messages between processes
ser = stmcomm.initialize_serial_connection()
# Create two processes: one for receiving from Android, one for sending to STM32
android_process = Process(target=androidcomm.read_bluetooth_messages, args=(shared_queue,))
stm32_process = Process(target=stmcomm.send_to_stm32, args=(shared_queue,ser))

# Start both processes
android_process.start()
stm32_process.start()

# Join the processes to the main process (wait for them to finish)
android_process.join()
stm32_process.join()
