# Netplan automatisierung

## prerequisites

you either need to have [graphviz](https://graphviz.org/download/) installed
or output to a .dot file and visualize it using another program or website, like [graphviz online](https://dreampuf.github.io/GraphvizOnline/)

## data formatting

data is provided using csv files
they are formatted like this

TASK_NR,TASK_LENGTH,TASK_PARENTS,TASK_CHILDREN

### example
```csv
1,5,,"2,3"
2,5,1,3
3,5,"1,2",
```
multiple values per field require quotes
multiple values are only allowed for the fields
TASK_PARENTS and TASK_CHILDREN


## usage
```shell
./create.py --input input.csv --output out.png
```
this creates an output image
```shell
./create.py --input input.csv --output out.dot
```
this creates an output dotfile

## example output
![out](https://user-images.githubusercontent.com/51709412/192847416-fc20051a-377c-48d2-9330-0692bfbaca66.png)
