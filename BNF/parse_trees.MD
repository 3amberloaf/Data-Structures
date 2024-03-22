# Parse Trees using BNF

**Example**

```go
<statments> -> <statement> | <statement><statements>
<statement> -> <assign>; | <if-statement>
<assign> -> id = id
<if-statement> -> if(<boolean_expression>)<statement> 
                | if(<boolean_expression>)<statement> else<statement>
<boolean_expression> -> id == id
```

**Derivation**

```go
<statments> => <statement><statements>
            => <assign>; <statments>
            => id = id; <statements>
            => id = id; <statement>
            => id = id; <if-statement>
            => id = id; if(<boolean_expression>)<statement> else<statement>
            => id = id; if (id == id) <statement> else <statement>
            => id = id; if(id == id) <assign;> else <statement>
            => id = id; if(id == id) id = id; else <statement>
            => id = id; if(id == id) id = id; else <assign>;
            => id = id; if(id == id) id = id; else id = id;
```

This final sentance is equal to the following code:

`threshold = userInput;
if(threshold == criticalValue)
    result = specialValue;
else
    result = userInput;`

**Parse Tree**
                                    <statements>
                                    /           \
                            <statement>         <statements>
                            /                      \
                        <assign>;                   <statement>
                        /                               \
                    id = id                             <if-statement>
                                                           \
                                if(<boolean_expression>)<statement> else<statement> 
                                       /                    /               \
                                    id == id            <assign>;           <assign>;
                                                            /                   \
                                                        id = id             id = id


# Ambiguous Grammer

Issue is the whitespace! Some languages account for it while others do not. 

`if(value == best)
    if(update == userUpdate)
        userBest = value;
    else
        groupBest = value;`

will be compiled differently than

`if(value == best)
    if(update == userUpdate)
        userBest = value;
else
    groupBest = value;`

# Unambiguous Grammer

Problem: if(<boolean_expression>)<statement> else<statement> 

There can be repeated <if-statement> nested in <statement>, leading to ambiguity.

Solution: Redefine an individual statement

```go
<statements> -> <statement> | <statement><statements>
<statement> -> <matched> | <unmatched>
<matched> -> <assign>; | <if(<boolean_expression>)<matched> else<matched>
<unmatched> -> if(<boolean_expression>) <statement> 
               | if(<boolean_expression>)<matched> else<unmatched>
<assign> -> id = id
<boolnea_expression> -> id == id
```

if(value==best)if(update == userUpdate) userBest = value; else groupBest= value;
     |                      |                   |                       |
<boolean_expression>    <boolean_expression>    <assign>            <assign>
                                                    |                   |
                                                <matched>           <matched>
                                    \               |                   /
                                                <matched>
                                                    |
                                                <statement>
        \                                        /
                    <unmatched>
                          |
                    <statement>
                          |
                    <statements>