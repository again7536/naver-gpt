from dataclasses import dataclass


@dataclass
class ChatFunctionCall:
    id: int
    name: str
    params: object


@dataclass
class Chat:
    id: int
    content: str
    function_call: ChatFunctionCall
