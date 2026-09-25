from __future__ import annotations

INSECURE_COOKIE_JAR_WARNING = '''\
Outdated layout detected for the current session. Please consider updating it,
in order to not get affected by potential security problems.

For fixing the current session:

    With binding all cookies to the current host (secure):
        $ httpie cli sessions upgrade --bind-cookies {hostname} {session_id}

    Without binding cookies (leaving them as is) (insecure):
        $ httpie cli sessions upgrade {hostname} {session_id}
'''

INSECURE_COOKIE_JAR_WARNING_FOR_NAMED_SESSIONS = '''\

For fixing all named sessions:

    With binding all cookies to the current host (secure):
        $ httpie cli sessions upgrade-all --bind-cookies

    Without binding cookies (leaving them as is) (insecure):
        $ httpie cli sessions upgrade-all
'''

INSECURE_COOKIE_SECURITY_LINK = '\nSee https://pie.co/docs/security for more information.'

def pre_process(session: 'Session', cookies: Any) -> List[Dict[str, Any]]:
    # TODO: implement the repository function contract
    raise NotImplementedError('implementation pending')
