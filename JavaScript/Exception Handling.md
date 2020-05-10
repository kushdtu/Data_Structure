# Exception Handling

This chapter describes how JavaScript's exception handling works. It begins with a general explanation of what exception handling is.

What Is Exception Handling?
---------------------------

In exception handling, you often group statements that are tightly coupled. If, while you are executing those statements, one of them causes an error, then it makes no sense to continue with the remaining statements. Instead, you try to recover from the error as gracefully as you can. This is loosely reminiscent of transactions (but without the atomicity).

Let's look at code without exception handling:

```javascript

function processFiles() {
    var fileNames = collectFileNames();
    var entries = extractAllEntries(fileNames);
    processEntries(entries);
}
function extractAllEntries(fileNames) {
    var allEntries = new Entries();
    fileNames.forEach(function (fileName) {
        var entry = extractOneEntry(fileName);
        allEntries.add(entry);  // (1)
    });
}
function extractOneEntry(fileName) {
    var file = openFile(fileName);  // (2)
    ...
}
...
```

What is the best way to react to an error in `openFile()` at (2)? Clearly, the statement (1) should not be executed anymore. But we wouldn't want to abort `extractAllEntries()`, either. Instead, it is enough to skip the current file and continue with the next one. To do that, we add exception handling to the previous code:

```javascript
function extractAllEntries(fileNames) {
    var allEntries = new Entries();
    fileNames.forEach(function (fileName) {
        try {
            var entry = extractOneEntry(fileName);
            allEntries.add(entry);
        } catch (exception) {  // (2)
            errorLog.log('Error in '+fileName, exception);
        }
    });
}
function extractOneEntry(fileName) {
    var file = openFile(fileName);
    ...
}
function openFile(fileName) {
    if (!exists(fileName)) {
        throw new Error('Could not find file '+fileName); // (1)
    }
    ...
}
```

There are two aspects to exception handling:

1. If there is a problem that can't be handled meaningfully where it occurs, throw an exception.
2. Find a place where errors can be handled: catch exceptions.

At (1), the following constructs are active:

```javascript
    processFile()
        extractAllEntries(...)
            fileNames.forEach(...)
                function (fileName) { ... }
                    try { ... } catch (exception) { ... }
                        extractOneEntry(...)
                            openFile(...)
```

The `throw` statement at (1) walks up that tree and leaves all constructs until it encounters an active `try` statement. It then invokes that statement's `catch` block and passes it the exception value.

Exception Handling in JavaScript
--------------------------------

Exception handling in JavaScript works like in most programming languages: a `try` statement groups statements and lets you intercept exceptions in those statements.

### throw

The syntax of `throw` is as follows:

```javascript
throw «value»;
```

Any JavaScript value can be thrown. For simplicity's sake, many JavaScript programs just throw strings:

```javascript
// Don't do this
if (somethingBadHappened) {
    throw 'Something bad happened';
}
```

Don't do this. JavaScript has special constructors for exception objects (see [Error Constructors](http://speakingjs.com/es5/ch14.html#error_constructors "Error Constructors")). Use those or subclass them (see [Chapter 28](http://speakingjs.com/es5/ch28.html "Chapter 28. Subclassing Built-ins")). Their advantage is that JavaScript automatically adds a stack trace (on most engines) and that they have room for additional context-specific properties. The simplest solution is to use the built-in constructor `Error()`:

```javascript
if (somethingBadHappened) {
    throw new Error('Something bad happened');
}
```

### try-catch-finally

The syntax of `try-catch-finally` looks as follows. `try` is mandatory, and at least one of `catch` and `finally` must be there, too:

```javascript
try {
    «try_statements»
}
⟦catch («exceptionVar») {
   «catch_statements»
}⟧
⟦finally {
   «finally_statements»
}⟧
```

Here's how it works:

- `catch` catches any exception that is thrown in `try_statements`, whether directly or in functions they invoke. Tip: If you want to distinguish between different kinds of exceptions, you can use the `constructor` property to switch over the exceptions' constructors (see [Use cases for the constructor property](http://speakingjs.com/es5/ch17.html#switch_constructor "Use cases for the constructor property")).
- `finally` is always executed, no matter what happens in `try_statements` (or in functions they invoke). Use it for clean-up operations that should always be performed, no matter what happens in `try_statements`:

    ```javascript
    var resource = allocateResource();
    try {
        ...
    } finally {
        resource.deallocate();
    }
    ```

    If one of the `try_statements` is a `return`, then the `finally` block is executed afterward (immediately before leaving the function or method; see the examples that follow).

### Examples

Any value can be thrown:

```javascript
function throwIt(exception) {
    try {
        throw exception;
    } catch (e) {
        console.log('Caught: '+e);
    }
}
```

Here is the interaction:

```javascript
> throwIt(3);
Caught: 3
> throwIt('hello');
Caught: hello
> throwIt(new Error('An error happened'));
Caught: Error: An error happened
```

`finally` is always executed:

```javascript
function throwsError() {
    throw new Error('Sorry...');
}
function cleansUp() {
    try {
        throwsError();
    } finally {
        console.log('Performing clean-up');
    }
}
```

Here is the interaction:

```javascript
> cleansUp();
Performing clean-up
Error: Sorry...
```

`finally` is executed *after* a `return` statement:

```javascript
function idLog(x) {
    try {
        console.log(x);
        return 'result';
    } finally {
        console.log("FINALLY");
    }
}
```

Here is the interaction:

```javascript
> idLog('arg')
arg
FINALLY
'result'
```

The return value is queued before executing `finally`:

```javascript
var count = 0;
function countUp() {
    try {
        return count;
    } finally {
        count++;  // (1)
    }
}
```

By the time statement (1) is executed, the value of `count` has already been queued for returning:

```javascript
> countUp()
0
> count
1
```

Error Constructors
------------------

ECMAScript standardizes the following error constructors. The descriptions are quoted from the ECMAScript 5 specification:

-   `Error` is a generic constructor for errors. All other error constructors mentioned here are subconstructors.
-   `EvalError` "is not currently used within this specification. This object remains for compatibility with previous editions of this specification."
-   `RangeError` "indicates a numeric value has exceeded the allowable range." For example:

    ```console
    > new Array(-1)
    RangeError: Invalid array length
    ```

-   `ReferenceError` "indicates that an invalid reference value has been detected." Usually, this is an unknown variable. For example:

    ```console
    > unknownVariable
    ReferenceError: unknownVariable is not defined
    ```

-   `SyntaxError` "indicates that a parsing error has occurred" either while parsing normal code or while parsing the argument of `eval()`. For example:

    ```console
    > 3..1
    SyntaxError: Unexpected number '.1'. Parse error.
    > eval('5 +')
    SyntaxError: Unexpected end of script
    ```

-   `TypeError` "indicates the actual type of an operand is different than the expected type." For example:

    ```console
    > undefined.foo
    TypeError: Cannot read property 'foo' of undefined
    ```

-   `URIError` "indicates that one of the global URI handling functions was used in a way that is incompatible with its definition." For example:

    ```console
    > decodeURI('%2')
    URIError: URI malformed
    ```

Here are the properties of errors:

`message`

The error message.

`name`

The name of the error.

`stack`

A stack trace. This is nonstandard, but is available on many platforms---for example, Chrome, Node.js, and Firefox.

Stack Traces
------------

The usual sources of errors are either external (wrong input, missing file, etc.) or internal (a bug in the program). Especially in the latter case, you will get unexpected exceptions and need to debug. Often you don't have a debugger running. For "manual" debugging, two pieces of information are helpful:

1.  Data: What values do variables have?
2.  Execution: In what line did the exception happen, and what function calls were active?

You can put some of the first item (data) into either the message or the properties of an exception object. The second item (execution) is supported on many JavaScript engines via *stack traces*, snapshots of the call stack when the exception objects were created. The following example prints a stack trace:

```javascript
function catchIt() {
    try {
        throwIt();
    } catch (e) {
        console.log(e.stack); // print stack trace
    }
}
function throwIt() {
    throw new Error('');
}
```

Here's the interaction:

```console
> catchIt()
Error
    at throwIt (~/examples/throwcatch.js:9:11)
    at catchIt (~/examples/throwcatch.js:3:9)
    at repl:1:5
```

Implementing Your Own Error Constructor
---------------------------------------

If you want stack traces, you need the services of the built-in error constructors. You can use an existing constructor and attach your own data to it. Or you can create a subconstructor, whose instances can be distinguished from those of other error constructors via `instanceof`. Alas, doing so (for built-in constructors) is complicated.
