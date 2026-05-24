from shared.logging import get_logger

log = get_logger("ServiceBusEvents")

def main(msg: str):
    log("Service Bus event received", event=msg)

    # Business workflow trigger
    log("Event handled successfully")