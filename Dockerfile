FROM python:3.8-slim

WORKDIR /usr/src/app

COPY ./requirements.txt ./
RUN python3 -m venv myenv
RUN . myenv/bin/activate
RUN pip install --no-cache-dir -r requirements.txt

COPY ./ ./

CMD [ "python", "-m", "unittest"  ]