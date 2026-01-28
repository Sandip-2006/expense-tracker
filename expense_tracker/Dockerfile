# 1️⃣ Base image: Python already installed Linux
FROM python:3.11-slim

# 2️⃣ Python settings (Docker best practice)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3️⃣ Container ke andar working folder
WORKDIR /app

# 4️⃣ Sirf requirements pehle copy karo (fast rebuild ke liye)
COPY requirements.txt .

# 5️⃣ Python dependencies install karo
RUN pip install --no-cache-dir -r requirements.txt

# 6️⃣ Ab poora Django project copy karo
COPY . .

# 7️⃣ Django default port
EXPOSE 8000

# 8️⃣ Container start hote hi Django run ho
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# 10️⃣ Optional: Use a production-ready server like Gunicorn
CMD ["gunicorn", "expense_tracker.wsgi:application", "--bind", "0. 0.0.0:8000"]