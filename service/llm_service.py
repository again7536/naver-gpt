from repository.llm_repository import LlmRepository
from repository.search_repository import SearchRepository
from config.app import PROMPT, MAX_RECURSION
from tools.naver_search import NAVER_SERACH_TOOL
import json


class LlmService:
    MAX_RECURSION = MAX_RECURSION
    llm_repository = LlmRepository()
    search_repository = SearchRepository()

    tools = [NAVER_SERACH_TOOL]
    functions = {}

    def __init__(self, llm_repository=None, search_repository=None):
        if type(llm_repository) is LlmRepository:
            self.llm_repository = llm_repository
        if type(search_repository) is SearchRepository:
            self.search_repository = search_repository

        self.functions["search"] = self.search_repository.search

    def chat(self, text, memory=[], tools=tools):
        chat = None

        for _ in range(self.MAX_RECURSION):
            chat = self.llm_repository.chat(text, PROMPT, memory, tools)

            if chat.content is not None:
                return chat.content

            # function call
            result = self.functions[chat.function_call.name](
                **chat.function_call.params)

            memory.append({
                "role": "assistant",
                "content": None,
                "tool_calls": [
                    {
                        "id": chat.function_call.id,
                        "type": "function",
                        "function": {
                          "name": chat.function_call.name,
                          "arguments": json.dumps(chat.function_call.params, ensure_ascii=False)
                          }
                    }
                ]
            })
            memory.append({
                "role": "tool",
                "content": json.dumps(result, ensure_ascii=False),
                "tool_call_id": chat.function_call.id
            })

        return chat
