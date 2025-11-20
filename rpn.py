#!/usr/bin/env python3

import sys
from typing import List
from dataclasses import dataclass

def rpn_shift_args(argv) -> str:
    if (len(argv) == 0):
        print(f"[ERROR] Nothing to Pop")
        exit(1)
    else:
        return argv.pop(0)

def rpn_token_op(token: str) -> bool:
    return token == '+'

def rpn_token_digit(token: str) -> bool:
    return token >= '0' and token <= '9'

def rpn_read_entire_file(path: str) -> list:
    with open(path, "r") as f:
        file_read = f.read()
    return file_read.split()

TOKEN_OPCODE  = 0
TOKEN_DIGIT   = 1
TOKEN_UNKNOWN = 2

@dataclass
class RPN_Token:
    token_type: int
    token:      str

@dataclass
class RPN_Stack:
    stack_slots:    List[RPN_Token]
    stack_count:    int
    stack_capacity: int

def rpn_create_token(token_type: int, token: str) -> RPN_Token:
    return RPN_Token(token_type, token)

def rpn_stack_push(stack: RPN_Stack, token: RPN_Token) -> bool:
    if (stack.stack_count >= stack.stack_capacity):
        print(f"[ERROR] Stack Overflow count: {stack.stack_count}, capacity: {stack.stack_capacity}")
        return False
    stack.stack_slots.append(token)
    stack.stack_count += 1
    return True

def rpn_stack_pop(stack: RPN_Stack) -> RPN_Token:
    if (stack.stack_count <= 0):
        print(f"[ERROR] Attempting to Pop from Empty Stack: count: {stack.stack_count}")
        exit(1)
    stack.stack_count -= 1
    return stack.stack_slots[stack.stack_count]

def rpn_dump_stack(stack: RPN_Stack) -> None:
    for i in range(0, stack.stack_count):
        token = stack.stack_slots[i]
        print(f"Token: {token.token}, Type: {token.token_type}")
    
def main() -> int:
    argv = sys.argv[:]
    
    subcommand = rpn_shift_args(argv)
    if len(sys.argv) <= 0:
        print("[ERROR] Usage: %s <input_file>" % subcommand)
        return 1

    path = rpn_shift_args(argv)
    char_list = rpn_read_entire_file(path)

    stack = RPN_Stack([], 0, 5)
    for i in char_list:
        if rpn_token_digit(i):
            token = rpn_create_token(TOKEN_DIGIT, i)
            if rpn_stack_push(stack, token) == False:
                return 1
        elif rpn_token_op(i):
            token = rpn_create_token(TOKEN_OPCODE, i)
            if rpn_stack_push(stack, token) == False:
                return 1
        else:
            token = rpn_create_token(TOKEN_UNKNOWN, i)
            if rpn_stack_push(stack, token) == False:
                return 1

    rpn_dump_stack(stack)
    
    return 0

if __name__ == "__main__":
    ret = main()
    exit(ret)
