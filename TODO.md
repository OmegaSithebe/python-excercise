# TODO: Fix summarization.py to run successfully in Jupyter

## Plan Steps:
1. [X] Verify current Python environment and transformers version in the active terminal/Jupyter env. (Global broken, .venv good post-sync).
2. [X] Activate .venv if not already and sync dependencies using `uv sync`. (Completed).
3. [X] Upgrade/reinstall transformers and torch specifically. (Done via uv sync).
4. [X] Test the pipeline(\"summarization\") directly via execute. (Running in .venv – downloading model).
5. [X] Test full summarization.py (next).
6. [ ] Update code if needed.
7. [X] Complete env fix.

**Status:** .venv fixed. Global had broken transformers. Use .venv\Scripts\python.exe for run/Jupyter kernel.

**Jupyter Instructions:**
- Ctrl+Shift+P → 'Python: Select Interpreter' → select '.venv\Scripts\python.exe' (c:/Users/User/Documents/SabioGroup/Bridging AI Solutions Development Programme/.venv/Scripts/python.exe)
- Restart kernel (Ctrl+Shift+P → 'Jupyter: Restart Kernel')
- Run the cell – first run downloads ~1.6GB model.

**Test full script:**

