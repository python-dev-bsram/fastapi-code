from schemas import bodySchemas, querySchemas, fromSchema

from fastapi import APIRouter, Body, Request, Header, Query, Cookie, Form
from fastapi.responses import JSONResponse
from typing_extensions import Annotated
from pydantic import Field
import json

demo = APIRouter()

# -----------------------------------------------------
# Annotating the parameters or schemas enables to validates the
# paramters automtaically and provides the readability the code
# we can use Annotation in the Query, Body, Headers, Cookies, Forms
# ----------------------------------------------------


# Annotate the Body
@demo.api_route("/body-api", methods=["POST"], response_model=bodySchemas.BodyData)
async def body_api(
    request: Request, body: Annotated[bodySchemas.BodyData, Body(embed=True)]
):

    return JSONResponse(status_code=200, content=body.model_dump())


# Annotate the Headers
@demo.api_route("/header-api", methods=["POST"])
async def header_api(
    request: Request, x_csrf_token: Annotated[str | None, Header()] = None
):
    headers = {"X-CSRF-Token": x_csrf_token}
    return JSONResponse(status_code=200, content=headers)


# Annotate the query parameters
@demo.api_route("/query-api", methods=["POST"])
async def query_api(query_params: Annotated[querySchemas.Filterdata, Query()]):
    return JSONResponse(status_code=200, content=query_params.model_dump())


# Annotate the Cookies
@demo.api_route("/cookie-api", methods={"GET"})
async def cookie_api(ads_id: Annotated[str | None, Cookie()] = None):
    return {"ads_id": ads_id}


# Annotate the FormData
@demo.api_route("/form-data", methods=["POST"], response_model=fromSchema.FormData)
async def form_data(data: Annotated[fromSchema.FormData, Form()]):
    return data
