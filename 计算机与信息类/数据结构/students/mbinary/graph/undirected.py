''' mbinary
#########################################################################
# File : undirected.py
# Author: mbinary
# Mail: zhuheqin1@gmail.com
# Blog: https://mbinary.coding.me
# Github: https://github.com/mbinary
# Created Time: 2018-04-26  10:33
# Description:
#########################################################################
'''

from collections import Iterable,deque
class vertex:
    def __init__(self,mark,val=None):
        self.mark = mark
        self.val = val
        self.edges = {}
        self.isVisited = False
    def __getitem__(self,adjVertexMark):
        return self.edges[adjVertexMark]
    def __delitem__(self,k):
        del self.edges[k]
    def __iter__(self):
        return iter(self.edges.values())
    def __str__(self):
        return 'V'+str(self.mark)
    def __repr__(self):
        return str(self)
class edge:
    def __init__(self,adjVertexs, weight = 1):
        '''adjVertexs:tuple(v.mark,u.mark)'''
        self.weight = weight
        self.adjVertexs = adjVertexs
        self.isVisted = False
    def __add__(self,x):
        return self.weight +x
    def __radd__(self,x):
        return self+x
    def __getitem__(self,k):
        if k!=0 or k!=1:raise IndexError
        return self.adjVertexs[k]
    def __str__(self):
        return '--'+str(self.weight)+'--'
    def __repr__(self):
        return str(self)
    @property
    def v(self):
        return self.adjVertexs[0]
    @property
    def u(self):
        return self.adjVertexs[1]
class graph:
    def __init__(self): 
        self.vertexs = {}
        self.edges = {}
    def __getitem__(self,i): 
        return self.vertexs[i]
    def __setitem__(selfi,x):
        self.vertexs[i]= x
    def __iter__(self):
        return iter(self.vertexs)
    def __bool__(self):
        return len(self.vertexs)!=0
    def addVertex(self,vertexs):
        '''vertexs is a iterable or just a mark that marks the vertex,whichc can be every imutable type'''
        if not isinstance(vertexs,Iterable):vertexs=[vertexs]
        for i in vertexs:
            if  not isinstance(i,vertex) and  i not in self.vertexs:self.vertexs[i]= vertex(i)
            if isinstance(i,vertex) and  i not in self.vertexs:self.vertexs[i.mark]= i

    def __getVertex(self,v):
        if not isinstance(v,vertex):
            if v not in self.vertexs:
                self.vertexs[v]=vertex(v)
            return self.vertexs[v]
        return v
    def addEdge(self,v,u,weight = 1):
        v = self.__getVertex(v)
        u = self.__getVertex(u)
        for arc in v:
            if  u in arc.adjVertexs:return  #examine that if v,u have been already connected
        vertexs = (v,u)
        newEdge = edge (vertexs,weight)
        self.edges[vertexs] = newEdge
        v.edges[u] = newEdge
        u.edges[v] = newEdge        
    def delEdge(self,v,u):
        if not isinstance(v,vertex):v= self.vertexs[v]
        if not isinstance(u,vertex):u= self.vertexs[u]
        try:
            del v[u]
            del u[v]
        except:print("error!"+str(v)+','+str(u)+' arent adjacent now')
        del self.edges[(v,u)]       
    def revisit(self):
        for i in self.vertexs.values():
            i.isVisited = False
        for i in self.edges.values():
            i.isVisited = False
    def __str__(self):
        arcs= list(self.edges.keys())
        arcs=[str(i[0])+str(self.edges[i])+str(i[1]) for i in arcs]
        s= '\n'.join(arcs)
        return s
    def __repr__(self):
        return str(self)
    def minPath(self,v,u):
        v=self.__getVertex(v)
        u=self.__getVertex(u)
        q=deque([v])
        last={i:None for i in self.vertexs.values()}
        last[v] = 0
        ds={i:1000000 for i in self.vertexs.values()}
        ds[v]=0
        while len(q)!=0:
            nd = q.popleft()
            nd.isVisited=True
            for edge  in nd:
                tgt=None
                if edge.v==nd:
                    tgt = edge.u
                else:tgt = edge.v
                tmp=ds[nd]+edge
                if ds[tgt] >tmp:
                    ds[tgt]=tmp
                    last[tgt] = nd
                if not tgt.isVisited:q.append(tgt)
        '''
        cur = u
        while cur !=v:
            print(str(cur)+'<---',end='')
            cur =last[cur]
        print(str(v))
        '''
        return ds[u]
    def hasCircle(self):
        pass
    def display(self):
        print('vertexs')
        for i in self.vertexs:
            print(i)
        print('edges')
        for i in self.edges:
            arc=self.edges[i]
            print(str(arc.v)+str(arc)+str(arc.u))               
        
if __name__=='__main__':
    n=int(input())
    while n>0:
        cities=int(input())
        n-=1
        g=graph()
        li={}
        for i in range(cities):
            li[input()]=i+1
            arc=int(input())
            for j in range(arc):
                s=input().split(' ')
                g.addEdge(i+1,int(s[0]),int(s[1]))
        ct  =int(input())
        for  i in range(ct):
            line = input()
            line= line .split(' ')
            v,u = li[line[0]],li[line[1]]
            print(g.minPath(v,u))
            g.revisit()
#http://www.spoj.com/submit/SHPATH/id=20525991
'''
1
4
gdansk
2
2 1
3 3
bydgoszcz
3
1 1
3 1
4 4
torun
3
1 3
2 1
4 1
warszawa
2
2 4
3 1
2
gdansk warszawa
bydgoszcz warszawa
V4<---V3<---V2<---V1
3
V4<---V3<---V2
2
>>> 
'''
