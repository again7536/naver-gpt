NAVER_SERACH_TOOL = {
    "type": "function",
    "function": {
        "name": "search",
        "description": "search data from website",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The query key to search data from website",
                },
                "section": {
                    "type": "string",
                    "enum": ["blog", "local"],
                    "description": "The section from which you get data. The blog section is good to find personal reviews. The local section is good to find exact places."},
            },
            "required": ["query", "section"],
        },
    }
}
