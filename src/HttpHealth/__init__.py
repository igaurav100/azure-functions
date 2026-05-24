import azure.functions as func
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(
        body="OK",
        status_code=200
    )