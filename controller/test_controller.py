from fastapi import APIRouter
from service.llm_service import LlmService


class TestController:
    router = APIRouter(prefix="/test")
    llm_service = LlmService()

    def __init__(self, llm_service=None):
        if type(llm_service) is LlmService:
            self.llm_service = llm_service
        self.router.add_api_route("/openai", self.query_gpt, methods=["GET"])

    def query_gpt(self, text: str):
        return self.llm_service.chat(text)

    @router.get("/")
    def test_method():
        return {"item": "test"}
