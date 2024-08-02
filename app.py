import logging
import uvicorn
from dotenv import dotenv_values
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

env_vars = dotenv_values(".env")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)

app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "PUT", "DELETE"],
#     allow_headers=["*"],
# )


def main():
    logger.info('Logger configured')
    logger.info('Starting FastAPI application')
    uvicorn.run(app, port=8080, host='0.0.0.0', access_log=False)


if __name__ == '__main__':
    main()
