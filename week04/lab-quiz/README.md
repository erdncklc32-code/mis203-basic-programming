#Lab-quiz: Savings Goal Planner

Test Performed
Case Tested: Boundary & Exact Goal Check 
  Inputs:
     Starting balance: `0`
     Monthly deposit: `1000`
     Monthly interest rate (%): `0`
     Savings goal: `3000`
  Result: Loop terminated at month 3 with an exact balance of `3000.00`. Goal was flagged as reached in 3 months.

 Post-Testing Change
 Fix Applied: Added an early check (`if balance >= goal:`) right after input validation to notify the user immediately and skip rendering table rows, fulfilling Acceptance Check 4.
