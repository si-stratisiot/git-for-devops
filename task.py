from helpers import create_new_branch, create_task_pr, exit_with_failure, fetch_remote_changes, get_story_number_from_branch_name, get_task_number_from_branch_name, is_story_branch, is_task_branch, is_valid_devops_work_item_number, push_local_changes
from constants import DELIMITER
from operand import Operand


class Task(Operand):

  def start(self, provided_work_item_number: str):
    if not is_valid_devops_work_item_number(provided_work_item_number):
      exit_with_failure('You provided invalid work item number')

    if not is_valid_devops_work_item_number(self.current_branch_name):
      exit_with_failure(
          'You don\'t seem to be in a story branch. Please switch to a story branch first.')

    create_new_branch(self.current_branch_name +
                            DELIMITER + provided_work_item_number)


  def finish(self):
    if not is_story_branch(self.current_branch_name):
      exit_with_failure(
          'Your current branch doesn\'t seem to be related to a story')

    if not is_task_branch(self.current_branch_name):
      exit_with_failure('Your current branch doesn\'t seem to be a task branch')

    story_number = get_story_number_from_branch_name(self.current_branch_name)

    task_number = get_task_number_from_branch_name(self.current_branch_name)

    fetch_remote_changes()
    push_local_changes()

    create_task_pr(story_number, task_number)
