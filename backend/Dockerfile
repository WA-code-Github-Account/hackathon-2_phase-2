FROM python:3.11-slim
WORKDIR /app
COPY . .
# Set environment variables
ENV DATABASE_URL="postgresql+asyncpg://postgres.iplmjayxpkqwkmbxjaie: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@aws-1-ap-southeast-2.pooler.supabase.com:5432/postgres"
ENV BETTER_AUTH_SECRET="your-super-secret-jwt-token-for-dev-environment-change-in-production"
ENV BETTER_AUTH_URL="https://wahi786-todo-backend.hf.space"
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 7860
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]