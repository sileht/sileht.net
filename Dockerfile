FROM python:3

COPY . .
RUN python -m pip install -r requirements.txt
RUN pelican content -o output -s settings.py -d --ignore-cache

WORKDIR ./output
EXPOSE 8000
CMD exec python -m http.server
