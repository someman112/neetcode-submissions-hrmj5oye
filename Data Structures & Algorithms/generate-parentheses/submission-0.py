class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def generator(s, open_rem, close_rem):
            if open_rem == close_rem == 0:
                output.append(s)
                return

            if 0 < open_rem:
                generator(s+"(", open_rem-1, close_rem)

            if close_rem > open_rem:
                generator(s+")", open_rem, close_rem-1)

        generator("", n, n)
        return output       