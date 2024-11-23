from fastapi import APIRouter
from app.logger import logger

companies_router = APIRouter(tags=['companies'])


@companies_router.get('/')
async def get_all_companies():
    logger.info('My endpoint get all companies')
    return {'message': 'get all companies'}


@companies_router.post('/')
async def create_new_company():
    return 'OK'