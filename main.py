from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from func.fn_nf import nffn
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

if __name__=='__main__':
  uvicorn.run(app,host='0.0.0.0',port=8080)