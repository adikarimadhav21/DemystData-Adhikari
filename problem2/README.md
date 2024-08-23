
## Problem2
### Madhav Adhikari
### Description:
dajkkkkkkkkkkkkkkkkkkkkkkkk with example input output

python -m problem2.test.test_anonymise_data
docker run --name problem1 -v output:/app/problem1/data/output problem1_fixedwidth_converter  
docker build -f Dockerfile.problem1 -t problem1_fixedwidth_converter . 


docker run --name problem2 -v output:/app/problem2/data/output problem2_anonymise_local  
docker build -f Dockerfile.problem2local -t problem2_anonymise_local . 

docker build -f Dockerfile.problem2spark -t problem2_anonymise_spark .
docker run --name problem22 -v output:/app/problem2/data/output problem2_anonymise_spark   
