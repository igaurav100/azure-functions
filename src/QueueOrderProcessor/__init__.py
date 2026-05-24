from shared.logging import get_logger

log = get_logger("QueueOrderProcessor")

def main(msg: str):
    log("Queue message received", payload=msg)

    # Process order (email, payment, inventory)
    log("Order processed successfully")