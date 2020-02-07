FROM python:3
COPY . /build
WORKDIR /build
RUN python -m pip install -r requirements.txt
RUN pelican content -o output -s settings.py -d --ignore-cache

FROM nginx
COPY --from=0  /build/output /usr/share/nginx/html
EXPOSE 80
