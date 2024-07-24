from uvicorn import run

from src.application.api.app import get_app

if __name__ == '__main__':
    run(get_app())