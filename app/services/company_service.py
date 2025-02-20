from sqlalchemy.ext.asyncio import AsyncSession

from app.logger import logger
from app.exceptions import SqlException
from app.repositories.company_repo import company_repo
from app.schemas.company_schemas import CompanySchema
from app.models.companies_model import Company


class CompanyService:

    def __init__(self):
        self.repo = company_repo



    async def get_all_companies(self, session: AsyncSession) -> list[CompanySchema]:
        companies = await self.repo.get_all(session=session)
        return companies
    
    async def add_company(self, request: CompanySchema, session: AsyncSession):
        company = Company(name=request.name, company_id=request.company_id)
        try:
            await self.repo.add(company=company, session=session)
        except SqlException as exc:
            logger.error('Company already exists')
            raise
    

company_service = CompanyService()