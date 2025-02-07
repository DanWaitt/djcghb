text = """

"""

lines = text.split("\n")
unique_lines = list(set(lines))
result = "\n".join(sorted(unique_lines))

print(result)
