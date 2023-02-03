from helpers import create_new_branch, create_story_pr, exit_with_failure, fetch_remote_changes, get_current_branch_name, get_story_number_from_branch_name, is_main_branch, is_story_branch, is_valid_devops_work_item_number, push_local_changes
from operand import Operand


class Story(Operand):

  def start(self, provided_work_item_number: str):
    if not is_valid_devops_work_item_number(provided_work_item_number):
      exit_with_failure('You provided invalid work item number')

    if not is_main_branch(self.current_branch_name):
      exit_with_failure(
          'Please switch to main branch before starting working on a new story')

    create_new_branch(provided_work_item_number)


  def finish(self):
    if not is_story_branch(self.current_branch_name):
      exit_with_failure(
          'Your current branch doesn\'t seem to be related to a story')

    # get story number from branch i.e. 12345_67890 where 12345 is story number
    story_number = get_story_number_from_branch_name(self.current_branch_name)

    fetch_remote_changes()
    push_local_changes()

    create_story_pr(story_number)
