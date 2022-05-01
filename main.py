from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from func.fn_nf import nffn
from func.fn_dtv import dtv_fn
import uvicorn

###############################################
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
################################
@app.get('/')
def root():
    return RedirectResponse('/docs')

###############################################################
@app.get("/newsfirst")
async def news_first():
    return nffn()
###########################################################
@app.get("/derananews")
async def derana_news():
    return dtv_fn()
###########################################################

if __name__=='__main__':
  uvicorn.run(app,host='0.0.0.0',port=8080)