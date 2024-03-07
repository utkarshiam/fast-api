import json
import os
from typing import Literal, Optional
from uuid import uuid4
from fastapi import FastAPI, HTTPException
import random
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from mangum import Mangum
from IdeoImageCreator import ideo as ideo_image_creator

class Book(BaseModel):
    name: str
    genre: Literal["fiction", "non-fiction"]
    price: float
    book_id: Optional[str] = uuid4().hex


BOOKS_FILE = "books.json"
BOOKS = []

if os.path.exists(BOOKS_FILE):
    with open(BOOKS_FILE, "r") as f:
        BOOKS = json.load(f)

app = FastAPI()
handler = Mangum(app)


@app.get("/")
async def root():
    return {"message": "Welcome to my bookstore app!"}


@app.get("/random-book")
async def random_book():
    return random.choice(BOOKS)


@app.get("/list-books")
async def list_books():
    return {"books": BOOKS}


@app.get("/book_by_index/{index}")
async def book_by_index(index: int):
    if index < len(BOOKS):
        return BOOKS[index]
    else:
        raise HTTPException(404, f"Book index {index} out of range ({len(BOOKS)}).")


@app.post("/add-book")
async def add_book(book: Book):
    book.book_id = uuid4().hex
    json_book = jsonable_encoder(book)
    BOOKS.append(json_book)

    with open(BOOKS_FILE, "w") as f:
        json.dump(BOOKS, f)

    return {"book_id": book.book_id}

@app.get("/get-ideo")
async def get_ideo(prompt:str):
    print(prompt)
    i = ideo_image_creator.ImageGen('_ga=GA1.1.905888928.1709760055; __cuid=249d22fa78a149ccbb2322411f5fc90d; amp_fef1e8=685f6be5-aa39-44a7-92a9-19a3e9b817d0R...1hoaqpc2l.1hoaqrk5o.7.1.8; __cf_bm=lnu9gfn8IIU.dt.dU2frqxpJ8S.mFB0ExE3Mlna_gp8-1709765017-1.0.1.1-eI9LxNshnOUiS3tmdidfFfXklzxSpvWRSaMyYgSnQyt7GUvdnwprR_d_LmGIq0C3xdylTobg1fu.kGltey8UvQ; cf_clearance=.sQVuOQPFPlMW9KU.gmCMP2R.E5FEcTpZMKoHZwvTqI-1709765017-1.0.1.1-CVqetqvQXXMyaDrCTPNsDXxg8B8r5ryvoEUyqtWrg8evxqf5gbstpG6Bpk8ukVaGYwB8M8n11JUC.8445UzGGw; session_cookie=eyJhbGciOiJSUzI1NiIsImtpZCI6IkFrZEJodyJ9.eyJpc3MiOiJodHRwczovL3Nlc3Npb24uZmlyZWJhc2UuZ29vZ2xlLmNvbS9pZGVvZ3JhbS1wcm9kIiwibmFtZSI6IlV0a2Fyc2ggVXBhZGh5YXkiLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUNnOG9jS2RHUUdHY29NTUNKQnprM3p3dDA1OS1PRUg5OFN5Z0J0YU5NdE1qcmZjXHUwMDNkczk2LWMiLCJhdWQiOiJpZGVvZ3JhbS1wcm9kIiwiYXV0aF90aW1lIjoxNzA5NzYwNzA3LCJ1c2VyX2lkIjoienozbjVvdmRYaVViM3pLb0pEMENsdEoza1Q2MiIsInN1YiI6Inp6M241b3ZkWGlVYjN6S29KRDBDbHRKM2tUNjIiLCJpYXQiOjE3MDk3NjUwMTksImV4cCI6MTcxMDk3NDYxOSwiZW1haWwiOiJ1dGthcnNoZGV2b3BAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZ29vZ2xlLmNvbSI6WyIxMTcyOTMzNjg3ODM1OTM4OTIyMDkiXSwiZW1haWwiOlsidXRrYXJzaGRldm9wQGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6Imdvb2dsZS5jb20ifX0.PZumsE8VgFhzPwBkvXd9YnT5N_WlX0-R9phKXnFibgOzFDuui-QwIfRtFRoC528TFA5iSHB58ox31kV4EjtGToNHZKaAz6HugLxsajoSASxm-mT35vUDyjFMZNkbCZbd4nEj7LYEsjsjIGubct0PQCEsc_CVeIY9GUhuGirznI_5S9PvdZ2cbXF7lZfPxExkrzOZVu-Lm2MWHoG59a1Y37vvG_e88QM9nc5r8VYYGvq_o_YL9YOAL3UcB0ZC0TXmFbteHBCHv5c6VXlgWFb4Z1_rLahzf-G4AOQKhV8JSC8SryIk_CAekvJnZd3mukdesQmhyt5U3TcPdfI_3e2EXw; _ga_44J8R31CP6=GS1.1.1709765017.2.1.1709765021.0.0.0', 'P505Y5C7SmSpwIz1AZOFcg', 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjNiYjg3ZGNhM2JjYjY5ZDcyYjZjYmExYjU5YjMzY2M1MjI5N2NhOGQiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiVXRrYXJzaCBVcGFkaHlheSIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NLZEdRR0djb01NQ0pCemszend0MDU5LU9FSDk4U3lnQnRhTk10TWpyZmM9czk2LWMiLCJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vaWRlb2dyYW0tcHJvZCIsImF1ZCI6ImlkZW9ncmFtLXByb2QiLCJhdXRoX3RpbWUiOjE3MDk3NjUwMjQsInVzZXJfaWQiOiJ6ejNuNW92ZFhpVWIzektvSkQwQ2x0SjNrVDYyIiwic3ViIjoienozbjVvdmRYaVViM3pLb0pEMENsdEoza1Q2MiIsImlhdCI6MTcwOTc2NTAyNCwiZXhwIjoxNzA5NzY4NjI0LCJlbWFpbCI6InV0a2Fyc2hkZXZvcEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJnb29nbGUuY29tIjpbIjExNzI5MzM2ODc4MzU5Mzg5MjIwOSJdLCJlbWFpbCI6WyJ1dGthcnNoZGV2b3BAZ21haWwuY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoiZ29vZ2xlLmNvbSJ9fQ.SNRaTrNIxcuNQLzbsRX_TAVsN4sNvOSAIqKiJovde1u2znSY4pV-XarDlZuRzDOhuSapo8pCy8sqI0e3EYk5OReMqeTKSobdvjwyCdoFmNy5gJtbA6rT89KTjCyoYaRF1934ESopioyPs91m04W6d7b62wefBASnKjfz4E0Kp5auBqMcTN-YX0hleiwzeum7m01pqxbaVop44GkTieusuTZnykxqHYJaJZ9HAZVMecHGJ_mxg4-jqxvxL4vgQpCYv0yvG_rQa-QzkFa6ZeJ_f_n66SxacAAZSjD3BREBa1GomWNC2g-AuWN0WXgUnD5G4Z1MayTjxAp2o_5ikfnlKg') # Replace 'cookie', 'user_id', and 'auth_token' with your own values
    # print(i.get_limit_left())
    image_urls = i.save_images(prompt, './output')

    return {"image_urls": image_urls}


@app.get("/get-book")
async def get_book(book_id: str):
    for book in BOOKS:
        if book.book_id == book_id:
            return book

    raise HTTPException(404, f"Book ID {book_id} not found in database.")
