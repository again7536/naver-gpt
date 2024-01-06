from openai import OpenAI
from config.openai import API_KEY
from model.chat import Chat, ChatFunctionCall
import json
from termcolor import cprint


class OpenAILlmRepository:
    client = OpenAI(api_key=API_KEY, timeout=2000, max_retries=2)
    model = "gpt-3.5-turbo"

    def __init__(self, client=None):
        if client is not None:
            self.client = client

    def chat(self, text, prompt: str, memory=[], tools=[]) -> Chat:
        cprint(memory, "red")
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "system", "content": prompt}] +
            memory + [{"role": "user", "content": text}],
            tools=tools,
        )

        message = response.choices[0].message
        content = message.content

        function_call = None
        if message.tool_calls is not None:
            tool_calls = message.tool_calls[0]
            function_call = ChatFunctionCall(
                id=tool_calls.id,
                name=tool_calls.function.name,
                params=json.loads(tool_calls.function.arguments)
            )

        return Chat(
            id=response.id,
            content=content,
            function_call=function_call
        )
