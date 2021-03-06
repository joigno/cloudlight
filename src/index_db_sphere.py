#!/usr/bin/python
'''
Created on Jun 29, 2010

@author: jose
'''

from cloudlight import BigGraph

import sys

filename =  len(sys.argv) > 1 and sys.argv[1] or None 

if not filename:
    print 'Error: first argument missing, input filename with BigGraph archive!'
    exit(-1)

type =  len(sys.argv) > 2 and sys.argv[2] or None 

if not type:
    print 'Error: second argument missing, input sphere type (link or node all )!'
    exit(-1)

lookahead =  len(sys.argv) > 3 and int(sys.argv[3]) or None 

if not lookahead and type != 'all': 
    print 'Error: third argument missing, input sphere lookahead (radius minus one)! lookahead 0 (zero) equals degree...'
    exit(-1)

# cache size in 2KB pages (?)
cache_size = 2**18

print 'opening BigGraph ' + filename
graph = BigGraph(filename, cache_size)
graph.debug = True

if type == 'link':
    
    print 'indexing with create_index_linksphere( lookahead  = %d)' % lookahead
    graph.create_index_linksphere(lookahead)
    
elif type == 'node':
    
    print 'indexing with create_index_nodesphere( lookahead  = %d)' % lookahead
    graph.create_index_nodesphere(lookahead)
    
elif type == 'all':
    
    #for lookahead in [1,2,3]:
    for lookahead in [1, 2]:
        
        print 'indexing with create_index_nodesphere( lookahead  = %d)' % lookahead
        graph.create_index_nodesphere(lookahead)

        print 'indexing with create_index_linksphere( lookahead  = %d)' % lookahead
        graph.create_index_linksphere(lookahead)
            
else:

    print 'Error: second argument malformed, input sphere type (link or node or all)! all for node and link spheres, lookaheads 1 and 2...'
    exit(-1)
        
                
        

