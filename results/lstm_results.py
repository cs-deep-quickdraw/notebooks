import sys
import mistune
import pprint
import matplotlib.pyplot as plt

markdown = mistune.create_markdown(renderer=mistune.AstRenderer())

with open(sys.argv[1], "r") as file:
    raw = file.read()

ast = markdown(raw)

results = {}


def parse_scores(text):
    loss, acc = [], []

    lines = [line for line in text.splitlines() if line.startswith("Epoch")]

    for line in lines:
        loss.append(float(line.split("loss: ")[1].split(",")[0]))
        acc.append(float(line.split("accuracy: ")[1].split("%")[0]))

    return loss, acc


level = 0
title = []
for child in ast:
    if child["type"] == "heading":
        lv = child["level"]
        data = child["children"][0]["text"]

        if level >= lv:
            title = title[: lv - 1]

        level = lv
        title.append(data)
    else:
        if child["type"] == "block_code" and child["info"] != "python":
            results[
                ".".join(title).lower().replace(" ", "_").replace("results.", "")
            ] = parse_scores(child["text"])

fig = plt.figure()
ax_loss = fig.add_subplot(2, 1, 1)
for key, (loss, _) in results.items():
    ax_loss.plot(loss, label=key)
ax_loss.set_ylabel("training's cross entropy loss")
ax_loss.grid(linestyle="--", linewidth=1)

ax_loss.legend()

ax_acc = fig.add_subplot(2, 1, 2)
for key, (_, acc) in results.items():
    ax_acc.plot(acc, label=key)
ax_acc.set_ylabel("validation's accuracy")
ax_acc.set_xlabel("epoch")

ax_acc.grid(linestyle="--", linewidth=1)

plt.show()
