import azure.functions as func
import json
from shared.validation import require_fields
from shared.logging import get_logger

log = get_logger("HttpOrders")

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        body = req.get_json()
        require_fields(body, ["orderId", "amount"])

        order_id = body["orderId"]
        amount = body["amount"]

        log("Order received", orderId=order_id, amount=amount)

        return func.HttpResponse(
            json.dumps({"status": "accepted", "orderId": order_id}),
            mimetype="application/json",
            status_code=202
        )

    except Exception as ex:
        log("Order failed", error=str(ex))
        return func.HttpResponse(
            json.dumps({"error": str(ex)}),
            status_code=400
        )