from nest.core import PyNestFactory, Module
from .config import config, PrometheusMiddleware, metrics, setting_otlp
from .app_controller import AppController
from .app_service import AppService
from src.users.users_module import UsersModule
import os
from src.users.users_module import UsersModule

APP_NAME = os.environ.get("APP_NAME", "api")
OTLP_GRPC_ENDPOINT = os.environ.get("OTLP_GRPC_ENDPOINT", "http://tempo:4317")


@Module(
    imports=[UsersModule, UsersModule],
    controllers=[AppController],
    providers=[AppService],
)
class AppModule:
    pass


app = PyNestFactory.create(
    AppModule,
    description="This is my Async PyNest app.",
    title="PyNest Application",
    version="1.0.0",
    debug=True,
)
http_server = app.get_server()
http_server.add_middleware(PrometheusMiddleware, app_name=APP_NAME)
http_server.add_route("/metrics", metrics)
setting_otlp(http_server, APP_NAME, OTLP_GRPC_ENDPOINT)


@http_server.on_event("startup")
async def startup():
    await config.create_all()
