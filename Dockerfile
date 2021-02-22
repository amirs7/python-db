FROM python:3

WORKDIR /usr/src/app

COPY ./ ./
RUN python3 -m venv myenv
RUN . myenv/bin/activate
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "-m", "unittest"  ]