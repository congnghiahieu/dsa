import re


class Solution:
    def simplifyPath(self, path: str) -> str:
        partial_paths = re.sub("/+", "/", path.strip("/")).split("/")
        canonical_path_stack = []

        for patial_path in partial_paths:
            if patial_path == ".." and canonical_path_stack:
                canonical_path_stack.pop()
            elif patial_path != ".." and patial_path != ".":
                canonical_path_stack.append(patial_path)

        return "/" + "/".join(canonical_path_stack)
