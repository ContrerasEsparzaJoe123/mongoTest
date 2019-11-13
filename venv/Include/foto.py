GPIO.setmode(GPIO.BOARD)
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://joec:that1guy2@cluster0-tlgse.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["parcial2"]
collection = db["posts"]

# define the pin that goes to the circuit
pin_to_circuit = 7


def rc_time(pin_to_circuit):
    count = 0

    # Output on the pin for
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    # Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)

    # Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count


# Catch when script is interrupted, cleanup correctly
try:
    # Main loop
    while True:
        print(rc_time(pin_to_circuit))
        post = {"Distanncia": str(rc_time(pin_to_circuit))}

        collection.insert_one(post)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()