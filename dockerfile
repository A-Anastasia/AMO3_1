FROM alpine
RUN apk add python3
RUN apk update
RUN apk add py-pip
RUN apk add py3-numpy
RUN apk add py3-pandas
RUN apk add py3-scikit-learn
COPY . /apps
WORKDIR /apps
CMD ["python3", "iris.py"]
