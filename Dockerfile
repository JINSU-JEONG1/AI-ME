# Step 1 : build stage (builder)
FROM python:3.12-slim AS builder
# uv 설치
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
WORKDIR /app
# 의존성 파일 복사 및 설치 (캐싱 활용)
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

# Step 2 : run stage (runner)
FROM python:3.12-slim
WORKDIR /app
# 빌드 단계에서 생성된 가상환경만 복사
COPY --from=builder /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"
# 소스 코드 복사
COPY ./app /app/app
# 보안: root 권한이 아닌 별도 유저로 실행 
RUN useradd -m appuser
USER appuser
# 실행 (Port 8000)
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]