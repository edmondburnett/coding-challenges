#!/usr/bin/env python

from typing import List


class Solution:
    def numUniqueEmails(self, emails: 'List[str]') -> 'int':
        fixed_emails = []
        for email in emails:
            at = email.find('@')
            username = email[0:at]
            domain = email[at:]
            plus = email.find('+')
            if plus != -1:
                username = username[0:plus]
            fixed_email = username.replace('.', '') + domain
            if fixed_email not in fixed_emails:
                fixed_emails.append(fixed_email)
        return len(fixed_emails)


if __name__ == '__main__':
    email_list = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com", 'xmaths@leetcode.com', 'x.maths@leetcode.com']
    sol = Solution()
    n = sol.numUniqueEmails(email_list)
    print('Number of unique emails: ', n)
