from shared.logging import get_logger

log = get_logger("BlobInvoiceProcessor")

def main(blob: bytes):
    size = len(blob)
    log("Invoice uploaded", size_bytes=size)

    if size == 0:
        raise ValueError("Empty file uploaded")

    log("Invoice processed successfully")