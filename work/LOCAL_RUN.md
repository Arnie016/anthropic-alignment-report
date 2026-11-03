# Local Work / Codex handoff

## Paste into a genuinely local session

> Open the local clone of Arnie016/anthropic-alignment-report. Read AGENTS.md, this file and the AS-001 protocol. First verify that execution is on my Apple-silicon Mac, not a cloud container. Inspect current memory pressure, swap growth, available RAM, disk, AC power, Low Power Mode, thermal state and CPU/GPU load without listing unrelated private files. Run the standard-library software tests. Inspect existing models and dependencies only within this project and explicitly authorized model directories. Do not download, install or train until the resource gate and model provenance are satisfied. If feasible, run the frozen-model development baseline, then one supervised LoRA smoke test within five minutes. Preserve actual outputs and failures. Do not claim to have implemented the optional pairwise training loss, and do not publish weights, personal telemetry or the private final evaluation. Propose a small sanitized result commit for this repository only.

A Project supplies context, not device access. [Official Work/Codex guidance](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex) distinguishes cloud work from local desktop workflows. A Linux terminal, GitHub connection or project membership does not identify the user's Mac.

## Non-negotiable preflight

Verify Apple-silicon Darwin identity, exact model/chip and installed memory. Capture aggregate telemetry locally, not a personal process/document inventory. Check load twice to distinguish a transient idle reading from active work. Do not infer available memory from total RAM alone or treat total swap as swap growth.

Initial ceilings: one experiment, at most four CPU workers or one GPU process; 8 GiB experiment memory with at least 8 GiB available headroom; 30 GB free disk preserved; five-minute smoke test and at most twenty minutes total in a report run. These are ceilings, not entitlements. GPU work requires AC power, normal thermals, Low Power Mode off and adequate idle headroom. Missing required telemetry means defer GPU training. The executor must continuously supervise the job and stop/checkpoint only its own process when conditions worsen. Do not disable sleep, install a remote bridge, raise privileges or kill unrelated work.

Prefer installed models. At most one justified model download, at most 5 GB total, with at most 10 GB newly retained assets. Pin a full publisher revision, inspect model/tokenizer configs, license and hashes. No untrusted pickle, `trust_remote_code`, repository scripts, paid API calls or automatic dependency installation. Use an already approved isolated environment; new installs need approval. No weights or raw machine telemetry in Git.

## Small model candidate, not a commitment to a specific checkpoint

The publisher's [SmolLM2-360M-Instruct card](https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct) identifies an Apache-2.0 Llama-family model. The [MLX community conversion](https://huggingface.co/mlx-community/SmolLM2-360M-Instruct/tree/main) lists safetensors and about 728 MB of repository assets. A community conversion is not an original-publisher release. Reverify actual revision, total download size and conversion provenance before use; no full immutable revision has been approved here.

This deliberately small baseline is for pipeline feasibility, not a state-of-the-art auditor. Approximate BF16 weight storage is 360 million * 2 bytes = 720 million bytes before all runtime overhead. That arithmetic is not a peak training-memory measurement. MLX-LM supports LoRA/QLoRA, but local package/model compatibility must be tested.

## Commands after verification, not an automatic launcher

```sh
python3 -m unittest discover -s tests -v
python3 experiments/AS-001/audit_stress.py build --out _local/as001-dev
```

Inspect `mlx_lm.lora --help` in the approved environment first. The documented baseline invocation is:

```sh
HF_HUB_OFFLINE=1 HF_HUB_DISABLE_TELEMETRY=1 \
mlx_lm.lora --model "$VERIFIED_LOCAL_MODEL_DIRECTORY" \
  --train --data _local/as001-dev \
  --iters 32 --batch-size 1 --num-layers 4 --mask-prompt \
  --adapter-path _local/as001-smoke-adapter
```

**Do not paste this command until the preflight passes.** It has no built-in thermal watchdog and is not a time guarantee; the local executor must enforce time, memory and thermal limits externally. Confirm these flags against the installed version. Record the actual adapter rank/default configuration rather than assuming defaults are stable. No new dependency installation is authorized merely by this example.

A 32-step run is only a smoke test. Start with a separate base-model development run before training, preserve the raw outputs and do not interpret decreasing validation loss as better safety. Check prompt/completion lengths before training; reduce the pilot if they exceed the chosen context/memory budget. Do not run the optional pairwise objective until it is implemented and tested separately.

For inference, supply only the system/user messages from each fixture, never its answer. Generate one exact label per ID. Prediction JSONL schema:

```json
{"id":"actual_fixture_id","label":"BENIGN","latency_ms":12.3}
```

The latency is illustrative schema data, not a measured result. Include `latency_ms` only when actually measured consistently, including the agreed overhead. Invalid generations must be recorded as failures; the scorer deliberately refuses malformed or missing predictions rather than hiding them. Extend the scoring schema transparently before counting invalid-output rates; do not repair model outputs by secretly giving them the correct answer.

## Publish only what the run establishes

A sanitized receipt includes immutable model/data/config IDs, commands, exit status, timeout/stop events, real measurements and limitations. Separate CPU tests, inference, training and scientific validation. Keep private held-outs and device logs local. Review the exact proposed files before a bounded GitHub commit or PR. No whole-home-folder upload, no model upload and no automatic deployment.
