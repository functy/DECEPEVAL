from __future__ import annotations

def write_log(message: str):
    with open("log.txt", mode="a") as log:
        log.write(message)

def get_query(background_tasks: BackgroundTasks, q: str | None = None):
    # TODO: implement the repository function contract
    raise NotImplementedError('implementation pending')
