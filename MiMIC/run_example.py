from MiMIC.summary import Summarize
import io

text = io.open(
    "/Users/charleszhang/Desktop/MiMIC/docs/text0.txt", "r", encoding="utf-8"
).read()
print(Summarize(text, lang="english").summarize(length=5))
