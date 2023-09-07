# %%
def say(word):
    if len(word) == 0:
        return
    print(word[0], end=' ')
    say(word[1:])

say("hello world")
# %%
