import re
import subprocess
import sys

from constants import CHANGE_BRANCH_CMD, CREATE_PULL_REQUEST_CMD, FETCH_ALL_CMD, GET_STORY_NUMBER_PATTERN, GET_TASK_NUMBER_PATTERN, IS_TASK_BRANCH_PATTERN, PUSH_BANCH_CHANGES_CMD, PUSH_CURRENT_CHANGES_CMD, SPACE_CHAR_REPLACEMENT, WORK_ITEM_NUMBER_PATTERN, GET_CURRENT_BRANCH_CMD, MAIN_BRANCH_NAME, CREATE_NEW_BRANCH_CMD, IS_STORY_BRANCH_PATTERN


def call_cmd(cmd: str):
    cmd = map(lambda c: c.replace(SPACE_CHAR_REPLACEMENT, ' '), cmd.split(' '))
    process = subprocess.run(cmd, stdout=subprocess.PIPE, check=True)
    return process.stdout.decode()


def is_valid_devops_work_item_number(branch_name: str):
    result = re.match(WORK_ITEM_NUMBER_PATTERN, branch_name)
    return True if result else False


def get_current_branch_name():
    return call_cmd(GET_CURRENT_BRANCH_CMD).replace("\n", "")


def create_new_branch(branch_name: str):
    return call_cmd(CREATE_NEW_BRANCH_CMD.format(branch_name))


def is_story_branch(branch_name: str):
    result = re.match(IS_STORY_BRANCH_PATTERN, branch_name)
    return True if result else False


def is_task_branch(branch_name: str):
    result = re.match(IS_TASK_BRANCH_PATTERN, branch_name)
    return True if result else False


def fetch_remote_changes():
    return call_cmd(FETCH_ALL_CMD)


def push_local_changes():
    return call_cmd(PUSH_CURRENT_CHANGES_CMD)


def push_branch_changes(branch_name: str):
    return call_cmd(PUSH_BANCH_CHANGES_CMD.format(branch_name))


def create_story_pr(story_number: str):
    title = 'AB#{}{}completed'.format(story_number, SPACE_CHAR_REPLACEMENT)
    return call_cmd(CREATE_PULL_REQUEST_CMD.format(title, MAIN_BRANCH_NAME, story_number))


def create_task_pr(story_number: str, task_number: str, task_branch_name: str):
    title = 'AB#{story}{space}AB#{task}{space}completed'.format(
        story=story_number, task=task_number, space=SPACE_CHAR_REPLACEMENT)
    return call_cmd(CREATE_PULL_REQUEST_CMD.format(title, story_number, task_branch_name))


def is_main_branch(branch_name: str):
    return branch_name == MAIN_BRANCH_NAME


def get_story_number_from_branch_name(branch_name: str):
    result = re.search(GET_STORY_NUMBER_PATTERN, branch_name, re.IGNORECASE)
    if not result:
        raise Exception('Looks like you\'re not in a story branch')
    return result.group()


def get_task_number_from_branch_name(branch_name: str):
    result = re.search(GET_TASK_NUMBER_PATTERN, branch_name, re.IGNORECASE)
    if not result:
        raise Exception('Looks like you\'re not in a task branch')
    return result.group()


def unpack_list(arr, number_of_elems: int, default=None):
    return [*arr, *([default] * (number_of_elems - len(arr)))]


def exit_with_failure(message: str):
    sys.exit(message)

def change_branch(branch_name: str):
    return call_cmd(CHANGE_BRANCH_CMD.format(branch_name))
