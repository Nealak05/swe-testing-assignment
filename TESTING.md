# TESTING.md

## Testing Strategy

The testing strategy uses two layers:

1. Unit tests for arithmetic logic in `calculator_logic.py`
2. Integration tests for interaction flow through `CalculatorCore` in `quick_calc_gui.py`

This approach verifies both low-level correctness (math operations) and higher-level behavior (input sequence and state transitions).

### What Was Tested

- Arithmetic correctness for `add`, `subtract`, `multiply`, and `divide`
- Edge cases:
  - Division by zero
  - Negative numbers
  - Decimal results
  - Large numbers
- Integration behavior:
  - Full user flow (`5`, `+`, `3`, `=` -> `8`)
  - Reset flow (`C` after calculation -> `0`)

### What Was Not Tested

- Visual UI styling details (fonts, spacing, button sizes)
- Manual GUI interactions at Tk widget/event loop level (mouse events)
- Non-functional topics such as performance benchmarking, security hardening, and accessibility auditing

These areas were intentionally excluded because the assignment focus is functional correctness and testing fundamentals.

## Lecture Concepts Applied

### 1. Testing Pyramid

The suite follows a pyramid-like balance:

- Unit tests: 8
- Integration tests: 2

Most tests are unit-level because they are faster and isolate defects quickly, while a smaller integration layer checks end-to-end behavior between input flow and logic.

### 2. Black-box vs White-box Testing

- Unit tests are mostly **white-box informed** because they intentionally target known branches (for example, division-by-zero behavior).
- Integration tests are **black-box oriented** because they treat the calculator as a user-facing system and only validate inputs/outputs.

### 3. Functional vs Non-Functional Testing

The current suite is primarily **functional testing**: it verifies that calculator operations and reset behavior are correct. Non-functional testing (performance, security, usability/accessibility) is acknowledged but outside scope for this assignment phase.

### 4. Regression Testing

The test suite is used as a regression safety net. After every code change, running:

```bash
python -m pytest -q
```

confirms whether existing behavior still works. If a future change breaks arithmetic or interaction flow, the failing tests should immediately reveal the regression.

## Test Results Summary

Latest run command:

```bash
python -m pytest -q
```

Latest result: `10 passed`

| Test Name | Type | Status |
|---|---|---|
| `test_add_basic` | Unit | Pass |
| `test_subtract_basic` | Unit | Pass |
| `test_multiply_basic` | Unit | Pass |
| `test_divide_basic` | Unit | Pass |
| `test_divide_by_zero` | Unit | Pass |
| `test_add_negative_numbers` | Unit | Pass |
| `test_divide_decimal_result` | Unit | Pass |
| `test_multiply_large_numbers` | Unit | Pass |
| `test_full_user_flow_addition` | Integration | Pass |
| `test_clear_after_calculation_resets_display` | Integration | Pass |
