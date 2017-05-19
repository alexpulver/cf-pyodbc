FROM python:2.7.13

RUN apt-get update && apt-get install -y unixodbc-dev

RUN mkdir -p /app

RUN wget -q -O - ftp://ftp.freetds.org/pub/freetds/stable/freetds-1.00.24.tar.gz | \
		tar -xzv --directory /tmp \
	&& cd /tmp/freetds-1.00.24 \
	&& ./configure \
		--prefix=/app/vendor \
		--with-tdsver=7.4 \
		--with-openssl \
	&& make \
	&& make install

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app/

# Gunicorn listens on port 8000 by default
EXPOSE 8000

WORKDIR /app
CMD ["gunicorn", "run:app", "--bind", "0.0.0.0", "--workers", "4"]
