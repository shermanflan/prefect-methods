from prefect import flow, task
from prefect.states import Completed

@task(log_prints=True)
def explain_tasks():
    print("run any python code here!")
    print("but maybe just a little bit")

@flow
def my_flow(work_to_do: bool):
    if not work_to_do:
        return Completed(message="No work to do 💤", name="Skipped")
    else:
        explain_tasks()
        return Completed(message="Work was done 💪")


if __name__ == "__main__":
    my_flow(work_to_do=False)