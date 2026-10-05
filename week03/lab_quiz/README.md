# Week 3 Lab: Order Approval Policy

## Boundary & Error Test Cases

| Case | Order Amount (TRY) | Available Stock | Requested Qty | Member? | Expected Status | Expected Final Price |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Below 500** | 499.99 | 10 | 2 | yes | APPROVED | 499.99 TRY |
| **Exact 500** | 500.00 | 10 | 2 | yes | APPROVED | 450.00 TRY (10% discount) |
| **Above 500** | 500.01 | 10 | 2 | yes | APPROVED | 450.01 TRY (10% discount) |
| **Insufficient Stock** | 600.00 | 2 | 5 | yes | REJECTED | No price displayed |

## Testing Notes

- **One test run:** Tested the boundary condition with an order amount of `499.99 TRY`, stock `10`, quantity `2`, and member set to `yes`.
-  Verified that the order was approved without applying the 10% discount.
- **One thing changed after testing:** Added an explicit input validation check (`requested_qty <= 0 or amount <= 0`) using a logical `or` operator to reject zero or negative quantities before checking warehouse stock.
