from fastapi import APIRouter, Depends
from starlette.responses import Response
from starlette.status import HTTP_404_NOT_FOUND, HTTP_409_CONFLICT, HTTP_201_CREATED
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.company_schemas import CompanySchema
from app.logger import logger
from app.services.company_service import company_service
from app.db import get_session


companies_router = APIRouter(tags=['companies'])


@companies_router.get('', response_model=list[CompanySchema] | None)
async def get_all_companies(session: AsyncSession = Depends(get_session)):
    all_companies = await company_service.get_all_companies()
    if not all_companies:
        return Response(status_code=HTTP_404_NOT_FOUND)
    return all_companies


@companies_router.post('', response_model=None)
async def create_company(request: CompanySchema, session: AsyncSession = Depends(get_session)):
    try:
        await company_service.add_company(request=request, session=session)
    except DuplicateException:
        logger.error('Company already exists')
        return Response(status_code=HTTP_409_CONFLICT)
    return Response(status_code=HTTP_201_CREATED)