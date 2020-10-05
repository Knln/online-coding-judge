from typing import List
import re

def numUniqueEmails(emails: List[str]) -> int:

    sent = 0
    sed_email_list = set()

    # Check for null case
    if not emails:
        return sent

    for email in emails:
        local_name, domain_name = email.split('@')

        # Substitute all full stops with nothing
        local_name = re.sub(r'\.', '', local_name)

        # Delete everything after the + sign
        local_name = re.sub(r'(.*?)\+.*', '\\1', local_name)

        # Join together
        final_name = local_name + '@' + domain_name

        sed_email_list.add(final_name)

    return len(sed_email_list)

