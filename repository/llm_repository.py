from repository.concrete.openai_llm_repository import OpenAILlmRepository
from model.chat import Chat


class LlmRepository:
    llm_repository = OpenAILlmRepository()

    def __init__(self, impl=None):
        if impl is not None:
            self.llm_repository = impl

    def chat(self, text, prompt: str, memory=[], tools=[]) -> Chat:
        return self.llm_repository.chat(text, prompt, memory, tools)
