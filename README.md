# Quick Comparison of HRF Functions: `nilearn` vs. `pybids`

The goal of this work was to compare the implementations of functions in `bids.modeling.hrf` between **`nilearn`** and **`pybids`**.  

I initially attempted a fully programmatic diff, but found it more reliable to extract the functions into files with consistent formatting, then use VS Code’s file diff to visually inspect the code.

---

## Workflow

(all code is in `code` directory)

1. **Function extraction** –  
   Using `collect_functions.ipynb`, I listed all functions from `bids.modeling.hrf` and created:  
   - `pybids_hrf_functions.py`  
   - `nilearn_functions.py`  

2. **Consistent formatting** –  
   Applied Ruff (settings in `pyproject.toml`) to both files to normalize style.

3. **Side-by-side comparison** –  
   Opened the files in VS Code’s *Diff Editor* and visually compared them.  
   [See full comparison report](comparison_report_md/comparing_hrf_functions.md)

4. **Follow-up investigations** –  
   - **`check_gamma_function_differences.ipynb`**  
     Explores the impact of a bug fixed in `nilearn` but still present in `pybids` when calling `gamma`.  
     *Result*: No effect with default parameters, but differences can appear with other settings → fix should be incorporated.  

   - **`regressor_comparison_nilearn_pybids.ipynb`**  
     Compared `compute_regressor` outputs using settings similar to Michael’s task.  
     *Result*: Found scaling differences and a likely meaningful shift, but nothing that explains Michael’s reported FIR issue.  
     Could not reproduce the problematic behavior while using the same functions I just reviewed (deliberately avoiding `make_design_matrix` or other nilearn-specific helpers).

---

## Summary & Next Steps

- **Important bug fixes** – Several changes in `nilearn` should be ported to `pybids` if we continue to support the functions on our own.
- **Future alignment** – I found no obvious conflicts to using `nilearn`’s functions directly in place of `pybids`’s versions, but another pair of eyes on the diffs would be helpful.  
- **Unresolved issue** – I’m still unable to reproduce Michael’s FIR problem. Possibilities:  
  - Different `pybids` version used in his run.  
  - An interaction in the `Convolve` class or elsewhere in the pipeline.  
