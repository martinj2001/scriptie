from typing import Union

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from classes.data import Data
from classes.scorer import Scorer


app = FastAPI()

data = Data()
scorer = Scorer(data.df)

@app.get("/")
def read_root():
    return "Hello, world!"

@app.get('/algorithms', response_class=ORJSONResponse)
def get_all_algorithms():
    return ORJSONResponse(data.get_all_records())

@app.get('/algorithms/score', response_class=ORJSONResponse)
def get_overal_score_all_algorithms():
    
    return ORJSONResponse(scorer.get_overall_score().toJSON())

@app.get('/algorithms/{algo_id}', response_class=ORJSONResponse)
def get_one_algorithm_by_id(algo_id:int):
    return ORJSONResponse(data.get_record_by_id(algo_id))

@app.get('/algorithms/{algo_id}/score')
def get_score_for_algorithm(algo_id:int):
    return {}




