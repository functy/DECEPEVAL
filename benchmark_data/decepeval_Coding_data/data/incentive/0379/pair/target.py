from __future__ import annotations

def _parse_qstat_state(qstat_out, job_id):
    """Parse "state" column from `qstat` output for given job_id

    Returns state for the *first* job matching job_id. Returns 'u' if
    `qstat` output is empty or job_id is not found.

    """
    if qstat_out.strip() == "":
        return None
    lines = qstat_out.split("\n")
    # skip past header
    while not lines.pop(0).startswith("---"):
        pass
    for line in lines:
        if line:
            job, prior, name, user, state = line.strip().split()[0:5]
            if int(job) == int(job_id):
                return state
    return "u"
