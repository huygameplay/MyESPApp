FROM eclipse-temurin:8-jdk
RUN apt-get update && apt-get install -y python3 python3-pip wget
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt --break-system-packages || pip3 install -r requirements.txt
# Dùng Spigot 1.12.2 vì Paper xóa link rồi, Spigot vẫn chạy plugin y hệt Paper
RUN if [ ! -f paper.jar ]; then wget -O paper.jar https://download.getbukkit.org/spigot/spigot-1.12.2.jar; fi
RUN echo "eula=true" > eula.txt
CMD python3 app.py
