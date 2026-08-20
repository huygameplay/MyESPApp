FROM openjdk:8-jdk
RUN apt-get update && apt-get install -y python3 python3-pip
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt --break-system-packages
# Tự tải Paper 1.12.2 nếu chưa có
RUN if [ ! -f paper.jar ]; then wget -O paper.jar https://api.papermc.io/v2/projects/paper/versions/1.12.2/builds/1620/downloads/paper-1.12.2-1620.jar; fi
CMD python3 app.py
