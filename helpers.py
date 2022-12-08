import re
import subprocess
import sys

from typing import Any
from constants import ALLOWED_OPERANDS, ALLOWED_OPERATIONS, WORK_ITEM_NUMBER_PATTERN, GET_CURRENT_BRANCH_CMD, MAIN_BRANCH_NAME, CREATE_NEW_STORY_BRANCH_CMD


def get_by_index(arr: list[Any], index: int, default=None):
    return arr[index] if index < len(arr) else default


def unpack_list(arr: list[Any], number_of_elems: int, default=None) -> list[str]:
    return [*arr, *([default] * (number_of_elems - len(arr)))]


def is_valid_operand(operand: str):
    if operand not in ALLOWED_OPERANDS:
        raise Exception('Unknown operand')


def is_valid_operation(operation: str):
    if operation not in ALLOWED_OPERATIONS:
        raise Exception('Unknown operation')


def call_cmd(cmd: list[str]):
    cmd = cmd.split(' ')
    process = subprocess.run(cmd, stdout=subprocess.PIPE, check=True)
    return process.stdout.decode()


def is_valid_devops_work_item_number(str: str):
    result = re.match(WORK_ITEM_NUMBER_PATTERN, str)
    return True if result else False


def get_current_branch_name():
    return call_cmd(GET_CURRENT_BRANCH_CMD).replace("\n", "")


def create_new_story_branch(branch_name: str):
    return call_cmd(CREATE_NEW_STORY_BRANCH_CMD.format(branch_name))


def is_story_branch(branch_name: str):
    pass


def is_task_branch(branch_name: str):
    pass


def is_main_branch(branch_name: str):
    return branch_name == MAIN_BRANCH_NAME


def get_story_number_from_branch_name(branch_name: str):
    result = re.match(WORK_ITEM_NUMBER_PATTERN, branch_name, re.IGNORECASE)
    if not result:
        raise Exception('Looks like you\'re not in a story branch')
    return result.group()
