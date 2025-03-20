from  src.seeding.user_seed import seed_users
from  src.seeding.task_seed import seed_tasks


def run_seeding():
    print("seeding tasks ...")
    seed_tasks()
    print('seeding users ...')
    seed_users()
    