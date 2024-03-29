from typing import Union, List


from fastapi import FastAPI, Query
from fastapi.responses import ORJSONResponse, Response
from fastapi.middleware.cors import CORSMiddleware

from classes.data import Data
from classes.scorer import Scorer

import jsonpickle

app = FastAPI()

origins = [
    'http://localhost:8080'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

data = Data()
scorer = Scorer()

@app.get("/")
def read_root():
    return "Hello, world!"

@app.get('/algorithms', response_class=ORJSONResponse)
def get_all_algorithms():
    return ORJSONResponse(data.get_all_records())

@app.get('/algorithms/score', response_class=ORJSONResponse)
def get_overal_score_all_algorithms(filterOrganizations: List[str] = Query(None), filterFields: List[str] = Query(None), version:str = Query(None)):
    print(filterOrganizations)
    print(filterFields)
    print(version)
    if filterOrganizations is not None or filterFields is not None:
        score = scorer.get_score(data.get_all_records_as_dataframe(filterOrganizations, filterFields))
    else:
        score = scorer.get_score(data.get_all_records_as_dataframe())
    return ORJSONResponse(score)

@app.get('/algorithms/{algo_id}', response_class=ORJSONResponse)
def get_one_algorithm_by_id(algo_id:int):
    return ORJSONResponse(data.get_record_by_id(algo_id))

@app.get('/algorithms/{algo_id}/score')
def get_score_for_algorithm(algo_id:int, filterOrganizations: List[str] = Query(None), filterFields: List[str] = Query(None)):
    print(filterOrganizations)
    score = scorer.get_score(data.get_record_by_id_as_dataframe(algo_id))
    return ORJSONResponse(score)

@app.get('/organizations')
def get_organizations():
    return ORJSONResponse(data.get_all_unique_organizations())

@app.get('/fields')
def get_fields():
    return ORJSONResponse(data.get_all_fields())


