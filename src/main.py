from pathlib import Path

from environs import Env
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from tokemon import tokemon, Provider, Mode, SUPPORTED_PROVIDERS

env = Env()
env.read_env()

app = FastAPI(title="Tokemon Demo", description="Token counting demo for tokemon library")

TEMPLATE_PATH = Path(__file__).parent / "templates" / "index.html"


class TokenCountRequest(BaseModel):
    provider: str = Field(..., description="LLM provider name")
    model: str = Field(..., description="Model name")
    text: str = Field(..., max_length=500, description="Text to tokenize")


class TokenCountResponse(BaseModel):
    token_count: int | None
    model: str
    provider: str
    error: str | None = None


@app.get("/", response_class=HTMLResponse)
async def index() -> HTMLResponse:
    html_content = TEMPLATE_PATH.read_text(encoding="utf-8")
    return HTMLResponse(content=html_content)


@app.get("/api/providers")
async def get_providers() -> dict[str, list[str]]:
    return SUPPORTED_PROVIDERS


@app.post("/api/count-tokens", response_model=TokenCountResponse)
async def count_tokens(request: TokenCountRequest) -> TokenCountResponse:
    is_openai = request.provider == Provider.OPENAI.value

    try:
        tokenizer = tokemon(
            model=request.model,
            provider=request.provider,
            mode=Mode.SYNC if is_openai else Mode.ASYNC,
        )

        if is_openai:
            response = tokenizer.count_tokens(request.text)
        else:
            response = await tokenizer.count_tokens(request.text)

        return TokenCountResponse(
            token_count=response.input_tokens,
            model=response.model,
            provider=response.provider,
        )
    except Exception as e:
        return TokenCountResponse(
            token_count=None,
            model=request.model,
            provider=request.provider,
            error=str(e),
        )
