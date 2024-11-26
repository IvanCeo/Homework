from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.base_repo import BaseRepo
from app.models.companies_model import Company
from app.schemas.company_schemas import CompanySchema

class CompanyRepo(BaseRepo):

    async def get_all(self, session: AsyncSession) -> list [CompanySchema]:
        result = await session.execute(select(Company))
        return [
            CompanySchema.model_validate(company) for company in result.scalars().all()
        ]