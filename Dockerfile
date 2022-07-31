FROM openjdk:11

RUN apt update -y
RUN apt upgrade -y
RUN apt install python3-dev unzip python3-pip python3 -y

COPY jdk-17_linux-x64_bin.tar.gz /tmp/
COPY siddhi-sdk-5.1.2.zip /tmp/
COPY siddhi-python-api-proxy-5.1.0.jar /tmp/
COPY ./requirements.txt /tmp/

RUN pip install --no-cache-dir -r /tmp/requirements.txt
RUN mkdir -p /usr/lib/jvm
RUN mkdir -p /usr/siddhi/sdk/
RUN tar zxvf /tmp/jdk-17_linux-x64_bin.tar.gz -C /usr/lib/jvm/
RUN update-alternatives --install "/usr/bin/java" "java" "/usr/lib/jvm/jdk-17.0.1/bin/java" 1
RUN update-alternatives --set java /usr/lib/jvm/jdk-17.0.1/bin/java
ENV JAVA_HOME=/usr/lib/jvm/jdk-17.0.1/bin
WORKDIR /tmp
RUN unzip ./siddhi-sdk-5.1.2.zip -d /usr/siddhi/sdk/
COPY ./siddhi-python-api-proxy-5.1.0.jar /usr/siddhi/sdk/siddhi-sdk-5.1.2/lib/
ENV SIDDHISDK_HOME=/usr/siddhi/sdk/siddhi-sdk-5.1.2

WORKDIR /usr/src/app
COPY main.py ./

CMD [ "python3", "./main.py" ]
