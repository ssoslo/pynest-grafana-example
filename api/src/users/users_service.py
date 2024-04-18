from .users_model import Users
from .users_entity import Users as UsersEntity
from src.utils.decorators import async_db_request_handler
from nest.core import Injectable

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

@Injectable
class UsersService:

    @async_db_request_handler
    async def add_users(self, users: Users, session: AsyncSession):
        new_users = UsersEntity(
            **users.dict()
        )
        session.add(new_users)
        await session.commit()
        return new_users.id

    @async_db_request_handler
    async def get_users(self, session: AsyncSession):
        query = select(UsersEntity)
        result = await session.execute(query)
        return result.scalars().all()
