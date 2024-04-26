# Table of Contents
[Graph 1](#graph-1)
- [Original Matrix](#original-graph-1-as-a-matrix)
- [Original Graph](#original-graph-1-as-a-graph)
- [Transitive Closure Matrix](#transitive-closure-of-graph-1)
- [Transitive Closure Graph](#transitive-closure-as-a-matrix-1)

[Graph 2](#graph-2)
- [Original Matrix](#original-graph-2-as-a-matrix)
- [Original Graph](#original-graph-2-as-a-graph)
- [Transitive Closure Matrix](#transitive-closure-of-graph-2)
- [Transitive Closure Graph](#transitive-closure-as-a-matrix-2)

[Graph 3](#graph-3)
- [Original Matrix](#original-graph-3-as-a-matrix)
- [Original Graph](#original-graph-3-as-a-graph)
- [Transitive Closure Matrix](#transitive-closure-of-graph-3)
- [Transitive Closure Graph](#transitive-closure-as-a-matrix-3)

[Graph 4](#graph-4)
- [Original Matrix](#original-graph-4-as-a-matrix)
- [Original Graph](#original-graph-4-as-a-graph)
- [Transitive Closure Matrix](#transitive-closure-of-graph-4)
- [Transitive Closure Graph](#transitive-closure-as-a-matrix-4)

[Graph 5](#graph-5)
- [Original Matrix](#original-graph-5-as-a-matrix)
- [Original Graph](#original-graph-5-as-a-graph)
- [Transitive Closure Matrix](#transitive-closure-of-graph-5)
- [Transitive Closure Graph](#transitive-closure-as-a-matrix-5)


# Graph 1
6 nodes

- Arc1-2
- Arc2-3
- Arc3-1
- Arc4-5
- Arc5-6
- Arc6-4

## Original Graph 1 as a Matrix:

    0 1 0 0 0 0 0 0
    0 0 1 0 0 0 0 0
    1 0 0 0 0 0 0 0
    0 0 0 0 1 0 0 0
    0 0 0 0 0 1 0 0
    0 0 0 1 0 0 0 0
    0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0

## Original Graph 1 as a Graph:

    0 -> 1;
    1 -> 2;
    2 -> 0;
    3 -> 4;
    4 -> 5;
    5 -> 3;

## Transitive Closure of Graph 1:

    0 1 0 0 0 0 0 0
    0 0 1 0 0 0 0 0
    1 0 0 0 0 0 0 0
    0 0 0 1 1 1 0 0
    0 0 0 1 1 1 0 0
    0 0 0 1 1 1 0 0
    0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0

## Transitive Closure as a Matrix:

    0 -> 1;
    1 -> 2;
    2 -> 0;
    3 -> 3;
    3 -> 4;
    3 -> 5;
    4 -> 3;
    4 -> 4;
    4 -> 5;
    5 -> 3;
    5 -> 4;
    5 -> 5;

# Graph 2
6 nodes
- Arc1-2
- Arc2-1
- Arc3-4
- Arc4-3
- Arc5-6
- Arc6-5

## Original Graph 2 as a Matrix:

    0 1 0 0 0 0 0 0
    1 0 0 0 0 0 0 0
    0 0 0 1 0 0 0 0
    0 0 1 0 0 0 0 0
    0 0 0 0 0 1 0 0
    0 0 0 0 1 0 0 0
    0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0

## Original Graph 2 as a Graph:

    0 -> 1;
    1 -> 0;
    2 -> 3;
    3 -> 2;
    4 -> 5;
    5 -> 4;


## Transitive Closure of Graph 2:

    0 1 0 0 0 0 0 0
    1 0 0 0 0 0 0 0
    0 0 1 1 0 0 0 0
    0 0 1 1 0 0 0 0
    0 0 0 0 1 1 0 0
    0 0 0 0 1 1 0 0
    0 0 0 0 0 0 0 0
    0 0 0 0 0 0 0 0

## Transitive Closure as a Matrix:

    0 -> 1;
    1 -> 0;
    2 -> 2;
    2 -> 3;
    3 -> 2;
    3 -> 3;
    4 -> 4;
    4 -> 5;
    5 -> 4;
    5 -> 5;

# Graph 3
8 nodes
- Arc 1-2
- Arc 2-3
- Arc 3-4
- Arc 4-5
- Arc 5-6
- Arc 6-7
- Arc 7-8

## Original Graph 3 as a Matrix:

    0 1 0 0 0 0 0 0
    0 0 1 0 0 0 0 0
    0 0 0 1 0 0 0 0
    0 0 0 0 1 0 0 0
    0 0 0 0 0 1 0 0
    0 0 0 0 0 0 1 0
    0 0 0 0 0 0 0 1
    0 0 0 0 0 0 0 0

## Original Graph 3 as a Graph:

    0 -> 1;
    1 -> 2;
    2 -> 3;
    3 -> 4;
    4 -> 5;
    5 -> 6;
    6 -> 7;

## Transitive Closure of Graph 3:

    0 1 0 0 0 0 0 0
    0 0 1 1 1 1 1 1
    0 0 0 1 1 1 1 1
    0 0 0 0 1 1 1 1
    0 0 0 0 0 1 1 1
    0 0 0 0 0 0 1 1
    0 0 0 0 0 0 0 1
    0 0 0 0 0 0 0 0

## Transitive Closure as a Matrix:

    0 -> 1;
    1 -> 2;
    1 -> 3;
    1 -> 4;
    1 -> 5;
    1 -> 6;
    1 -> 7;
    2 -> 3;
    2 -> 4;
    2 -> 5;
    2 -> 6;
    2 -> 7;
    3 -> 4;
    3 -> 5;
    3 -> 6;
    3 -> 7;
    4 -> 5;
    4 -> 6;
    4 -> 7;
    5 -> 6;
    5 -> 7;
    6 -> 7;

# Graph 4
8 nodes
- Arc 1-2
- Arc 2-3
- Arc 3-4
- Arc 5-6
- Arc 6-7
- Arc 7-8

## Original Graph 4 as a Matrix:

    0 1 0 0 0 0 0 0
    0 0 1 0 0 0 0 0
    0 0 0 1 0 0 0 0
    0 0 0 0 0 0 0 0
    0 0 0 0 0 1 0 0
    0 0 0 0 0 0 1 0
    0 0 0 0 0 0 0 1
    0 0 0 0 0 0 0 0

## Original Graph 4 as a Graph:

    0 -> 1;
    1 -> 2;
    2 -> 3;
    4 -> 5;
    5 -> 6;
    6 -> 7;


## Transitive Closure of Graph 4:

    0 1 0 0 0 0 0 0
    0 0 1 1 0 0 0 0
    0 0 0 1 0 0 0 0
    0 0 0 0 0 0 0 0
    0 0 0 0 0 1 1 1
    0 0 0 0 0 0 1 1
    0 0 0 0 0 0 0 1
    0 0 0 0 0 0 0 0

## Transitive Closure as a Matrix:

    0 -> 1;
    1 -> 2;
    1 -> 3;
    2 -> 3;
    4 -> 5;
    4 -> 6;
    4 -> 7;
    5 -> 6;
    5 -> 7;
    6 -> 7;

# Graph 5 
8 nodes
    - Arc1-2
    - Arc2-3
    - Arc3-4
    - Arc4-5
    - Arc5-6
    - Arc6-7
    - Arc7-8
    - Arc8-1

## Original Graph 5 as a Matrix:

    0 1 0 0 0 0 0 0
    0 0 1 0 0 0 0 0
    0 0 0 1 0 0 0 0
    0 0 0 0 1 0 0 0
    0 0 0 0 0 1 0 0
    0 0 0 0 0 0 1 0
    0 0 0 0 0 0 0 0
    1 0 0 0 0 0 0 0

## Original Graph 5 as a Graph:

    0 -> 1;
    1 -> 2;
    2 -> 3;
    3 -> 4;
    4 -> 5;
    5 -> 6;
    7 -> 0;

## Transitive Closure of Graph 5:

    0 1 0 0 0 0 0 0
    0 0 1 1 1 1 1 0
    0 0 0 1 1 1 1 0
    0 0 0 0 1 1 1 0
    0 0 0 0 0 1 1 0
    0 0 0 0 0 0 1 0
    0 0 0 0 0 0 0 0
    1 0 0 0 0 0 0 0

## Transitive Closure as a Matrix:

    0 -> 1;
    1 -> 2;
    1 -> 3;
    1 -> 4;
    1 -> 5;
    1 -> 6;
    2 -> 3;
    2 -> 4;
    2 -> 5;
    2 -> 6;
    3 -> 4;
    3 -> 5;
    3 -> 6;
    4 -> 5;
    4 -> 6;
    5 -> 6;
    7 -> 0;