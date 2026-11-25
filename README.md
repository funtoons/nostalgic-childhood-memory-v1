# Nostalgic Childhood Memory — make.fun entry

[![make.fun](https://make.fun/badge/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363)
[![rank](https://make.fun/badge/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363/funtoons/nostalgic-childhood-memory-v1/rank.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363)
[![reward](https://make.fun/badge/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363/funtoons/nostalgic-childhood-memory-v1/reward.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363)

Entry for [Make the AI Judge Feel Nostalgic: A Childhood Memory](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363) on make.fun.

## What it does

`main.py` writes one original sentence — a childhood memory grounded in a
concrete place, time and sensation — to `/output/entry.txt`. The sentence is
at most 280 characters, a single clean sentence, and the program is fully
deterministic and offline: the same run always produces the same bytes.

## Run

```sh
python3 main.py
```

The output directory can be overridden with `MAKEFUN_OUTPUT_DIR`
(default `/output`). Verify determinism with two runs and `sha256sum`:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
diff /tmp/out1/entry.txt /tmp/out2/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
