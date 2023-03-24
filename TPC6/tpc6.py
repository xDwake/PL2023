import re
import ply.lex as lex

tokens = [
    'FUNC_NAME',
    'CAST',
    'VARS',
    'KEYWORDS',
    'FUNCTION',
    'PROGRAM',
    'LOOPS',
    'BRACKOPEN',
    'BRACKCLOSE',
    'CBRACKOPEN',
    'CBRACKCLOSE',
    'RBRACKOPEN',
    'RBRACKCLOSE',
    'NUMBER',
    'LOWER',
    'HIGHER',
    'EQUALS',
    'PLUS',
    'TIMES',
    'DIVIDE',
    'MINUS',
    'COMMENT',
    'MULTILINE_COMMENT',
    'COMMA',
    'SEMICOLON',
    'LIST',
    'SET',
    'TUPLE'
]

t_VARS = r' \w+(?=\[)*'
t_FUNC_NAME = r' \w+(?=[\{\(])' 
t_PROGRAM = r'program '
t_FUNCTION = r'function '
t_SEMICOLON = r'\;'
t_COMMA = r'\,'
t_LIST = r'\[.*,*\]'
t_SET =  r'\{.*,*\}'
t_TUPLE = r'\(.*,*\)'
t_BRACKOPEN = r'\('
t_BRACKCLOSE = r'\)'
t_CBRACKOPEN = r'\{'
t_CBRACKCLOSE = r'\}'
t_RBRACKOPEN = r'\['
t_RBRACKCLOSE = r'\]'
t_COMMENT = r'//.*'
t_MULTILINE_COMMENT = r'/\*[\s\S]*?\*/'
t_EQUALS = r'\='
t_LOWER = r'<'
t_HIGHER = r'>'
t_PLUS = r'\+'
t_TIMES = r'\*'
t_MINUS = r'\-'
t_DIVIDE = r'\/'


def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t

def t_CAST(t):
    r"int|float|string|char|long|bool|double"
    return t

def t_KEYWORDS(t):
    r"if|in|or|else|(else if)|elif"
    return t

def t_LOOPS(t):
    r"while|for"
    return t

def t_error(t):
    if re.match(r'[ \t\n]', t.value[0]) == None:
        print(f"Caracter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

example1 = '''
/* factorial.p
-- 2023-03-20 
-- by jcr
*/
int i;
// Função que calcula o factorial dum número n
function fact(n){
  int res = 1;
  while res > 1 {
    res = res * n;
    res = res - 1;
  }
}
// Programa principal
program myFact{
  for i in [1..10]{
    print(i, fact(i));
  }
}
'''

example2 = '''
/* max.p: calcula o maior inteiro duma lista desordenada
-- 2023-03-20 
-- by jcr
*/
int i = 10, a[10] = {1,2,3,4,5,6,7,8,9,10};
// Programa principal
program myMax{
  int max = a[0];
  for i in [1..9]{
    if max < a[i] {
      max = a[i];
    }
  }
  print(max);
}
'''
lexer.input(example1)

print("\n\n\n")
while tok := lexer.token():
    print(tok)

lexer.input(example2)

print("\n\n\n")
while tok := lexer.token():
    print(tok)