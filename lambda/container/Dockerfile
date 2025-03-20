FROM public.ecr.aws/lambda/python:3.12

COPY function/function.py function/requirements.txt /var/task/

RUN pip install -r requirements.txt

CMD ["function.handler"]