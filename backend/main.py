from typing import Union

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from classes import Data


app = FastAPI()

data = Data()

@app.get("/")
def read_root():
    return "Hello, world!"

@app.get('/algorithms', response_class=ORJSONResponse)
def get_all_algorithms():
    return ORJSONResponse(data.get_all_records())

@app.get('/algorithms/{algo_id}', response_class=ORJSONResponse)
def get_one_algorithm_by_id(algo_id:int):
    return ORJSONResponse(data.get_record_by_id(algo_id))

@app.get('algorithms/score')
def get_overal_score_all_algorithms():
    return {}

@app.get('algorithms/{algo_id}/score')
def get_score_for_algorithm(algo_id:int):
    return {}




