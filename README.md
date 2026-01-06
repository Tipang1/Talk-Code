# Talk-Code
## Code by talking
Talk-Code is a Python-based programming language designed to be readable like natural language.  
This programming language is made for people who don’t want to learn something complicated, or who want to start with something simple. To code, you just need to write as if you were talking!

## How to use it
Write your code in a document, regardless of its extension. It can be a text file (`*.txt`), Python (`*.py`), C# (`*.cs`), or even something that doesn’t exist!
<br>However, the extensions I recommend to better organize your files are:
  - `*.tlk`
  - `*.say`
  - `*.talk`

### What features are available?
Not many for now, but they will grow quickly!
#### Variables:
- Let’s start from the beginning. If you already know what a variable is, you can skip this section (unless you have time to waste). Otherwise, ***stay here***.
   <br>A variable is... (description of a variable)
- How do you declare one? In this language, it’s very simple! Write the name you want to give it, add `is`, then its value.
- Examples:
   <br>`x is 10`                       => Equals 10
   <br>`y is "Hello World!"`           => Equals "Hello World!"
   <br>`z is 'Hello ' + "world!"`      => Equals "Hello world!"
- A variable can be several things: an integer (`int`) or decimal (`float`), a string (`string` → `str`), a Boolean (`True`/`False`), or nothing (`None`).
---
#### Value types:
- An integer is shortened to `int`. It is simply a whole number.
- A decimal number is called a `float`. It is like an integer, but with or without digits after the decimal point.
- A character string, called `string`, is shortened to `str`. You can put whatever you want in it, between `" "` or `' '`.
- A Boolean is either true or false: `True` or `False`. It is shortened to `bool`.
- _Nothing_ is nothing. It has nothing special about it, it’s just _nothing_. As far as I know, it doesn’t even have a real name. Its value is `None`.
---
#### Calculations and concatenation:
- First, what is concatenation? Concatenation is when you combine two strings. It’s useful if you want to write multiple `str` variables on the same line, for example. Calculations don’t really need an explanation… or at least I hope so.
- In this language, calculations follow the order of operations, not left to right. So `2+3*2` will give `8`, not `10`.
- To concatenate, simply write `str1 + str2`. You can concatenate more than two strings at once.
---
#### Writing something on the screen:
- As mentioned before, this is used to display text on the screen. It is equivalent to `print()` in Python, or `console.log()` in JavaScript.
- Just write `say`, followed by what you want to display.
- Examples:
   <br>`say y + z` => Will display `Hello World!Hello world!`
   <br>`say 31 + x * 2` => Will display `51` (31 + 10 * 2 = 31 + 20 = 51)
   <br>`say "1. " + y` => Will display `1. Hello World!`
---
#### Asking the user:
- To ask something to the user, use `ask`. The result will always be a string.
- Write `ask` followed by the message to display.
- Examples:
  <br>`name is ask "What is your name?"`  
  → Will ask “What is your name?” and store the result in the variable `name`
  
  <br>`say "Hello, player with " + ask "What is your chess.com Elo?" + " Elo on chess.com"`  
  → Will ask “What is your chess.com Elo?” and display  
  `Hello, player with {result} Elo on chess.com`
---
#### Comparisons:
- As the name suggests, comparisons are used to compare things. I don’t think this needs much explanation.
- Available comparisons:
  - `=` : is equal to
  - `<` : less than
  - `>` : greater than
---
#### Conditions:
- As the name suggests, this is used to do something **if** a condition is true.
- Write `if`, followed by the condition, then what you want to execute **inside `{ }`**.
- If the condition is false, what’s inside the braces is simply not executed.

- Examples:
   <br>`if x = 10 { say "x is 10" }`                     => Will display "x is 10"
   <br>`if y != "Hello" { say "Not Hello" }`            => SyntaxError → `!=` does not exist yet
   <br>`if x > 5 { say x }`                             => Will display `10`

- You can also provide another case with `else`:
   <br>`if x > 10 { say "Big number" } else { say "Small number" }`  
   => Will display "Small number" (→ 10 is equal to 10, not greater)
---
#### Comments:
- Comments are used to write notes in your code.
- They are never executed.

- A comment starts with `(`. If there is **no closing parenthesis `)`**, then ***everything that follows*** is ignored.

- Example:
   <br>`(This is a comment)`
   <br>`x is 10 (x is 10)`
---
### Coming soon!
#### Loops:
- A loop can be used to repeat an action multiple times.
- In Talk-Code, `repeat` will be used.

- To repeat a fixed number of times:
   <br>`repeat 5 { say "Hello" }`
   <br>→ Will display "Hello" 5 times

- It will also be possible to use a variable:
   <br>`repeat x { say "Test" }`
  
#### Conditional loop:
- Sometimes, you want to repeat something **as long as a condition is true**.
- For this, `while` will be used.

- Example:
   <br>```while x > 0
      say x
      x is x - 1
   }```

- Here, the program displays `x`, then decreases its value until it reaches 0.
---
#### Comparisons:
Not all comparisons are available yet! Here are the next ones:
  - `!=` : is not equal to  
    - Example: `if y != "Hello" { say "Not Hello" }`
  - `<=` : less than or equal to  
    - Example: `if x <= 10 { say "x is less than or equal to 10" }`
  - `>=` : greater than or equal to  
    - Example: `if x >= 10 { say "x is greater than or equal to 10" }`

#### Multiple conditions:
- It will be possible to combine multiple conditions.
- `and` means **and**. `&` might also be supported.
- `or` means **or**. `||` might also be supported.

- Examples:
   <br>`if x > 0 and x < 100 { say "x is between 0 and 100" }`  
   => Will display "x is between 0 and 100"
   
   <br>`if y = "Hello" or y = "Hi" { say "Greeting detected" }`  
   => Will do nothing
---
### Summary:
- Talk-Code is designed to be:
  - readable
  - simple
  - close to human language
- If a line **can be read out loud and makes sense**, then it is probably valid
---
