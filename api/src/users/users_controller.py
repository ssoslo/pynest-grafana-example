from nest.core import Controller, Get, Post, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.config import config


from .users_service import UsersService
from .users_model import Users


@Controller("users")
class UsersController:

    def __init__(self, users_service: UsersService):
        self.users_service = users_service

    @Get("/")
    async def get_users(self, session: AsyncSession = Depends(config.get_db)):
        return await self.users_service.get_users(session)

    @Post("/")
    async def add_users(self, users: Users, session: AsyncSession = Depends(config.get_db)):
        return await self.users_service.add_users(users, session)
 