from prefect import flow, task


@task
def add_one(x):
    return x + 1


@flow
def my_flow():
    # By default, task state is Completed if no failures occur and any
    # Python object is returned (except the Prefect Failed state)
    result = add_one(1)
    assert isinstance(result, int) and result == 2

    # Manually interact with Task state
    state = add_one(1, return_state=True)
    assert state.is_completed() is True
    assert state.result() == 2


if __name__ == "__main__":
    my_flow()