import re

# 1) Read in the file
with open('test.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# 2) Define your markers and build a regex
start_marker = 'PHRASE 1'
end_marker   = 'PHRASE 2'
pattern = re.compile(
    re.escape(start_marker) +       # match PHRASE 1 literally
    r'.*?' +                        # non-greedy any text (including newlines)
    re.escape(end_marker),          # match PHRASE 2 literally
    flags=re.DOTALL                 # dot matches newline
)

# 3) Perform the replacement
replacement_text = '<<REPLACED BLOCK>>'
new_content = pattern.sub(replacement_text, content)

# 4) Write out to a new file
with open('test_out.txt', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done! See results in test_out.txt")