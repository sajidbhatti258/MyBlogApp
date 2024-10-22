# Step 1: Use an official Python base image
FROM python:3.12-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy requirements.txt to install dependencies
COPY requirements.txt /app/

# Step 4: Install dependencies
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade pip setuptools wheel
RUN pip install --prefer-binary --no-cache-dir -r requirements.txt


# Step 5: Copy the Django project files to the container
COPY . /app/

# Step 6: Expose the port your Django app runs on
EXPOSE 8000

# Step 7: Run the Django server (or entry point)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
