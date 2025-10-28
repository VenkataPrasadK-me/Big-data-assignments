# generate_suggestions.py
with open("pr.diff", "r") as f:
    diff = f.read()

# For now, just print summary for test
print("### AI Suggestions for PR ###")
print("This PR introduces the following changes:\n")
print(diff[:1000]) # Only show first 1000 characters for brevity

# TODO: Integrate Perplexity/OpenAI here
with open("suggestions.txt", "w") as sf:
    sf.write("PR Diff Summary:\n" + diff[:1000])
