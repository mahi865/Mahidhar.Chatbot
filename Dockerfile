# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Just in case you are using Mac Apple Silicon chips
RUN apt-get update && apt-get install -y libhdf5-dev  
RUN pip install --no-binary=h5py h5py

# Copy the reqs
COPY ./requirements.txt /app


# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 80 available to the world outside this container
EXPOSE 80

# Run flask_chatbot_app.py when the container launches
CMD ["python", "app.py"]
