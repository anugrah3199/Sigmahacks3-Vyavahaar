from fastapi import FastAPI, Form, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import aiofiles
import shutil
import os
from fer import FER
import matplotlib.pyplot as plt

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def getRoot():
    async with aiofiles.open("templates/", mode="r") as f:
        data = await f.read()
    return data


@app.get("/user", response_class=HTMLResponse)
async def getUser():
    async with aiofiles.open("templates/", mode="r") as f:
        data = await f.read()
    return data


@app.get("/login", response_class=HTMLResponse)
async def getlogin():
    async with aiofiles.open("templates/", mode="r") as f:
        data = await f.read()
    return data


@app.get("/signup", response_class=HTMLResponse)
async def getsignup():
    async with aiofiles.open("templates/", mode="r") as f:
        data = await f.read()
    return data


@app.get("/photo", response_class=HTMLResponse)
async def getPhoto():
    async with aiofiles.open("templates/capture.html", mode="r") as f:
        data = await f.read()
    return data


@app.get('/detect', response_class=HTMLResponse)
async def proceed():
    async with aiofiles.open("templates/", mode="r") as f:
        data = await f.read()
    return data


@app.get("/questionnaire", response_class=HTMLResponse)
async def getQuestionnaireHome():
    async with aiofiles.open("templates/", mode="r") as f:
        data = await f.read()
    return data


@app.get("/questionnaire/q", response_class=HTMLResponse)
async def getQuestionnaire():
    async with aiofiles.open("templates/", mode="r") as f:
        data = await f.read()
    return data


@app.get("/questionnaire/selfHelpAnxiety", response_class=HTMLResponse)
async def getanxiety():
    async with aiofiles.open("templates/", mode="r") as f:
        data = await f.read()
    return data


@app.get("/questionnaire/selfHelpDepp", response_class=HTMLResponse)
async def getdepression():
    async with aiofiles.open("templates/", mode="r") as f:
        data = await f.read()
    return data


@app.get("/questionnaire/selfHelpStress", response_class=HTMLResponse)
async def getstress():
    async with aiofiles.open("templates/", mode="r") as f:
        data = await f.read()
    return data


@app.get("/vent", response_class=HTMLResponse)
async def getVent():
    async with aiofiles.open("templates/", mode="r") as f:
        data = await f.read()
    return data


@app.get("/gethelp", response_class=HTMLResponse)
async def gethelp():
    async with aiofiles.open("templates/", mode="r") as f:
        data = await f.read()
    return data


@app.get("/about", response_class=HTMLResponse)
async def getabout():
    async with aiofiles.open("templates/", mode="r") as f:
        data = await f.read()
    return data
