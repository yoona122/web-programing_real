from fastapi import FastAPI

import requests

app = FastAPI()




@app.get("/")
def root():
    URL = "https://bigdata.kepco.co.kr/openapi/v1/powerUsage/industryType.do?apiKey=mtJCVe56P691oLNQZWcw6qpja525iDOR66z2iAMN"

    contents = requests.get(URL).text

    return {"message":contents}


@app.get("/home")
def home():
    return {"message":"Home!"}
