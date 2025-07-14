import report
from tableformat import create_formatter, print_table
from stock import Stock
from timethis import timethis

def avg(x, *more):
    return float((x+sum(more))/(1+len(more)))

if __name__ == '__main__':

    @timethis
    def countdown(n):
        while n > 0:
            n -= 1
    
    @timethis
    def picovina(n):
        while n>0:
            n**3
            n-=0.1

    picovina(100)

    countdown(100)
    