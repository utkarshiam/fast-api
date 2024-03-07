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
    auth_token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjNiYjg3ZGNhM2JjYjY5ZDcyYjZjYmExYjU5YjMzY2M1MjI5N2NhOGQiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiVXRrYXJzaCBVcGFkaHlheSIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NLZEdRR0djb01NQ0pCemszend0MDU5LU9FSDk4U3lnQnRhTk10TWpyZmM9czk2LWMiLCJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vaWRlb2dyYW0tcHJvZCIsImF1ZCI6ImlkZW9ncmFtLXByb2QiLCJhdXRoX3RpbWUiOjE3MDk3NjUwMjQsInVzZXJfaWQiOiJ6ejNuNW92ZFhpVWIzektvSkQwQ2x0SjNrVDYyIiwic3ViIjoienozbjVvdmRYaVViM3pLb0pEMENsdEoza1Q2MiIsImlhdCI6MTcwOTgzMjg4NiwiZXhwIjoxNzA5ODM2NDg2LCJlbWFpbCI6InV0a2Fyc2hkZXZvcEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJnb29nbGUuY29tIjpbIjExNzI5MzM2ODc4MzU5Mzg5MjIwOSJdLCJlbWFpbCI6WyJ1dGthcnNoZGV2b3BAZ21haWwuY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoiZ29vZ2xlLmNvbSJ9fQ.ECFHglUhTEM-CQrmJPVOXrIDwFVwy3zTO2NK6GjeEp6jIqWyZtroxLCOmlg6ydnmGbWX78dXIjl5U8q74aLh0Kk5JT2pyQ4aD3THTbKugZISvFObKJWiw_b21SgyD4GtmgdMv9kjiFwYhslB7VdPDm4ThDDbc3itVED6zZxUoU7KaWeWjVZW3kT9-m-x5b9Eey3QjUkzwlzzMccSytGWZKlxLT5l6jO4SimfzAwJX9pMZl0dEOpZx1N9F58Gb0UbjAQhFEiaH9kST_q9syNDjYJgHDgpKL1jEbIYd-9xmFsgvoz11gPOr_ZI9HdDEY04bab2h-7A45uH-3HjNdal0A"
    userId = "P505Y5C7SmSpwIz1AZOFcg"
    cookie = "_ga=GA1.1.905888928.1709760055; __cuid=249d22fa78a149ccbb2322411f5fc90d; amp_fef1e8=685f6be5-aa39-44a7-92a9-19a3e9b817d0R...1hoaqpc2l.1hoaqrk5o.7.1.8; __cf_bm=AAZR4ZcBoRPomCsyeYlHwurB7iaL0Ur407T4suakrO0-1709832883-1.0.1.1-toTJTUwq2EOetWG9eEEYKx2mo5GiyixvleLDcFDL8cM8lZB070g73cRHm7SIHqaxCgvkxOJ7ybPZz0qYCyWakA; cf_clearance=ToW7WAF9_l6zLrtEpD.AmoFReGuV0v9UXFLzEY.OoRc-1709832884-1.0.1.1-5Lbzz1dnstBUQ7tpIguewWaYEc1tYgMhTDDBrXSw07OGxmdUFoCJs3npUQrB9gY2NFqaCcQnRFhoYUxRAuERfQ; session_cookie=eyJhbGciOiJSUzI1NiIsImtpZCI6IkFrZEJodyJ9.eyJpc3MiOiJodHRwczovL3Nlc3Npb24uZmlyZWJhc2UuZ29vZ2xlLmNvbS9pZGVvZ3JhbS1wcm9kIiwibmFtZSI6IlV0a2Fyc2ggVXBhZGh5YXkiLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUNnOG9jS2RHUUdHY29NTUNKQnprM3p3dDA1OS1PRUg5OFN5Z0J0YU5NdE1qcmZjXHUwMDNkczk2LWMiLCJhdWQiOiJpZGVvZ3JhbS1wcm9kIiwiYXV0aF90aW1lIjoxNzA5NzY1MDI0LCJ1c2VyX2lkIjoienozbjVvdmRYaVViM3pLb0pEMENsdEoza1Q2MiIsInN1YiI6Inp6M241b3ZkWGlVYjN6S29KRDBDbHRKM2tUNjIiLCJpYXQiOjE3MDk4MzI4ODYsImV4cCI6MTcxMTA0MjQ4NiwiZW1haWwiOiJ1dGthcnNoZGV2b3BAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZ29vZ2xlLmNvbSI6WyIxMTcyOTMzNjg3ODM1OTM4OTIyMDkiXSwiZW1haWwiOlsidXRrYXJzaGRldm9wQGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6Imdvb2dsZS5jb20ifX0.ViBJ-6xzDijEU5U8lG-AkLcIiIsLOfTkMSW0Ls8M5fCJKPMM9YNkyKaiFezvyz9dbWg0c3zdiavSa2lPHTtTPH3ak8ilbxuwbTgydS-DcQsNCbu2MPRIUjCr6E0MdvUHhrk73xj39X3NpWPzQguXTJFNAei1iPgHm3tm00ROJmEGYLuJwAA9mnSYtQI6GV2OaGN4HC8HOMq3LPF3ZYqgmdYrKWClzwg2YP1b2FaWHhV8p_HiY7SXtuAZXTSu6t0zwIIroy8hl9mTbMY0tSl3406MuEml7NC6LDgJIMa6hS6QuGnUu6OW_sBQolZjNx3iJlT-FXp5cjArPC1p0GxBlA; _ga_44J8R31CP6=GS1.1.1709832883.6.1.1709832893.0.0.0"
    i = ideo_image_creator.ImageGen(cookie, userId, auth_token)
    print(i.get_limit_left())
    image_urls = i.save_images(prompt, './output')

    return {"image_urls": image_urls}


@app.get("/get-book")
async def get_book(book_id: str):
    for book in BOOKS:
        if book.book_id == book_id:
            return book

    raise HTTPException(404, f"Book ID {book_id} not found in database.")
