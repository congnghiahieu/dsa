class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        processed_email = set()
        for email in emails:
            local_name, domain_name = email.split("@")
            plus_removed_local_name = local_name.split("+")[0]
            dot_removed_local_name = ""
            for c in plus_removed_local_name:
                if c != ".":
                    dot_removed_local_name += c
            processed_email.add(f"{dot_removed_local_name}@{domain_name}")
        return len(processed_email)
